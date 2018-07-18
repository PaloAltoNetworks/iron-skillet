
Loading templates
=================


The template are xml file format that have to loaded into the device as a full config or with modular partial loading.


Load full configuration file
----------------------------

Similar to a device bootstrap, a full xml can be loaded into the system as a candidate configuration. This provides the simplicity of loading a new configuration but will replace any configuration currently in the device.

In comparison, a load config partial requires additional steps but merges into the existing configuration instead of replacing.

The steps below can be used for a full configuration load and replace.


Edit the full xml configuration file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Since this will replace the existing configuration, the user is required to modify the xml file with admin accounts, management IP, and other initial configuration values.

The template uses ``{{ text }}`` markers in the config file to denote values that MUST be changed.
During a commit, the device will show an error with the ``{{ text }}`` values in the error message.

Import the configuration file using the GUI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Log into the firewall and click on the ``Device`` tab

2. Select ``Setup`` in the left nav bar

3. Click on the ``Operations`` tab

4. Then ``Import named configuration snapshot`` choosing the day one config xml file


.. Note::
    You can perform a ``Save named configuration snapshot`` as backup prior to loading the new configuration


Load and commit the configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Still under the ``Operations`` tab, use ``Load named configuration snapshot`` choosing the day one config xml file

2. Ensure no errors loading the configuration.

3. Once loaded use the GUI to verify the configuration elements have been loaded then ``commit``


.. Note::
    As referenced above, you may see ``{{ text }}`` related errors during the commit.
    If this happens, you will need to edit the pre-imported xml file and then repeat the steps above to import, load, and commit the configuration.



Using load config partial
-------------------------

The configuration file uses the xml format. Therefore each configuration element sits in the xml tree and is referenced by its ``xpath``.

Using this concept, a template configuration file can be imported into Panorama or the firewall with only the referenced elements merged into the existing configuration. This is more modular than loading a full configuration file that replaces the existing configuration.

The syntax used for loading the templates is:


 load config partial from ``{{filename}}`` from-xpath ``{{xpath}}`` to-xpath ``{{xpath}}`` mode merge


where:

 ``{{filename}}`` is the xml file loaded into the device

 ``{{xpath}}`` denotes what part of the configuration is being merged from the day one file to the candidate configuration.


Edit the configuration xml file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Load config partial will merge the configuration elements.
However, there are parts of the configuration such as the management configuration interface that will be specific to each device.

The template uses ``{{ text }}`` markers in the config file to denote values that MUST be changed.
During a commit, the device will show an error with the ``{{ text }}`` values in the error message.

It is recommended that the configuration elements with the ``{{ text }}`` areas be modified to match the desired device settings or are removed from the configuration file before importing.

Import the Day One configuration: GUI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Log into the firewall and click on the ``Device`` tab

2. Select ``Setup`` in the left nav bar

3. Click on the ``Operations`` tab

4. Then ``Import named configuration snapshot`` choosing the day one config xml file


.. Note::
    You can perform a ``Save named configuration snapshot`` as backup prior to loading the new configuration


Load the configuration elements: CLI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Log into the PAN-OS command line interface

2. Enter ``configure`` to go into configuration mode

3. Paste in each of the ``load config partial`` commands, in order

4. Once complete use the GUI to verify the configuration elements have been loaded then ``commit``


PAN-OS load config partial commands
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cut-and-paste from the table below into the PAN-OS command line while in configuration mode.


You can paste multiple items. The system will pause during each load config partial, return a status message, then move to the next load. When complete, ensure the final load is entered and a status message received.

