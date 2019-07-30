# Copyright (c) 2018, Palo Alto Networks
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

# Author: Scott Shoaf <sshoaf@paloaltonetworks.com>

'''
Palo Alto Networks create_batch.py

creates a roll-up of loadable configs in the repo for the various
options: mgmt dhcp/static and public cloud flavors

Edit the config_variables.yaml values and then run the script

This software is provided without support, warranty, or guarantee.
Use at your own risk.
'''

import os
import sys
import oyaml

from jinja2 import Environment, FileSystemLoader
from passlib.hash import md5_crypt
from build_full_templates import build_xpath, generate_full_config_template
from create_set_spreadsheet import create_spreadsheet

defined_filters = ['md5_hash']


def myconfig_newdir(myconfigdir_name):
    '''
    create a new main loadable_configs folder if required then new subdirectories for configs
    :param myconfigdir_name: prefix folder name from the my_variables.py file
    :param foldertime: datetime when script run; to be used as suffix of folder name
    :return: the myconfigdir full path name
    '''

    # get the full path to the config directory we want (panos / panorama)
    myconfigpath = os.path.abspath(os.path.join('..', 'loadable_configs'))
    if os.path.isdir(myconfigpath) is False:
        os.mkdir(myconfigpath, mode=0o755)
        print('created new loadable config directory')

    # check that configs folder exists and if not create a new one
    # then create snippets and full sub-directories
    myconfigdir = '{0}/{1}'.format(myconfigpath, myconfigdir_name)
    if os.path.isdir(myconfigdir) is False:
        os.mkdir(myconfigdir, mode=0o755)
        print('\ncreated new archive folder {0}'.format(myconfigdir_name))

    if os.path.isdir('{0}/{1}'.format(myconfigdir, config_type)) is False:
        os.mkdir('{0}/{1}'.format(myconfigdir, config_type))
        print('created new subdirectories for {0}'.format(config_type))

    return myconfigdir


def create_context(config_var_file):
    # read the metafile to get variables and values
    try:
        with open(config_var_file, 'r') as var_metadata:
            variables = oyaml.safe_load(var_metadata.read())

    except IOError as ioe:
        print(f'Could not open metadata file {config_var_file}')
        print(ioe)
        sys.exit()

    # grab the metadata values and convert to key-based dictionary
    jinja_context = dict()

    for snippet_var in variables['variables']:
        jinja_context[snippet_var['name']] = snippet_var['value']

    return jinja_context


def yaml2dict(config_var_file):
    # read the metafile to get variables and values
    try:
        with open(config_var_file, 'r') as var_metadata:
            variables = oyaml.safe_load(var_metadata.read())

    except IOError as ioe:
        print(f'Could not open metadata file {config_var_file}')
        print(ioe)
        sys.exit()

    return variables


def template_render(filename, template_path, render_type, context):
    '''
    render the jinja template using the context value from config_variables.yaml
    :param filename: name of the template file
    :param template_path: path for the template file
    :param render_type: type if full or set commands; aligns with folder name
    :param context: dict of variables to render
    :return: return the rendered xml file and set conf file
    '''

    print('..creating template for {0}'.format(filename))

    env = Environment(loader=FileSystemLoader('{0}/{1}'.format(template_path, render_type)))

    # load our custom jinja filters here, see the function defs below for reference
    env.filters['md5_hash'] = md5_hash

    template = env.get_template(filename)
    rendered_template = template.render(context)

    return rendered_template


def template_save(snippet_name, myconfigdir, config_type, element):
    '''
    after rendering the template save to the myconfig directory
    each run saves with a unique prefix name + datetime
    :param snippet_name: name of the output file
    :param myconfigdir: path to the my_config directory
    :param config_type: based on initial run list; eg. panos or panorama
    :param element: xml element rendered based on input variables; used as folder name
    :param render_type: type eg. if full or snippets; aligns with folder name
    :return: no value returned (future could be success code)
    '''

    print('..saving template for {0}'.format(snippet_name))

    filename = snippet_name

    with open('{0}/{1}/{2}'.format(myconfigdir, config_type, filename), 'w') as configfile:
        configfile.write(element)

    return


# define functions for custom jinja filters
def md5_hash(txt):
    '''
    Returns the MD5 Hashed secret for use as a password hash in the PanOS configuration
    :param txt: text to be hashed
    :return: password hash of the string with salt and configuration information. Suitable to place in the phash field
    in the configurations
    '''
    return md5_crypt.hash(txt)


def replace_variables(config_type, render_type, input_var):
    '''
    get the input variables and render the output configs with jinja2
    inputs are read from the template directory and output to my_config
    :param config_type: panos or panorama to read/write to the respective directories
    :param archivetime: datetimestamp used for the output my_config folder naming
    '''

    config_variables = 'config_variables.yaml'

    # create dict of values for the jinja template render
    context = create_context(config_variables)

    # update context dict with variables from user input
    for snippet_var in input_var:
        context[snippet_var] = input_var[snippet_var]

    # get the full path to the output directory we want (panos / panorama)
    template_path = os.path.abspath(os.path.join('..',
                                                 'templates', config_type))

    # append to the sys path for module lookup
    sys.path.append(template_path)

    # output subdir located in loadable_configs dir
    myconfig_path = myconfig_newdir(input_var['output_dir'])

    # render full and set conf files
    print('\nworking with {0} config template'.format(render_type))
    if render_type == 'full':
        filename = 'iron_skillet_{0}_full.xml'.format(config_type)
    if render_type == 'set_commands':
        filename = 'iron_skillet_{0}_full.conf'.format(config_type)

    element = template_render(filename, template_path, render_type, context)
    template_save(filename, myconfig_path, config_type, element)

    print('\nconfigs have been created and can be found in {0}'.format(myconfig_path))
    print('along with the metadata values used to render the configs\n')

    return


if __name__ == '__main__':
    # Use the timestamp to create a unique folder name

    print('=' * 80)
    print(' ')
    print('Welcome to Iron-Skillet batch create loadable configs'.center(80))
    print(' ')
    print('=' * 80)

    # build full config from snippets
    print('Building full configs...')
    for config_type in ['panos', 'panorama']:
        generate_full_config_template(config_type)

    # create sample loadable configs as part of core repo
    # uses full config template so updated after new full config build
    input_var = {}
    # get batch variables define loadable_config types and values
    loadable_types = yaml2dict('batch_variables.yaml')

    for loadable in loadable_types['variables']:

        # this prompts for the prefix name of the output directory
        input_var['output_dir'] = loadable['name']
        input_var['MGMT_TYPE'] = loadable['MGMT_TYPE']
        input_var['PANORAMA_TYPE'] = loadable['PANORAMA_TYPE']

        # loop through all config types that have their respective template folders
        for config_type in ['panos', 'panorama']:
            for render_type in ['full', 'set_commands']:
                replace_variables(config_type, render_type, input_var)

    # create set command spreadsheet based on set command text file
    for config_type in ['panos', 'panorama']:
        create_spreadsheet(config_type)
