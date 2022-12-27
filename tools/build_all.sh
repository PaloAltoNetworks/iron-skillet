#!/bin/bash
# This is a bash script to run all SLI Tooling commands. This script
# is meant to replace the build_all.py python script which ran all
# The .py functions found within the IronSkillet Tooling directory.
# This bash script is still a work in progress.
#MGM Cloud is default
MGMT_STATIC="MGMT_TYPE=static"
MGMT_DHCP="MGMT_TYPE=dhcp"
#Panorama Static is default
PANORAMA_CLD="PANORAMA_TYPE=cloud"
CONFIG_ALL_PANOS="config_mgmt_intf=yes config_dns=yes config_admin_user=yes"
CONFIG_ALL_PANORAMA="config_admin_panorama=yes config_mgmt_intf_panorama=yes"

echo "Checking if a Venv already exists in given directory"
if [ ! -d "./venv" ]
then
  echo "Directory ./venv DOES NOT exist."
  echo "Creating the venv"
  python3 -m venv ./venv
  echo "Activate the venv"
  source ./venv/bin/activate
  echo "Install Sli in venv"
  pip install sli
else
  echo "Directory ./venv exists"
  echo "Activate the venv"
  source ./venv/bin/activate
  echo "Upgrade SLI to the latest"
  pip install sli --upgrade
fi
echo "Run SLI"
sli
echo "Perform SLI Load to load all skillets"
cd ..
sli load
cd tools

echo "Create loadable_config directories"
cd ..
mkdir loadable_configs
cd loadable_configs
mkdir sample-cloud-AWS
cd sample-cloud-AWS
mkdir panorama
mkdir panos
cd ..
mkdir sample-cloud-Azure
cd sample-cloud-Azure
mkdir panorama
mkdir panos
cd ..
mkdir sample-cloud-GCP
cd sample-cloud-GCP
mkdir panorama
mkdir panos
cd ..
mkdir sample-mgmt-dhcp
cd sample-mgmt-dhcp
mkdir panorama
mkdir panos
cd ..
mkdir sample-mgmt-static
cd sample-mgmt-static
mkdir panorama
mkdir panos
cd ..
mkdir sample-set-commands
cd sample-set-commands
mkdir panorama
mkdir panos
if [ ! -d "./README.md" ]
then
  echo "Creating README.md for directory"
  touch README.md
  printf "# Set-Commands Loadable Configuration\n\n" >> README.md
  printf "The set commands loadable config files created within this directory\n" >> README.md
  printf "are initialized with both static and dhcp options by default. It is up to the\n" >> README.md
  printf "user's discretion on which configuration they would like to use." >> README.md
else
  echo "README.md file already exists, moving forward"
fi
cd ..

# Below block of commands rolls up all skillets from the playlists directories
echo "Rollup all skillets in the playlists/panos/ directory"
sli -sd ../../ rollup_playlist -n ironskillet_panos_11_0 ../templates/panos/snippets/.meta-cnc.yaml

# swap out skillet preamble text after rollup
# temp fix until features added to SLI for value options
cd ../templates/panos/snippets
sed -i '' 's/ironskillet_panos_11_0_rollup/skillet_panos_v11_0/' .meta-cnc.yaml
sed -i '' 's/PAN-OS NGFW IronSkillet 11.0/v11.0 Iron-Skillet for NGFW/' .meta-cnc.yaml
sed -i '' 's/IronSkillet Playlists/IronSkillet/' .meta-cnc.yaml
cd ../../../tools

echo "Rollup all skillets in the playlists/panorama/ directory"
sli -sd ../../ rollup_playlist -n ironskillet_panorama_notshared_dgstack_all_11_0 ../templates/panorama/snippets_dgstack_notshared/.meta-cnc.yaml
sli -sd ../../ rollup_playlist -n ironskillet_panorama_notshared_11_0 ../templates/panorama/snippets_notshared/.meta-cnc.yaml
sli -sd ../../ rollup_playlist -n ironskillet_panorama_shared_dgtemplate_11_0 ../templates/panorama/snippets_dgtemplate_shared/.meta-cnc.yaml
sli -sd ../../ rollup_playlist -n ironskillet_panorama_shared_11_0 ../templates/panorama/snippets/.meta-cnc.yaml