.. parsed-literal::

    load config partial from |panosconfigfile| from-xpath /config/shared/log-settings to-xpath /config/shared/log-settings mode merge
    load config partial from |panosconfigfile| from-xpath /config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/tag to-xpath /config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/tag mode merge
    load config partial from |panosconfigfile| from-xpath /config/devices/entry[@name='localhost.localdomain']/deviceconfig/system to-xpath /config/devices/entry[@name='localhost.localdomain']/deviceconfig/system mode merge
    load config partial from |panosconfigfile| from-xpath /config/devices/entry[@name='localhost.localdomain']/deviceconfig/setting to-xpath /config/devices/entry[@name='localhost.localdomain']/deviceconfig/setting mode merge
    load config partial from |panosconfigfile| from-xpath /config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/address to-xpath /config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/address mode merge
    load config partial from |panosconfigfile| from-xpath /config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/external-list to-xpath /config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/external-list mode merge
    load config partial from |panosconfigfile| from-xpath /config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/profiles to-xpath /config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/profiles mode merge
    load config partial from |panosconfigfile| from-xpath /config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/profile-group to-xpath /config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/profile-group mode merge
    load config partial from |panosconfigfile| from-xpath /config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/rulebase to-xpath /config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/rulebase mode merge
    load config partial from |panosconfigfile| from-xpath /config/devices/entry[@name='localhost.localdomain']/network/profiles/zone-protection-profile to-xpath /config/devices/entry[@name='localhost.localdomain']/network/profiles/zone-protection-profile mode merge
    load config partial from |panosconfigfile| from-xpath /config/shared/reports to-xpath /config/shared/reports mode merge
    load config partial from |panosconfigfile| from-xpath /config/shared/report-group to-xpath /config/shared/report-group mode merge
    load config partial from |panosconfigfile| from-xpath /config/shared/email-scheduler to-xpath /config/shared/email-scheduler mode merge


PAN-OS config elements used in load config partial
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Each xpath in the load config partial gives an indication of each element loaded. Below is a simple explanation of the configuration elements with key items in the xml load.

================   ==========================================================================
xpath              suffix description
================   ==========================================================================
log settings       settings syslog/email profiles and system, configuration logging
tag                referenced tags used in security rules
system             dynamic updates, dns and ntp server settings
setting            Wildfire max file sizes, disable log suppression
address            named references for sinkholes values used in security rules
external list      EDLs referenced in security rules, eg. IPv4/v6 bogons
profiles           Threat, URL Filtering, Wildfire, and decryption profile configurations
profile-group      Group settings for the security profiles, eg. Inbound, Outbound, Alert-All
rulebase           template security and decryption rules
zone protection    recommended zone protection profile
reports            traffic and threat reports
report groups      grouping of reports for viewing and scheduling
email scheduler    email schedule for report groups
================   ==========================================================================


Panorama load config partial commands
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cut-and-paste from the table below into the PAN-OS command line while in configuration mode.

You can paste multiple items. The system will pause during each load config partial, return a status message, then move to the next load. When complete, ensure the final load is entered and a status message received.

::

    load config partial from panorama_day_one_1.0.0.xml from-xpath /config/devices/entry[@name='localhost.localdomain']/deviceconfig/system to-xpath /config/devices/entry[@name='localhost.localdomain']/deviceconfig/system mode merge
    load config partial from panorama_day_one_1.0.0.xml from-xpath /config/devices/entry[@name='localhost.localdomain']/deviceconfig/setting to-xpath /config/devices/entry[@name='localhost.localdomain']/deviceconfig/setting mode merge
    load config partial from panorama_day_one_1.0.0.xml from-xpath /config/panorama/log-settings to-xpath /config/panorama/log-settings mode merge
    load config partial from panorama_day_one_1.0.0.xml from-xpath /config/devices/entry[@name='localhost.localdomain']/template to-xpath /config/devices/entry[@name='localhost.localdomain']/template mode merge
    load config partial from panorama_day_one_1.0.0.xml from-xpath /config/devices/entry[@name='localhost.localdomain']/device-group to-xpath /config/devices/entry[@name='localhost.localdomain']/device-group mode merge
    load config partial from panorama_day_one_1.0.0.xml from-xpath /config/shared to-xpath /config/shared mode merge
    load config partial from panorama_day_one_1.0.0.xml from-xpath /config/devices/entry[@name='localhost.localdomain']/log-collector-group to-xpath /config/devices/entry[@name='localhost.localdomain']/log-collector-group mode merge



Panorama config elements used in load config partial
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Each xpath in the load config partial gives an indication of each element loaded. Below is a simple explanation of the configuration elements with key items in the xml load.

This uses an aggregate template loading module with multiple configuration elements contained under the template, device-group, and shared parts of the xml tree. The hierarchical nature of Panorama simplifies the configuration loading.

======================  ==========================================================================
xpath                   suffix description
======================  ==========================================================================
panorama system         panorama specific dynamic updates, dns and ntp server settings
panorama settings       enable reporting on groups and sharing of unused objects
panorama log settings   syslog/email profiles and system, configuration logging
template                test template configuration with device settings and zone profile
device-group            reports, report groups, and email scheduler
shared                  profile object, rules, and other device-group 'top of tree' items
log collector           settings for Panorama when used as a log collector
======================  ==========================================================================

