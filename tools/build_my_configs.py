#!/usr/bin/env python3
'''
simple jinja substitution of values from my_variables.py
output to panorama and panos folders as loadable configs
'''

import datetime
import os
import shutil
import sys
import time

from jinja2 import Environment, FileSystemLoader
from my_variables import xmlvar
from passlib.hash import des_crypt
from passlib.hash import md5_crypt
from passlib.hash import sha512_crypt

defined_filters = ['md5_hash', 'des_hash', 'sha512_hash']


def myconfig_newdir(myconfigdir_name, foldertime):
    # get the full path to the config directory we want (panos / panorama)
    myconfigpath = os.path.abspath(os.path.join('..', 'my_configs'))
    if os.path.isdir(myconfigpath) is False:
        os.mkdir(myconfigpath, mode=0o755)
        print('created new myconfig directory')

    # check that configs folder exists and if not create a new one
    # then create snippets and full sub-directories

    myconfigdir = f'{myconfigpath}/{myconfigdir_name}-{foldertime}'
    if os.path.isdir(myconfigdir) is False:
        os.mkdir(myconfigdir, mode=0o755)
        print(f'created new archive folder {myconfigdir_name}-{foldertime}')

    if os.path.isdir(f'{myconfigdir}/{config_type}') is False:
        os.mkdir(f'{myconfigdir}/{config_type}')
        os.mkdir(f'{myconfigdir}/{config_type}/snippets')
        os.mkdir(f'{myconfigdir}/{config_type}/full')
        print(f'created new subdirectories for {config_type}')

    return myconfigdir


def template_render(filename, template_path, render_type):
    '''
    Uses jinja substitutions from the xml snippets to load web form variables
    '''

    print(f'..creating template for {filename}')

    env = Environment(loader=FileSystemLoader(f'{template_path}/{render_type}'))

    # load our custom jinja filters here, see the function defs below for reference
    env.filters['md5_hash'] = md5_hash
    env.filters['des_hash'] = des_hash
    env.filters['sha512_hash'] = sha512_hash

    template = env.get_template(filename)
    element = template.render(xmlvar)

    return element


def template_save(snippet_name, myconfigdir, config_type, element, render_type):
    print(f'..saving template for {snippet_name}')

    filename = f'{snippet_name}'

    with open(f'{myconfigdir}/{config_type}/{render_type}/{filename}', 'w') as configfile:
        configfile.write(element)

    # copy the variables file used for the render into the my_template folder
    if os.path.isfile(f'{myconfigdir}/my_variables.py') is False:
        vfilesrc = 'my_variables.py'
        vfiledst = f'{myconfigdir}/my_variables.py'
        shutil.copy(vfilesrc, vfiledst)

    return
  
# define functions for custom jinja filters
def md5_hash(txt):
    """
    Returns the MD5 Hashed secret for use as a password hash in the PanOS configuration
    :param txt: text to be hashed
    :return: password hash of the string with salt and configuration information. Suitable to place in the phash field
    in the configurations
    """
    return md5_crypt.hash(txt)


def des_hash(txt):
    """
    Returns the DES Hashed secret for use as a password hash in the PanOS configuration
    :param txt: text to be hashed
    :return: password hash of the string with salt and configuration information. Suitable to place in the phash field
    in the configurations
    """
    return des_crypt.hash(txt)


def sha512_hash(txt):
    """
    Returns the SHA512 Hashed secret for use as a password hash in the PanOS configuration
    :param txt: text to be hashed
    :return: password hash of the string with salt and configuration information. Suitable to place in the
    phash field in the configurations
    """
    return sha512_crypt.hash(txt)


def replace_variables(config_type, archivetime):
    # get the full path to the config directory we want (panos / panorama)
    template_path = os.path.abspath(os.path.join('..', 'templates', config_type))

    # append to the sys path for module lookup
    sys.path.append(template_path)

    # import both python files here based on config_type
    load_order = __import__(f'{config_type}_snippet_load_order')

    if config_type == 'panos':
        snippet_dict = load_order.panos_gold_template_dict
    elif config_type == 'panorama':
        snippet_dict = load_order.panorama_gold_template_dict
    else:
        print('Oops. Not a supported config type')
        sys.exit()

    myconfig_path = myconfig_newdir(xmlvar['MYCONFIG_DIR'], archivetime)

    # iterator over the load order dict
    # parse the snippets into XML objects
    # save to archive folder
    for i in snippet_dict:
        # i is a key in the orderedDict

        print(f'\nworking with {i}')

        render_type = 'snippets'

        snippet_name = f'{snippet_dict[i][0]}.xml'
        snippet_path = os.path.join(template_path, 'snippets', snippet_name)

        # skip snippets that aren't actually there for some reason
        if not os.path.exists(snippet_path):
            print(snippet_path)
            print('this snippet does not actually exist!')
            continue

        # render snippet variables folder
        element = template_render(snippet_name, template_path, render_type)
        template_save(snippet_name, myconfig_path, config_type, element, render_type)

    # render full config file
    print('\nworking with full config template')
    render_type = 'full'
    filename = 'iron_skillet_day1_template.xml'
    element = template_render(filename, template_path, render_type)
    template_save(filename, myconfig_path, config_type, element, render_type)


    print(f'\nconfigs have been created and can be found in {myconfig_path}')
    print('along with the my_variables.py values used to render the configs\n')


if __name__ == '__main__':
    # Use the timestamp to create a unique folder name
    archive_time = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d_%H%M%S')
    print(f'datetime used for folder creation: {archive_time}')
    for config_type in ['panos', 'panorama']:
        replace_variables(config_type, archive_time)
