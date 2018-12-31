# Using the tools

The python tools can be broken into two categories:

* end user tools
    + create_loadable_configs.py: variable substitutions for xml/set to create
    loadable output files archied in `loadable_configs`

* template administrator tools
    + build_full_templates.py: merge xml snippets into a full template file
    + create_set_spreadsheet.py: read the panorama and panos set commands .conf
    file and output a formula-based Excel file

## End user tools

The tools require python3.5 or later to be running in a virtual environment
with required packages installed.

The steps below are for a standard python virtual environment setup.
Python3.6 is used in the example. Python3.5 or python3.7 may also be used.

```bash
cd iron-skillet/tools
python3.6 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

#### create_loadable_configs.py
Creates both full xml and set commands outputs with user-specified variable
values contained in `config_variables.yaml`.

```bash
vi config_variables.yaml   [Edit variables for your local environment]
python3 ./create_loadable_configs.py
```

The output loadable templates, full and snippet configs, are saved in the
`loadable_configs` directory with name as `config prefix` + `datetime`.

Each run results in a new archive directory allowing for new configs with
modified variables.

## Template Admin
The admin utilities are also python based and assume a working python
environment. Directions for activating the virtual environment are above.

#### create_set_spreadsheet.py
Reads the set command .conf files in `/templates/panos/set_commands`
and `/templates/panorama/set_commands` along with `config_variables.yaml`
to generate a formula-based Excel spreadsheet of loadable set commands.

Output is in the respective set_commands directory.

#### build_full_templates.py
Starts with the baseline.xml file for panorama and panos then adds in
the xml snippets using the xml filenames and xpaths in the respective
metadata.yaml files from the snippets folders to create a complete
xml configuration file including jinja variables.

The resulting templates are stored in the `full` directory as
`iron_skillet_full.xml`


## Variables used by iron-skillet
For information about the variables used in iron-skillet can be found at:

[iron-skillet variables](https://iron-skillet.readthedocs.io/en/80dev/creating_loadable_configs.html#variables-list-and-descriptions)