______________________________________________________________________

Loading configuration snippets with pan-python
----------------------------------------------

pan-python overview
~~~~~~~~~~~~~~~~~~~

Pan-python provides a simple command-line model to use the Panorama/PAN-OS API. It leverages the standard xml xpath+element model to push configuration changes to the device. The GitHub repo is found here:

`pan-python repo
<https://github.com/kevinsteves/pan-python>`_


Training for pan-python including the initial install and getting the device api-key are found here:


`pan-python api lab
<http://api-lab.paloaltonetworks.com>`_


Before using pan-python, it helps to be familiar with the xpaths used in the template along with the configuration load order. These provide the foundation for the xpath and element references in the examples below.


`xpath and snippet load order
<https://github.com/PaloAltoNetworks/iron-skillet/wiki/Panorama-PAN-OS-API-Overview>`_


pan-python full syntax for loading a config element
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The standard entry model is
::

    panxapi.py -h ``{{ ip address }}`` -K ``{{ api-key }}`` -S ``{{ filename.xml }}`` "``{{ xpath }}``"


where the elements are:
::

    {{ ip address }} is the device ip address
    {{ api-key }} is the user/device specific api-key
    {{ filename }} is the xml snippet to be loaded
    {{ xpath }} is the xpath specific to the config element


For example, to load the tag.xml file to ip address 192.168.55.10 and api-key: 12345 would be
::
    panxapi.py -h 192.168.55.10 -K 12345 -S tag.xml "/config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/tag"


or an external list object (aka EDL)
::
    panxapi.py -h 192.168.55.10 -K 12345 -S external_list.xml "/config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/external-list"



Simple scripts can be used to iterate through multiple load requests.


.. Note::
   Based on the local pan-python install and use of .panrc you may not require the -h and -K elements and only have to reference the xpath and filename.


_________________________________________________

The Panorama/PAN-OS API and XML
-------------------------------

API Overview
~~~~~~~~~~~~

For extended reading about the API, you can access the documentation for 8.1 here:

`PAN-OS API Reference
<https://www.paloaltonetworks.com/documentation/81/pan-os/xml-api>`_


The configuration file and api calls are XML specific. XML is based on XML nodes with the xpath specifying the node in the tree to be referenced. Thus in order to use the API, two configuration items are needed:

1. The xpath pointing to the node to be configured
2. The xml snippet to be used as the element in the configuration

Along with these two items, the IP address of the device and a user-based API are required to modify the configuration.


Reference values contained in the repo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


``xpaths list``: a python dictionary that can be used within scripts. The key is the reference name for the xpath and the value is the xpath name. The key and value will be referenced in the table below to show load order.

``config snippets folder``: set of xml files named according to config element; referenced as the value in the snippet load order dictionary

``snippet load order``: A python Ordered Dictionary used to show the config load order. The key is the xpath name from the xpaths list and the value is the config snippet file name. Load order is critical since some configuration elements like security rules rely on predefined objects such as EDLs, logging profiles, and security profiles.

With the xpath, snippet, and load order various tools such as pan-python, curl, and postman can be used to add configuration using the API. Other tools such as Ansible and Terraform use the same concept but have their own template format to create playbooks and responders.



Panorama items


    `xpaths
    <https://github.com/PaloAltoNetworks/iron-skillet/blob/master/docs/panorama_xpaths_list.py>`_

    `snippets
    <https://github.com/PaloAltoNetworks/iron-skillet/tree/master/Panorama_version-08.0/xml-config-snippets>`_

    `load order
    <https://github.com/PaloAltoNetworks/iron-skillet/blob/master/docs/panorama_snippet_load_order.py>`_



PAN-OS items


    `xpaths
    <https://github.com/PaloAltoNetworks/iron-skillet/blob/master/docs/panorama_xpaths_list.py>`_

    `snippets
    <https://github.com/PaloAltoNetworks/iron-skillet/tree/master/PANOS_version-08.0/xml-config-snippets>`_

    `load order
    <https://github.com/PaloAltoNetworks/iron-skillet/blob/master/docs/panorama_snippet_load_order.py>`_




With the xpath, snippet, and load order various tools such as pan-python, curl, and postman can be used to add configuration using the API. Other tools such as Ansible and Terraform use the same concept but have their own template format to create playbooks and responders.