# swap out skillet preamble text after rollup
# temp fix until features added to SLI for value options
# shared snippets
cd ../templates/panorama/snippets
sed -i '' 's/ironskillet_panorama_shared_11_0_rollup/skillet_panorama_v11_0/' .meta-cnc.yaml
sed -i '' 's/Panorama Shared IronSkillet 11.0/v11.0 Iron-Skillet for Panorama (Shared Values)/' .meta-cnc.yaml
sed -i '' 's/IronSkillet Playlists/IronSkillet/' .meta-cnc.yaml
# dgstack_notshared
cd ../snippets_dgstack_notshared
sed -i '' 's/ironskillet_panorama_notshared_dgstack_all_11_0_rollup/skillet_panorama_dgstack_notshared_v11_0/' .meta-cnc.yaml
sed -i '' 's/Panorama Notshared DGTemplate IronSkillet 11.0/v11.0 Iron-Skillet for Panorama with Device-Group and Stack only (No Shared Values)/' .meta-cnc.yaml
sed -i '' 's/IronSkillet Playlists/IronSkillet/' .meta-cnc.yaml
# dgtemplate_shared
cd ../snippets_dgtemplate_shared
sed -i '' 's/ironskillet_panorama_shared_dgtemplate_11_0_rollup/skillet_panorama_dgtemplate_shared_v11_0/' .meta-cnc.yaml
sed -i '' 's/Panorama Shared IronSkillet 11.0/v11.0 Iron-Skillet for Panorama with Device-Group and Template only (no Panorama system config)/' .meta-cnc.yaml
sed -i '' 's/IronSkillet Playlists/IronSkillet/' .meta-cnc.yaml
# snippets_notshared
cd ../snippets_notshared
sed -i '' 's/ironskillet_panorama_notshared_11_0_rollup/skillet_panorama_notshared_v11_0/' .meta-cnc.yaml
sed -i '' 's/Panorama Notshared IronSkillet 11.0/v11.0 Iron-Skillet for Panorama (No Shared Values)/' .meta-cnc.yaml
sed -i '' 's/IronSkillet Playlists/IronSkillet/' .meta-cnc.yaml
cd ../../../tools



# Below block of commands creates the full template configurations for Panos
# This template is an XML version of the panos_full.skillet.yaml in the playlists/panos directory
# but leaves Jinja unrendered and results are outputted in templates/panos/full/ directory.
echo "Creating a full XML Jinja Template configuration for Panos"
cd ..
sli create_template $CONFIG_ALL_PANOS -n ironskillet_panos_11_0 templates/panos/baseline/baseline.xml templates/panos/full/iron_skillet_panos_full.xml
cd tools

echo "Creating a full XML Jinja Template configuration for Panorama"
cd ..
sli create_template $CONFIG_ALL_PANORAMA -n ironskillet_panorama_shared_11_0 templates/panorama/baseline/baseline.xml templates/panorama/full/iron_skillet_panorama_full.xml
cd tools


# Create all loadable config XML and set command files with rendered jinja for panos and
# Panorama Using full panos file from playlists/panos/panos_full outputting in respective
# Loadable config folders
echo "using sli template to create the loadable config xml with rendered jinja for panos"
sli template -sd ../ -ad -n skillet_full_panos_v11_0 -o ../loadable_configs/sample-cloud-AWS/panos/iron_skillet_panos_full.xml
sli template -sd ../ -ad -n skillet_full_panos_v11_0 -o ../loadable_configs/sample-cloud-Azure/panos/iron_skillet_panos_full.xml
sli template -sd ../ -ad -n skillet_full_panos_v11_0 -o ../loadable_configs/sample-cloud-GCP/panos/iron_skillet_panos_full.xml
sli template -sd ../ -ad -n skillet_full_panos_v11_0 -o ../loadable_configs/sample-mgmt-dhcp/panos/iron_skillet_panos_full.xml
sli template -sd ../ -ad $MGMT_STATIC -n skillet_full_panos_v11_0 -o ../loadable_configs/sample-mgmt-static/panos/iron_skillet_panos_full.xml

echo "Using sli template to create the loadable config set commands with rendered jinja for panos"
sli template -sd ../ -ad -n skillet_set_command_panos_v11_0 -o ../loadable_configs/sample-set-commands/panos/iron_skillet_panos_full.conf

echo "using sli template to create the loadable config xml with rendered jinja for panorama"
sli template -sd ../ -ad $PANORAMA_CLD -n skillet_full_panorama_v11_0 -o ../loadable_configs/sample-cloud-AWS/panorama/iron_skillet_panorama_full.xml
sli template -sd ../ -ad $PANORAMA_CLD -n skillet_full_panorama_v11_0 -o ../loadable_configs/sample-cloud-Azure/panorama/iron_skillet_panorama_full.xml
sli template -sd ../ -ad $PANORAMA_CLD -n skillet_full_panorama_v11_0 -o ../loadable_configs/sample-cloud-GCP/panorama/iron_skillet_panorama_full.xml
sli template -sd ../ -ad -n skillet_full_panorama_v11_0 -o ../loadable_configs/sample-mgmt-dhcp/panorama/iron_skillet_panorama_full.xml
sli template -sd ../ -ad $MGMT_STATIC -n skillet_full_panorama_v11_0 -o ../loadable_configs/sample-mgmt-static/panorama/iron_skillet_panorama_full.xml

echo "Using sli template to create the loadable config set commands with rendered jinja for panorama"
sli template -sd ../ -ad -n skillet_setcommand_panorama_v11_0 -o ../loadable_configs/sample-set-commands/panorama/iron_skillet_panorama_full.conf


# Below block of commands creates the spreadsheet files for both Panorama and Panos set commands
echo "Creating Panos spreadsheet to be output in /templates/panos/set_commands/"
sli spreadsheet -sd ../templates/panos/set_commands -n skillet_set_command_panos_v11_0 -o ../templates/panos/set_commands/
echo "Creating Panorama spreadsheet to be output in /templates/panorama/set_commands/"
sli spreadsheet -sd ../templates/panorama/set_commands -n skillet_setcommand_panorama_v11_0 -o ../templates/panorama/set_commands/
