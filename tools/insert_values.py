#!/usr/bin/env python3
'''
simple jinja substitution of values from variables.py
output to panorama and panos folders as loadable configs
'''

import os
import sys
import time
import datetime
import shutil
from jinja2 import Environment, FileSystemLoader
from variables import xmlvar


def template_newsubdir(fw_name, foldertime):

    # get the full path to the config directory we want (panos / panorama)
    base_path = os.path.abspath(os.path.join('..', 'templates'))
    archive_dir = 'my_templates'

    # check that configs folder exists and if not create a new one
    # then create snippets and full sub-directories

    archive_folder = f'{base_path}/{archive_dir}/{fw_name}-{foldertime}'
    if os.path.isdir(archive_folder) is False:
        os.mkdir(archive_folder, mode=0o755)
        print(f'created new archive folder {fw_name}-{foldertime}')

    if os.path.isdir(f'{archive_folder}/{config_type}') is False:
        os.mkdir(f'{archive_folder}/{config_type}')
        os.mkdir(f'{archive_folder}/{config_type}/snippets-variables')
        os.mkdir(f'{archive_folder}/{config_type}/full')
        print(f'created new subdirectories for {config_type}')

    return archive_folder


def template_render(filename, template_path, render_type):

    '''
    Uses jinja substitutions from the xml snippets to load web form variables
    '''

    print(f'..creating template for {filename}')

    env = Environment(loader=FileSystemLoader(f'{template_path}/{render_type}'))
    template = env.get_template(filename)
    element = template.render(xmlvar)

    return element


def template_save(snippet_name, archive_folder, config_type, element, render_type):

    print(f'..saving template for {snippet_name}')

    filename = f'{snippet_name}'

    with open(f'{archive_folder}/{config_type}/{render_type}/{filename}', 'w') as configfile:
        configfile.write(element)

    # copy the variables file used for the render into the my_template folder
    if os.path.isfile(f'{archive_folder}/variables.py') is False:
        vfilesrc = 'variables.py'
        vfiledst = f'{archive_folder}/variables.py'
        shutil.copy(vfilesrc, vfiledst)

    return


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

    mytemplate_path = template_newsubdir(xmlvar['FW_NAME'], archivetime)

    # iterator over the load order dict
    # parse the snippets into XML objects
    # save to archive folder
    for i in snippet_dict:
        # i is a key in the orderedDict

        print(f'\nworking with {i}')

        render_type = 'snippets-variables'

        snippet_name = f'{snippet_dict[i][0]}.xml'
        snippet_path = os.path.join(template_path, 'snippets-variables', snippet_name)

        # skip snippets that aren't actually there for some reason
        if not os.path.exists(snippet_path):
            print(snippet_path)
            print('this snippet does not actually exist!')
            continue

        # render snippet variables folder
        element = template_render(snippet_name, template_path, render_type)
        template_save(snippet_name, mytemplate_path, config_type, element, render_type)

    # render full config file
    print('\nworking with full config template')
    render_type = 'full'
    filename = 'iron-skillet-template.xml'
    element = template_render(filename, template_path, render_type)
    template_save(filename, mytemplate_path, config_type, element, render_type)

            
if __name__ == '__main__':
    # Use the timestamp to create a unique folder name
    archivetime = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d_%H%M%S')
    print(f'datetime used for folder creation: {archivetime}')
    for config_type in ['panos', 'panorama']:
        replace_variables(config_type, archivetime)