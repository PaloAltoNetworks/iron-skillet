# SLI Tooling
Documentation showing how to install/use SLI in the CLI 
and run the relevant tooling commands. SLI allows for the user
to run a type panos or panorama skillet against a config file
without the need to communicate to a live device.

**Quick overview of the SLI tooling capabilities**
* `sli spreadsheet`: Read the panorama and panos template set commands .yaml
    file and output a formula-based Excel file.
  
* `sli preview`: Variable substitutions for xml/set commands to create
    loadable output files archived in the given directory
  
* `sli load_config`: Load a candidate config into the NGFW 
    from an xml file

* `sli load_set`: Load a candidate config from a file containing 
    set commands
  
* `sli rollup_skillet`: Take in a .skillet.yaml file and performs a 
    rollup on it resulting in an output .skillet.yaml file with full
    XML snippets within.
  
* `sli rollup_playlist`: takes a playlist and turns it into a 
    standard skillet file.
  
* `sli template`: Render an xml or set command template and save it to a file.
    Templates will be created named as they are named in the skillet.
  
* `sli create_template`: Input a skillet and baseline.xml file to 
    Output a full XML Jinja file with default variables.
  

## Quick Start with PanHandler 
PanHandler is one of the recommended tools to use as a skillet player. 
See the [quick start guide for panHandler](https://live.paloaltonetworks.com/t5/Skillet-Tools/Install-and-Get-Started-With-Panhandler/ta-p/307916)
in Live.


## Quick Start with SLI
The SLI tool can also be used to run end user and template admin tools
quickly and efficiently.

**SLI Setup Steps**
```bash
> mkdir (choose a directory name)
> cd (into directory from above)
> python3 -m venv ./venv (create the venv)
> source ./venv/bin/activate (activate the venv)
> pip intall sli (install sli)
```

Once SLI has been installed it can be tested by running `sli` or
`sli --help` to see available commands. Visit the [SLI repository](https://gitlab.com/panw-gse/as/sli)
for more information.


## Using SLI to Create a SpreadSheet
SLI can be used to read a yaml file and render it to load into a spreadsheet.
To do this we can utilize the `sli spreadsheet` command. The command takes in
a template type yaml file that creates set commands, if a yaml file is
passed in that *doesn't* create set commands the `sli spreadsheet` command will error out.

The expected result is an output spreadsheet containing all the variable names, default values
and all loadable set commands with default variable values passed in.

**SLI Spreadsheet Command**
```bash
> sli spreadsheet -n {Template Skillet Name} -o {Output Directory}
Example usage
> sli spreadsheet -n skillet_set_command_panos_v10_1 -o /Users/bmutluoglu/Desktop/
```
Note: Make sure you are in the correct directory to access the template
skillet.

The -n flag takes in the name of the set command template skillet to be used.
The -o flag takes in a directory to store the output spreadsheet.


## Using SLI to Create a Loadable Config File
The user can use the `sli template` command to create a loadable config file.
with rendered Jinja variables. Running `sli template` allows the user to make 
changes and gives the user a template of what the config file would look like.
this command modifies the configuration of the device but as opposed to 
modifying it on your device it saves the config file to your specified directory.

**SLI Template Command**
```bash
> sli template -n {Panos or Panorama Skillet Name} {Output Directory Ending in File Name}
Example usage:
> sli template -sd ../ -ad -n skillet_full_panos_v10_1 ../loadable_configs/sample-cloud-AWS/panos
```

The `-sd` flag specifies a directory to load all skillets from. The `-n` flag takes 
in a panos/panorama skillet. The `-ad` flag accepts all the default values for 
skillet variables.


## Using SLI to Load a Config into the NGFW
The user can also load a config saved in an xml or txt file to the NGFW.
In order to load an xml config into the NGFW the user would use the
command `sli load_config`. In order to load a set command config into the
NGFW the user would use the command `sli load_set`. you can run these load 
config commands, specify the config file, and it will load the file into 
the device as the candidate config.

**SLI Load Commands**
```bash
> sli load_config -uc {Directory Containing File}
> sli load_set -uc {Directory Containing File}
Example usage:
> sli load_config -uc /Users/bmutluoglu/Desktop/testing.xml
> sli load_set -uc /Users/bmutluoglu/Desktop/testing.txt
```

The `-uc` flag uses the NGFW information previously stored in the SLI context.
You can check what is stored in your context by doing `sli show_context`. If you 
have no NGFW stored in your context you can run the command without the -uc flag
and enter in the information manually. Be sure to give the correct
path to the required xml/txt file when running this command.


## Using SLI to Rollup a Panos Skillet
The user can use SLI to create a full config file from an existing file.
The `sli rollup_skillet` command takes in a baseline skillet yaml file 
that performs a rollup on all the snippets within as is with no Jinja
variable rendering and then returns out a yaml skillet file containing
the full XML snippets. The output file will appear in the current 
working directory.

2 arguments, use the -n flag to get the playlist, specify the output file
make sure it exists, take the header data from it, copy everything over
and then override it.

**SLI Rollup Skillet Command**
```bash
> sli rollup_skillet {Input File Name} {Output File Name}
Example Usage:
> sli rollup_skillet skillet_full_panos_v10_1.meta-cnc.yaml out.skillet.yaml
```

The user passes in a skillet yaml filename in their current working
directory into the `Input File Name` section. The user can pass in
any file name they want as long as it ends with .skillet.yaml into the
`Output File Name` section.


## Using SLI to Transform a Playlist to a Skillet
The function sli `rollup_playlist` takes a playlist and turns it into a 
standard skillet file. This function gets rid of all includes statements
and expands them to be in the newly generated skillet file. The variables
section would capture all of the playlist variables. The snippets section
would contain all of the playlist snippets swapping the includes statements
with XML Xpaths and XML element information.

**SLI Rollup Playlist Command**
```bash
> sli rollup_playlist -n {Input Skillet Name} {Output File Name}
Example Usage:
> sli rollup_playlist -n skillet_full_panos_v10_1.meta-cnc.yaml out.skillet.yaml
```


## Using SLI to Output a Full XML Jinja Template
The user can use SLI to create a full XML Jinja Template configuration
through use of the `sli create_template` command. Running this command
with the proper inputs results in a large XML template file with all
the Jinja variables unrendered. This allows the user to load this
new output file as a jinja template, render it and have it be a valid
XML that works for a PANW device.

**SLI Create Template Command**
```bash
> sli create_template -n {Input Full Skillet Name} {Baseline XML File} {Output XML File Name}
Example Usage:
> sli create_template -n ironskillet_panos_10_1 templates/panos/baseline/baseline.xml out.xml
```

The create template sli command takes 3 arguments. First it takes the 
full skillet in the `Input Full Skillet Name` section which includes 
many other skillets each of which reference other XML Jinja templates.
It also takes the baseline XML file in the `Baseline XML File` section
and the users choice of output file in the `Output XML File Name` section.


## Build_all.sh Bash Script
Used by the IronSkillet administrator to generate the full config skillets,
loadable configs and spreadsheets. Simply run the bash script to populate
and update all templates/playlists/config directories.


## Variables used by iron-skillet
For information about the variables used in iron-skillet can be found at:

[iron-skillet variables](https://iron-skillet.readthedocs.io/en/docs_master/creating_loadable_configs.html#variables-list-and-descriptions)