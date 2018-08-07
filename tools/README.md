# Using the tools

### Creating loadable configurations


To create loadable template files with variable substitutions:

```
vi my_variables.py   [Edit variables for your local environment]
python3 ./build_my_configs.py
```

The output loadable templates, full and snippet configs, are in the `my_configs` directory with name as `config prefix` + `datetime`.

Each run results in a new archive directory allowing for new configs with modified variables.


### Template Admin

To build a full configuration from the supplied configuration baseline and snippets:

```bash
cd tools
python3 ./build_full_templates.py
```


The resulting templates are stored in the `full` directory as `iron_skillet_day1_template.xml`
