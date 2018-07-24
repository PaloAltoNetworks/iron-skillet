# Using the tools

To build a full configuration from the supplied configuration snippets:

```bash
cd tools
python3 ./build_full_templates.py
```


The resulting templates are stored in the `full` directory as `iron-skillet-template.xml`


To create loadable template files with variable substitutions:

```
vi variables.py   [Edit variables to the local environment]
python3 ./insert_values.py
```

The output loadable templates are in the `templates/my_templates` directory with name as `device name` + `datetime`.

Each run results in a new archive directory allowing for new configs with modified variables.

