# Using the tools

The python tools can be broken into two categories:

* end user tools
    + create_loadable_configs.py: variable substitutions for xml/set to create
    loadable output files archied in `loadable_configs`
* template administrator tools
    + build_full_templates.py: merge xml snippets into a full template file
    + create_set_spreadsheet.py: read the panorama and panos set commands .conf
    file and output a formula-based Excel file

The first section will focus on the user tools.

### First Time Use and Python Set Up

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

### Creating loadable configurations

To create loadable template files with variable substitutions:

```bash
vi config_variables.yaml   [Edit variables for your local environment]
python3 ./create_loadable_configs.py
```

The output loadable templates, full and snippet configs, are in the `loadable_configs` directory with name as `config prefix` + `datetime`.

Each run results in a new archive directory allowing for new configs with modified variables.


## Template Admin

To build a full configuration from the supplied configuration baseline and snippets:

```bash
cd tools
python3 ./build_full_templates.py
```


The resulting templates are stored in the `full` directory as `iron_skillet_day1_template.xml`


