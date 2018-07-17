
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

.. Note::
You can perform a ``Save named configuration snapshot`` as backup prior to loading the new configuration


4. Then ``Import named configuration snapshot`` choosing the day one config xml file


Load and commit the configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Still under the ``Operations`` tab, use ``Load named configuration snapshot`` choosing the day one config xml file

2. Ensure no errors loading the configuration.

3. Once loaded use the GUI to verify the configuration elements have been loaded then ``commit``


.. Note::
As referenced above, you may see {{ text }} related errors during the commit.
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

.. Note::
You can perform a ``Save named configuration snapshot`` as backup prior to loading the new configuration


4. Then ``Import named configuration snapshot`` choosing the day one config xml file


Load the configuration elements: CLI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Log into the PAN-OS command line interface

2. Enter ``configure`` to go into configuration mode

3. Paste in each of the ``load config partial`` commands, in order

4. Once complete use the GUI to verify the configuration elements have been loaded then ``commit``


Load config partial commands
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cut-and-paste from the table below into the PAN-OS command line while in configuration mode.

You can paste multiple items. The system will pause during each load config partial, return a status message, then move to the next load. When complete, ensure the final load is entered and a status message received.

::

    load config partial from panos_day_one_1.0.0.xml from-xpath /config/shared/log-settings to-xpath /config/shared/log-settings mode merge
    load config partial from panos_day_one_1.0.0.xml from-xpath /config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/tag to-xpath /config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/tag mode merge
    load config partial from panos_day_one_1.0.0.xml from-xpath /config/devices/entry[@name='localhost.localdomain']/deviceconfig/system to-xpath /config/devices/entry[@name='localhost.localdomain']/deviceconfig/system mode merge
    load config partial from panos_day_one_1.0.0.xml from-xpath /config/devices/entry[@name='localhost.localdomain']/deviceconfig/setting to-xpath /config/devices/entry[@name='localhost.localdomain']/deviceconfig/setting mode merge
    load config partial from panos_day_one_1.0.0.xml from-xpath /config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/address to-xpath /config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/address mode merge
    load config partial from panos_day_one_1.0.0.xml from-xpath /config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/external-list to-xpath /config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/external-list mode merge
    load config partial from panos_day_one_1.0.0.xml from-xpath /config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/profiles to-xpath /config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/profiles mode merge
    load config partial from panos_day_one_1.0.0.xml from-xpath /config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/profile-group to-xpath /config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/profile-group mode merge
    load config partial from panos_day_one_1.0.0.xml from-xpath /config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/rulebase to-xpath /config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/rulebase mode merge
    load config partial from panos_day_one_1.0.0.xml from-xpath /config/devices/entry[@name='localhost.localdomain']/network/profiles/zone-protection-profile to-xpath /config/devices/entry[@name='localhost.localdomain']/network/profiles/zone-protection-profile mode merge
    load config partial from panos_day_one_1.0.0.xml from-xpath /config/shared/reports to-xpath /config/shared/reports mode merge
    load config partial from panos_day_one_1.0.0.xml from-xpath /config/shared/report-group to-xpath /config/shared/report-group mode merge
    load config partial from panos_day_one_1.0.0.xml from-xpath /config/shared/email-scheduler to-xpath /config/shared/email-scheduler mode merge

Configuration Elements Load Order Explained
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Each xpath in the load config partial gives an indication of each element loaded. Below is a simple explanation of the configuration elements with key items in the xml load.

================  =============================================
xpath             suffix description
================  =============================================
log               |settings syslog/email profiles and system, configuration logging
tag               referenced tags used in security rules
system            dynamic updates, dns and ntp server settings
setting           Wildfire max file sizes, disable log suppression
address           named references for sinkholes values used in security rules
external list     EDLs referenced in security rules, eg. IPv4/v6 bogons
profiles          Threat, URL Filtering, Wildfire, and decryption profile configurations
profile-group     Group settings for the security profiles, eg. Inbound, Outbound, Alert-All
rulebase          template security and decryption rules
zone protection   recommended zone protection profile
reports           traffic and threat reports
report groups     grouping of reports for viewing and scheduling
email scheduler   email schedule for report groups
================  =========================================
