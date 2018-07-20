#!/usr/bin/env python3
#
# Iron-Skillet build_full_templates
#
# This tool combines the iron-skillet configuration snippets into a full configuration template. This template
# can then be customized and applied to a new out-of-the-box PanOS NGFW or Panorama
#
# 07-17-18 nembery@paloaltonetworks.com
#
#

import os
import re
import sys
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
    # first of all, we need to fix the xpath to be relative (replace config with '.')
    modified_xpath = re.sub('^/config', '.', xpath)
    print('Checking xpath %s' % modified_xpath)
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
            # garb the last part of the xpath and start there
            # we will work backwards 'up' the tree until we find something that exists and build all the parts we
            # need back 'down' the tree
            tail = split_path[-1]
            print('tail is {}'.format(tail))
            # put the path back together minus the 'tail' (last node)
            parent_path = "/".join(split_path[:-1])
            print('parent_path is {}'.format(parent_path))
            # does this one exist?
            parent_element = parent_doc.find(parent_path)
            print('parent_element is {}'.format(parent_element))
            # go ahead and keep this around even if it exists or not
            # FIXME could be problematic if we ever need to merge items and not just overwrite them
            print('appending {} to path_to_build'.format(tail))
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
            print('appending {} to parent_element'.format(p))
            parent_element = ElementTree.SubElement(parent_element, p)

        # we should now have a document that has the tree fully built out to the xpath we want
        # wrap up the new_element_contents in the leaf node and attach it to the last known parent_element
        leaf_node = path_to_build[0]
        # FIXME - this string formatting could prolly be done a bit better
        wrapped_snippet = "<{l}>{c}</{l}>".format(l=leaf_node, c=new_element_contents)
        print(wrapped_snippet)
        snippet_xml = ElementTree.fromstring(wrapped_snippet)
        print('appending to parent_element')
        parent_element.append(snippet_xml)
        # print it out if needed
        # print(ElementTree.tostring(parent_element))


def generate_full_config_template(config_type):
    """
    Generates the full configuration template for a given configuration type (panos or panorama).
    This will use the load order
    :param config_type: currently supported: 'panos' or 'panorama'
    :return: will print full configs to STDOUT and also overwrite the full/iron-skillet-template.xml
    """
    # get the path to the full baseline config for this config type
    full_config_file_path = os.path.abspath(os.path.join('..', 'templates', config_type, 'baseline', 'baseline.xml'))
    output_file_path = os.path.abspath(os.path.join('..', 'templates', config_type, 'full', 'iron-skillet-template.xml'))

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

    # import both python files here
    load_order = __import__("panos_snippet_load_order")
    xpaths_list = __import__("panos_xpaths_list")

    # iterator over the load order dict
    # parse the snippets into XML objects
    # attach to the full_config dom
    for i in load_order.Panos_gold_template_dict:
        # i is a key in the orderedDict of
        # it is also the name of the XML snippet we want to load
        snippet_name = "%s.xml" % i
        snippet_path = os.path.join(config_path, 'snippets-variables', snippet_name)

        # skip snippets that aren't actually there for some reason
        if not os.path.exists(snippet_path):
            print('this snippet does not actually exist!')
            continue

        # read them in
        with open(snippet_path, 'r') as snippet_obj:
            snippet_string = snippet_obj.read()

        # verify this snippet has an xpath associated and if so, let's attach to the document
        if i in xpaths_list.xpaths_Panos:
            xpath = xpaths_list.xpaths_Panos[i]
            # magic happens here
            # update the document in place to attach the snippet string in the correct place according to it's xpath
            build_xpath(full_config, xpath, snippet_string)

    print('=' * 80)
    raw_xml = str(ElementTree.tostring(full_config.getroot(), encoding='unicode'))
    print(raw_xml)
    # open the output file for writing
    with open(output_file_path, 'w') as output_config_obj:
        output_config_obj.write(raw_xml)
    print('=' * 80)


if __name__ == '__main__':
    for config_type in ['panos', 'panorama']:
        generate_full_config_template(config_type)
