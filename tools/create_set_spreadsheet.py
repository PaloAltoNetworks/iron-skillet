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
Palo Alto Networks Iron-Skillet create_set_spreadsheet

This tool turns the set-based template file into a formula-based spreadsheet
This template can then be customized and applied to a new out-of-the-box PanOS NGFW or Panorama

This software is provided without support, warranty, or guarantee.
Use at your own risk.
'''


import os
import sys
import oyaml
import xlsxwriter

from jinja2 import Environment, meta


def create_spreadsheet(config_type):
    """
    Generates the full configuration template for a given configuration type (panos or panorama).
    This will use the load order
    :param config_type: currently supported: 'panos' or 'panorama'
    :return: will print full configs to STDOUT and also overwrite the full/iron_skillet_full.xml
    """
    # get the path to the full baseline config for this config type


    # get the full path to the config directory we want (panos / panorama)
    set_path = os.path.abspath(os.path.join('..', 'templates', config_type, 'set_commands'))

    # append to the sys path for module lookup
    sys.path.append(set_path)

    set_file = '{0}/iron_skillet_{1}_full.conf'.format(set_path, config_type)
    config_variables = 'config_variables.yaml'.format(set_path)

    print('creating workbook based on {0}'.format(set_file))
    # Create a workbook and add worksheets.
    workbook = xlsxwriter.Workbook('{0}/iron_skillet_{1}_full.xlsx'.format(set_path, config_type))

    # add columns and format width
    worksheet_values = workbook.add_worksheet('values')
    worksheet_values.set_column(0, 0, 30)
    worksheet_values.set_column(1, 1, 30)
    worksheet_set = workbook.add_worksheet('set commands')

    # Add a bold format to use to highlight cells.
    bold = workbook.add_format({'bold': 1})

    # read the metafile to get variables and values
    try:
        with open(config_variables, 'r') as set_metadata:
            set_variables = oyaml.safe_load(set_metadata.read())

    except IOError as ioe:
        print(f'Could not open metadata file {config_variables}')
        print(ioe)
        sys.exit()

    row = 1

    # positional list to map variables into formula
    # padded since variables start at row 2 with zero offset
    variable_list = ['first row', 'second row']

    worksheet_values.write(0, 0, 'Variable Name', bold)
    worksheet_values.write(0, 1, 'Variable Value', bold)
    worksheet_values.write(0, 2, 'Description', bold)

    # iterate through each variable in the yaml file and
    # add to variable worksheet including defaults
    for variable in set_variables['variables']:
        print('working with variable: {0}'.format(variable))
        worksheet_values.write(row, 0, variable['name'])
        worksheet_values.write(row, 1, variable['value'])
        worksheet_values.write(row, 2, variable['description'])
        variable_list.append(variable['name'])

        row += 1

    row = 1

    try:
        with open(set_file, 'r') as set_commands:
            set_list = set_commands.readlines()

    except IOError as ioe:
        print(f'Could not open metadata file {set_file}')
        print(ioe)
        sys.exit()

    for line in set_list:

        # read the line and create a variable set
        env = Environment()
        var_set = sorted(meta.find_undeclared_variables(env.parse(line)))

        # check if line has a single variable
        if len(var_set) == 1:
            # replace quote with 2xquotes to be excel friendly
            line = line.replace('"', '""').strip()
            var_name = var_set[0]
            jinja_var = '{{ ' + var_name + ' }}'
            cell_pos = variable_list.index(var_name)

            # formula format  = =SUBSTITUTE("set deviceconfig system dns-setting servers primary {0}", "{0}", '0-Config Values'!B21)
            form_line = '=SUBSTITUTE("{0}", "{1}", \'values\'!B{2})'.format(line, jinja_var, cell_pos)
            # print(form_line)
            worksheet_set.write(row, 0, form_line)

        # check if line has 2 variables when requires nested SUBSTITUTEs
        elif len(var_set) == 2:
            # replace quote with 2xquotes to be excel friendly
            line = line.replace('"', '""').strip()
            var_name_0 = var_set[0]
            jinja_var_0 = '{{ ' + var_name_0 + ' }}'
            cell_pos_0 = variable_list.index(var_name_0)

            var_name_1 = var_set[1]
            jinja_var_1 = '{{ ' + var_name_1 + ' }}'
            cell_pos_1 = variable_list.index(var_name_1)

            # inner is first substitute and all is nested substitute for excel
            form_line_inner = 'SUBSTITUTE("{0}", "{1}", \'values\'!B{2})'.format(line, jinja_var_0, cell_pos_0)
            form_line_all = '=SUBSTITUTE({0}, "{1}", \'values\'!B{2})'.format(form_line_inner, jinja_var_1, cell_pos_1)
            worksheet_set.write(row, 0, form_line_all)

        else:
            # replace quotes and also remove hidden quotes for standard non-formula cells
            line = line.replace('"', '""').strip()
            worksheet_set.write(row, 0, line)

        row += 1

    workbook.close()
    print('...done')

if __name__ == '__main__':

    print('=' * 80)
    print(' ')
    print('Welcome to Iron-Skillet spreadsheet creator'.center(80))
    print(' ')
    print('=' * 80)

    for config_type in ['panos', 'panorama']:
        create_spreadsheet(config_type)
