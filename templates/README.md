# Iron-Skillet Templates

The templates directory houses the jinja-based templates for xml and set
configurations. These are not loadable configurations and require use
of scripting tools or other applications for rendering.

Also contained are the set commands spreadsheets that use Excel formulas,
allowing users to add in custom values specific to their deployment.

A complete list of template variables, along with descriptions, can be found
[here](https://iron-skillet.readthedocs.io/en/panos_v8.1/creating_loadable_configs.html#variables-list-and-descriptions)


##  Excel set command spreadsheets
The directories `templates/panorama/set_commands` and `templates/panos/set_commands`
each contain an Excel file with two worksheets:

* values: the list of variables and editable values
* set commands: formula-base set commands for value substitution

Users can edit the values worksheet based on their local needs. Set commands
can then be pasted to the configuration via CLI.

## Text-based set command files
The directories `templates/panorama/set_commands` and `templates/panos/set_commands`
also contain .conf files. These are jinja-based text files that require variable
value substitution.

**NOTE:** Jinja uses the format `{{ variable name }}` to place variables into
the configuration. Searching for `{{` makes it easy to find the variables
in the file.

The `create_loadable_configs.py` utility in `tools` is designed to read in
the `config_variables.yaml` file for the substitution.

For users that elect to do simple substitutions without python utilities,
they can use text-based 'find-and-replace' for each variable value. Searches
for variables can be specific by variable name or a generic search for `{{`
can be used.

The set_command directory also contains a .meta-cnc.yaml file detailing the
list of variables contained in the .conf file. This is used by external tools
(link???) for application-based value substitution.

## XML snippet files and metadata
The `snippets` directories found in `templates/panos` and `templates/panorama`
house sets of xml config files. These are subsets of a main configuration
specific to functional areas of the configuration such as security profiles,
device system configuration, logging, etc.

Designed primarily for API usage, the snippets are paired with a `.meta-cnc.yaml`
file that includes all variable names/defaults and an ordered list of file names
and their respective xpaths.

These snippets are also used by `tools/create_loadable_configs.py` to
substitute variable values and output full xml configurations into the
`loadable_configs` directory.

## Types of Panorama templates
Panorama has a multi-device management platform has various options for loading
configurations, namely shared and device-specific configurations. This results
in multiple template snippet types:

* `snippets`: A full Panorama configuration using shared device-group
and template configurations

* `snippets_dgstack_shared`: used to add additional device-groups
and stacks based on the shared model

* `snippets_not_shared`: a full Panorama configuration with the device-group
and stack containing all configuration elements. Nothing is shared.

* `snippets_dgstack_notshared`: used to add additional device-groups
and stack, each with full configuration elements. Nothing is shared.


## Details of template best practices
The details of what's in a template are located in the documentation:

[Panorama template information](https://iron-skillet.readthedocs.io/en/panos_v8.1/panorama_template_guide.html)

[PAN-OS template information](https://iron-skillet.readthedocs.io/en/panos_v8.1/panos_template_guide.html)
