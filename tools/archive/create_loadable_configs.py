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
Palo Alto Networks create_loadable_configs.py

Provides rendering of configuration templates with user defined values
Output is a set of loadable full configurations and set commands for Panos and Panorama

Edit the config_variables.yaml values and then run the script

This software is provided without support, warranty, or guarantee.
Use at your own risk.
'''

import datetime
import os
import shutil
import sys
import time
import getpass
import oyaml

from jinja2 import Environment, FileSystemLoader
from passlib.hash import des_crypt
from passlib.hash import md5_crypt
from passlib.hash import sha256_crypt
from passlib.hash import sha512_crypt

defined_filters = ['md5_hash', 'des_hash', 'sha512_hash']


def myconfig_newdir(myconfigdir_name, foldertime):
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
    myconfigdir = '{0}/{1}-{2}'.format(myconfigpath, myconfigdir_name, foldertime)
    if os.path.isdir(myconfigdir) is False:
        os.mkdir(myconfigdir, mode=0o755)
        print('\ncreated new archive folder {0}-{1}'.format(myconfigdir_name, foldertime))

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
    env.filters['des_hash'] = des_hash
    env.filters['sha512_hash'] = sha512_hash

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

    # copy the variables file used for the render into the my_template folder
    var_file = 'loadable_config_vars/config_variables.yaml'
    if os.path.isfile('{0}/{1}'.format(myconfigdir, var_file)) is False:
        vfilesrc = var_file
        vfiledst = '{0}/{1}'.format(myconfigdir, var_file)
        shutil.copy(vfilesrc, vfiledst)

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


def des_hash(txt):
    '''
    Returns the DES Hashed secret for use as a password hash in the PanOS configuration
    :param txt: text to be hashed
    :return: password hash of the string with salt and configuration information. Suitable to place in the phash field
    in the configurations
    '''
    return des_crypt.hash(txt)


def sha256_hash(txt):
    '''
    Returns the SHA256 Hashed secret for use as a password hash in the PanOS configuration
    :param txt: text to be hashed
    :return: password hash of the string with salt and configuration information. Suitable to place in the
    phash field in the configurations
    '''
    return sha256_crypt.hash(txt)


def sha512_hash(txt):
    '''
    Returns the SHA512 Hashed secret for use as a password hash in the PanOS configuration
    :param txt: text to be hashed
    :return: password hash of the string with salt and configuration information. Suitable to place in the
    phash field in the configurations
    '''
    return sha512_crypt.hash(txt)


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
    myconfig_path = myconfig_newdir(input_var['output_dir'], input_var['archive_time'])

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
    print('Welcome to Iron-Skillet'.center(80))
    print(' ')
    print('=' * 80)

    input_var = {}
    # archive_time used as part of the my_config directory name
    input_var['archive_time'] = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d_%H%M%S')
    print('\ndatetime used for folder creation: {0}\n'.format(input_var['archive_time']))

    # this prompts for the prefix name of the output directory
    input_var['output_dir'] = input('Enter the name of the output directory: ')

    # this prompts for the superuser username to be added into the configuration; no default admin/admin used
    input_var['ADMINISTRATOR_USERNAME'] = input('Enter the superuser administrator account username: ')

    print('\na phash will be created for superuser {0} and added to the config file\n'.format(
        input_var['ADMINISTRATOR_USERNAME']))
    passwordmatch = False

    # prompt for the superuser password to create a phash and store in the my_config files; no default admin/admin
    while passwordmatch is False:
        password1 = getpass.getpass("Enter the superuser administrator account password: ")
        password2 = getpass.getpass("Enter password again to verify: ")
        if password1 == password2:
            input_var['ADMINISTRATOR_PASSWORD'] = password1
            passwordmatch = True
        else:
            print('\nPasswords do not match. Please try again.\n')

    # loop through all config types that have their respective template folders
    for config_type in ['panos', 'panorama']:
        for render_type in ['full', 'set_commands']:
            replace_variables(config_type, render_type, input_var)