#!/usr/bin/env python3
'''
simple jinja substitution of values from variables.py
output to panorama and panos folders as loadable configs
'''

import os
import sys
import time
import datetime
from jinja2 import Environment, FileSystemLoader
from variables import xmlvar


def template_newfolder(template_path, fw_name):

    # Use the timestamp to create a unique filename
    foldertime = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d_%H%M%S')

    # check that configs folder exists and if not create a new one
    # then create snippets and full sub-directories

    archive_folder = f'{template_path}/{fw_name}-{foldertime}'
    if os.path.isdir(archive_folder) is False:
        os.mkdir(archive_folder, mode=0o755)
        os.mkdir(f'{archive_folder}/snippets-variables')
        os.mkdir(f'{archive_folder}/full')
        print(f'created new folder {template_path}/{foldertime} and sub-directories')

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


def template_save(snippet_name, archive_folder, element, render_type):

    print(f'..saving template for {snippet_name}')

    filename = f'{snippet_name}'

    with open(f'{archive_folder}/{render_type}/{filename}', 'w') as configfile:
        configfile.write(element)

    return


def replace_variables(config_type):

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

    archivefolder = template_newfolder(template_path, xmlvar['FW_NAME'])

    # iterator over the load order dict
    # parse the snippets into XML objects
    # save to archive folder
    for i in snippet_dict:
        # i is a key in the orderedDict

        print(f'\nworking with {i}')

        render_type = 'snippets-variables'

        snippet_name = "%s.xml" % snippet_dict[i][0]
        snippet_path = os.path.join(template_path, 'snippets-variables', snippet_name)

        # skip snippets that aren't actually there for some reason
        if not os.path.exists(snippet_path):
            print(snippet_path)
            print('this snippet does not actually exist!')
            continue

        # render snippet variables folder
        element = template_render(snippet_name, template_path, render_type)
        template_save(snippet_name, archivefolder, element, render_type)

    # render full config file
    print('\nworking with full config template')
    render_type = 'full'
    filename = 'iron-skillet-template.xml'
    element = template_render(filename, template_path, render_type)
    template_save(filename, archivefolder, element, render_type)

            
if __name__ == '__main__':
    for config_type in ['panos', 'panorama']:
        replace_variables(config_type)