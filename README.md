# IronSkillet Day One Configuration Template


The purpose of the IronSkillet project is to provide day-one best practice
configuration templates that can be loaded into a Palo Alto Networks
Next-Generation Firewall or Panorama management platform.

Once loaded, the configuration can be augmented with use case specific
security policies and other deployment requirements including interfaces,
zones, and NAT.

Detailed information can be found in the 
[IronSkillet Documentation](https://iron-skillet.readthedocs.io)

The docs include a [IronSkillet Visual Guide](https://iron-skillet.readthedocs.io/en/docs_master/viz_guide_panos.html)
 for a view of IronSkillet from a GUI perspective.

## Quick Start
The templates are provided with a variety of usage options based
on the user operational environment.


#### panHandler Skillet Player
A quick an easy way to play IronSkillet and other skillets is with the panHandler application.

The [panHandler quick start guide](https://live.paloaltonetworks.com/t5/Skillet-Tools/Install-and-Get-Started-With-Panhandler/ta-p/307916)
in the Skillet District Live community walks you through installation and usage including
how to import the IronSkillet skillets.


#### Getting templates from the repo
Users can either grab content file-by-file from the github repo or download all
content to a local drive.

**TIP:** when copying or getting text files from the repo, users should select
the `Raw` format. This is found as a GUI option when viewing the file.

Downloading the files is done using a `git clone` command or a direct
download of the repo as a zip file.

```
git clone https://github.com/PaloAltoNetworks/iron-skillet.git
```


#### Loading configurations using IronSkillet defaults
The `loadable_configs` directory contains a variety of ready-to-go
NGFW and Panorama configurations based on iron-skillet template defaults.
These can be loaded 'as-is' and later updated using the GUI or CLI.

The two options to load are:

* ...full.xml: complete xml configuration to import and load
* ...full.conf: complete list of CLI-based set commands

###### Full XML configuration file
Loading the full XML file as a candidate configuration:

```
* Log into the GUI
* Go to `Device` > `Setup` > `Operations`
* Choose `Import named configuration snapshot`
* Select the file from a local directory to import
* Choose `Load named configuration snapshot`
* Review the loaded configuration and `commit` to apply changes
```

**WARNING:** this configuration `replaces` the existing configuration and
is not a merge of configurations. Merging configurations requires the
use of `load config partial` referencing select xpaths to be loaded and merged.

###### SET commands
Using `set` commands to load in a configuration:

* Log into the CLI
* Enter `configure` to enter configuration mode
* Copy a cluster of set commands, 30-40 lines recommended as maximum
* Paste into the command line and hit `Enter` to ensure the last line is entered
* Add all set commands in the conf file
* Enter `commit`

**TIP:** Before entering configure mode, you can use `set cli scripting-mode on`
to paste in a higher volume of lines. This will however remove the option to
use '?' as a command-line helper. If scripting mode is enabled and you wish
to disable, simply return to CLI operation mode with `exit` and enter
'set cli scripting-mode off'.

#### Editing loaded configurations
The detailed documentation provides a list of variables that can be edited
and instructions for GUI and CLI edits to these values.

[IronSkillet variables](https://iron-skillet.readthedocs.io/en/docs_master/creating_loadable_configs.html#variables-list-and-descriptions)


#### Using the SET command spreadsheet to edit values
Found in `templates/panorama/set_commands` and `templates/panos/set_commands`
are formula-based Excel files.

The cells in the `values` worksheet can be edited to create a
localized configuration without the iron-skillet defaults. This updates the
values in the `set commands` worksheet. Using the set command steps above,
the configuration can then be loaded using the CLI.

**WARNING:** only update the `values` worksheet. Using caution if editing
the worksheets to ensure cell references and formulas are not incorrect.

### Tools scripts
As an alternative, the `tools` directory contains python scripts to help
manage and create loadable configurations. Additional documentation can be
found in `tools`.


## Recommended Reading for Additional Best Practice Configuration Steps

Prior to utilizing these configuration templates, it is important to
familiarize yourself with the best practice recommendations for
Internet Gateway, Datacenter, Wildfire, L4-L7 evasions and other use cases.

[Best Practice Recommendations](https://docs.paloaltonetworks.com/best-practices)

While useful as suggestions and recommendations, the user is still required
to manually use the GUI or CLI to configure each recommendation.


## Contributing
Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on how you can help contribute to this project.

## Support
This is a Palo Alto Networks contributed project.

## Authors

* Scott Shoaf [(@scotchoaf)](https://github.com/scotchoaf)
* Suzi VanPatten - [(@suzivp)](https://github.com/suzivp)
* Edward Arcuri - [(@sdndude)](https://github.com/sdndude)
* Bob Hagen - [(@stealthllama)](https://github.com/stealthllama)

See also the list of [contributors](https://github.com/PaloAltoNetworks/iron-skillet/contributors) who have participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
