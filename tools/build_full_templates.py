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

# Author: Nathan Embery <nembery@paloaltonetworks.com>

'''
Palo Alto Networks Iron-Skillet build_full_templates

This tool combines the iron-skillet configuration snippets into a full configuration template.
This template can then be customized and applied to a new out-of-the-box PanOS NGFW or Panorama

This software is provided without support, warranty, or guarantee.
Use at your own risk.
'''


import os
import re
import sys
import oyaml

from xml.etree import ElementTree


def build_xpath(parent_doc, xpath, new_element_contents):
    """
    attaches a new Element to the document at the specified xpath with the specified contents
    if the xpath is something like '/config/xyz/abc' then create an element 'abc' and attach it as a
    subelement of 'xyz'.
    :param parent_doc: XML document to modify
    :param xpath: where to attach the new element
    :param new_element_contents: contents of the element
    :return: None. parent_doc is modified in place
    """

    # viewing the current xpath of interest
    print('working with this xpath:')
    print(xpath)
    # first of all, we need to fix the xpath to be relative (replace config with '.')
    modified_xpath = re.sub('^/config', '.', xpath)
    print(f'Checking xpath {modified_xpath}')
    # let's check if the xpath exists as is first of all
    is_present = parent_doc.find(modified_xpath)
    if is_present is not None:
        print('This one has been found')
        print('$' * 80)
        print(modified_xpath)
        print('$' * 80)
    else:
        # get a list of the tree elements that make up the xpath
        split_path = modified_xpath.split('/')
        # keep a list of things we'll need to manually construct
        path_to_build = []
        # begin infinite loop
        while True:
            # grab the last part of the xpath and start there
            # we will work backwards 'up' the tree until we find something that exists and build all the parts we
            # need back 'down' the tree
            tail = split_path[-1]
            print(f'tail is {tail}')
            # put the path back together minus the 'tail' (last node)
            parent_path = "/".join(split_path[:-1])
            print(f'parent_path is {parent_path}')
            # does this one exist?
            parent_element = parent_doc.find(parent_path)
            print(f'parent_element is {parent_element}')
            # go ahead and keep this around even if it exists or not
            # FIXME could be problematic if we ever need to merge items and not just overwrite them
            print(f'appending {tail} to path_to_build')
            path_to_build.append(tail)
            if parent_element is not None:
                print('found a parent element')
                print(parent_element)
                # found a node that exists so we can break out of the loop here
                break
            else:
                # pop tail from the path we're searching and try again
                split_path.pop()

        # we now have a path that exists and list of items we need to build
        # flesh out the tree if the path we need to build is larger than one, i.e. the leaf node needs to attach
        # to another node that doesn't yet exist, go ahead and build them all the up
        while len(path_to_build) > 1:
            p = path_to_build.pop()
            #print('appending {} to parent_element'.format(p))
            parent_element = ElementTree.SubElement(parent_element, p)

        # we should now have a document that has the tree fully built out to the xpath we want
        # wrap up the new_element_contents in the leaf node and attach it to the last known parent_element
        leaf_node = path_to_build[0]
        wrapped_snippet = f"<{leaf_node}>{new_element_contents}</{leaf_node}>"
        #print(wrapped_snippet)
        snippet_xml = ElementTree.fromstring(wrapped_snippet)
        #print('appending to parent_element')
        parent_element.append(snippet_xml)
        # print it out if needed
        # print(ElementTree.tostring(parent_element))


def generate_full_config_template(config_type):
    """
    Generates the full configuration template for a given configuration type (panos or panorama).
    This will use the load order
    :param config_type: currently supported: 'panos' or 'panorama'
    :return: will print full configs to STDOUT and also overwrite the full/iron_skillet_day1_template.xml
    """
    # get the path to the full baseline config for this config type
    full_config_file_path = os.path.abspath(os.path.join('..', 'templates', config_type, 'baseline', 'baseline.xml'))
    output_file_path = os.path.abspath(os.path.join('..', 'templates', config_type, 'full', 'iron_skillet_day1_template.xml'))
    metadata_file = os.path.abspath(os.path.join('..', 'templates', config_type, 'snippets_{0}'.format(config_type), 'metadata.yaml'))

    # open the file and read it in
    with open(full_config_file_path, 'r') as full_config_obj:
        full_config_string = full_config_obj.read()

    # debugging
    # print(full_config_string)

    # Begin XML manipulation. Grab the full config and parse into a DOM
    full_config_element = ElementTree.fromstring(full_config_string)

    full_config = ElementTree.ElementTree(full_config_element)

    # get the full path to the config directory we want (panos / panorama)
    config_path = os.path.abspath(os.path.join('..', 'templates', config_type))

    # append to the sys path for module lookup
    sys.path.append(config_path)

    # import both python files here based on config_type
    '''
    FIXME fix this to use the yaml file
    '''

    # read the metafile to get xpaths and load order
    try:
        with open(metadata_file, 'r') as snippet_metadata:
            service_config = oyaml.load(snippet_metadata.read())

    except IOError as ioe:
        print(f'Could not open metadata file {metadata_file}')
        print(ioe)
        sys.exit()

    # iterator through the metadata snippets load order
    # parse the snippets into XML objects
    # attach to the full_config dom
    for xml_snippet in service_config['snippets']:
        # xml_snippet is a set of attributes in the metadata.yaml file
        # that includes the xpaths and files listed in the proper load order
        snippet_name = xml_snippet['file']
        xpath = xml_snippet['xpath']
        snippet_path = os.path.join(config_path, 'snippets_{0}'.format(config_type), snippet_name)

        # skip snippets that aren't actually there for some reason
        if not os.path.exists(snippet_path):
            print(snippet_path)
            print('this snippet does not actually exist!')
            sys.exit()

        # read them in
        with open(snippet_path, 'r') as snippet_obj:
            snippet_string = snippet_obj.read()


        # verify this snippet has an xpath associated and if so, let's attach to the document
        #if xml_snippet in xpaths_configtype:

        # magic happens here
        # update the document in place to attach the snippet string in the correct place according to it's xpath
        build_xpath(full_config, xpath, snippet_string)

    print('=' * 80)
    raw_xml = str(ElementTree.tostring(full_config.getroot(), encoding='unicode'))
    #print(raw_xml)
    # open the output file for writing
    with open(output_file_path, 'w') as output_config_obj:
        output_config_obj.write(raw_xml)
    print('=' * 80)


if __name__ == '__main__':
    for config_type in ['panos', 'panorama']:
        generate_full_config_template(config_type)
