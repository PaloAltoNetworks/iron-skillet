# Loadable configurations using iron-skillet defaults

This directory contains a suite of ready-to-go configurations that are
immediately usable with iron-skillet defaults. Full configurations using
set commands and xml are provided.

## Loadable config options

* sample-cloud options: management interfaces for Panorama and PAN-OS use DHCP
* sample-mgmt-dhcp: PAN-OS default to DHCP while Panorama uses a static IP interface
* sample-mgmt-static: both PAN-OS and Panorama use static IP Interfaces for management


## Quick Start
The templates are provided with a variety of usage options based
on the user operational environment. The Quick Start covers non-python
template variable editing and loading options.

As an alternative, the `tools` directory contains python scripts to help
manage and create loadable configurations. Additional documentation can be
found in `tools`.

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


#### Loading configurations using iron-skillet defaults
The `loadable_configs` directory contains a variety of ready-to-go
NGFW and Panorama configurations based on iron-skillet template defaults.
These can be loaded 'as-is' and later updated using the GUI or CLI.

The two options to load are:

* ...full.xml: complete xml configuration to import and load
* ...full.conf: complete list of CLI-based set commands

###### Full XML configuration file
Loading the full XML file as a candidate configuration:

* Log into the GUI
* Go to `Device` > `Setup` > `Operations`
* Choose `Import named configuration snapshot`
* Select the file from a local directory to import
* Choose `Load named configuration snapshot`
* Review the loaded configuration and `commit` to apply changes

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

## Editing loaded configurations
The detailed documentation provides a list of variables that can be edited
and instructions for GUI and CLI edits to the these values.

[Iron-Skillet Variables list](https://iron-skillet.readthedocs.io/en/panos_v9.0/creating_loadable_configs.html#variables-list-and-descriptions)

## Python utilities and loadable configs
Users that take advantage of the python utilities in `tools` will have their
configurations output into these directories using a tag name and timestamp.

Along with panos/panorama and xml/set command files will be the `config_variables.yaml'
file containing the variables used when the script was run. This file can be
copied into the tools folder as needed to recreate a configuration output.