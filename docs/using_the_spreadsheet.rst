.. _using_the_spreadsheet:

Using the Formula-based Excel Spreadsheet
=========================================

For users who want to customize their configuration before loading without the use of python utilities, this is a preferred
model for configuration.

The spreadsheets are found in the repo in ``templates/panorama/set_commands`` and ``templates/panos/set_commands``.

The ``values`` worksheet can be updated with user-specific values. Formulas embedded in the ``set commands`` worksheet
will use the user added values.

Once the spreadsheet is updating, the traditional copy-and-paste model can be used to load the configuration using the CLI.


.. Warning::
    The set commands use formulas referencing cells in the values worksheet. Use caution if making changes to the base
    spreadsheet to avoid incorrect references to cell values.

