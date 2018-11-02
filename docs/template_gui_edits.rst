
Template Edits with GUI or Console
==================================


The templates are xml file format that have to be loaded into the device as a full config or with modular partial loading.

Base templates use a jinja variable format allowing for simple scripts to modify per-deployment values. A list of the
variables can be found in the section, Creating Loadable Configurations.

Instead of using scripting tools, the instructions below allow a user to ``Import`` and ``Load`` a candidate configuration
that can be manually edited with the GUI or a small number of ``set`` console commands.

.. Note::
    Sample configuration files are in the my_config directory. Samples include a static management interface,
    basic dhcp-client management interface, and additional dhcp-client options for cloud deployments.


Load a candidate configuration file
-----------------------------------

----------------------------------------------------------------------

The starter steps below step through import and load of a full configuration file.


Import the configuration file using the GUI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Click on the ``Device`` tab

2. Select ``Setup`` in the left nav bar

3. Click on the ``Operations`` tab

4. Then ``Import named configuration snapshot`` choosing the day one config xml file


.. Note::
    You should perform a ``Save named configuration snapshot`` as backup prior to loading the new configuration


Load the configuration
~~~~~~~~~~~~~~~~~~~~~~

1. Still under the ``Operations`` tab, use ``Load named configuration snapshot`` choosing the day one config xml file

2. Ensure no errors loading the configuration.

.. image:: images/import_load.png
   :width: 400


.. Note::
    If you see {{ text }} related import or load errors ensure you have the template file imported from the my_config
    directory and not the template directory.

----------------------------------------------------------------------

GUI variable edits: Firewall
----------------------------


The steps below are for a stand-alone NGFW platform without Panorama.


Device tab edits
~~~~~~~~~~~~~~~~

----------------------------------------------------------------------

The following edits are found under the ``Device`` tab

.. image:: images/device_tab.png
   :width: 600


From here the following edits can be made:


Hostname
~~~~~~~~

1. Go to Device --> Setup --> Management

2. Click the ``gear`` icon to edit the hostname

.. image:: images/setup_management.png
   :width: 600


DNS and NTP servers
~~~~~~~~~~~~~~~~~~~

1. Go to Device --> Setup --> Services

2. Click the ``gear`` icon to edit the server values

3. Choose the Services (DNS) and NTP tabs accordingly

.. image:: images/setup_services.png
   :width: 600


Static Management Interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~

For a static management interface configuration, edit the IP address, subnet mask, default gateway.

1. Go to Device --> Setup --> Interfaces

2. Click on the ``Management`` link

3. Edit the management interface attributes

.. image:: images/setup_interfaces.png
   :width: 600


Superuser Administrator
~~~~~~~~~~~~~~~~~~~~~~~

The sample configuration uses the default admin/admin username and password setting. It is recommended to remove this
user and add a new superuser or at a minimum change the admin user password.

1. Go to Device --> Administrators

2. Select and delete the ``admin`` user account

3. Choose to ``Add`` a new user entering the username and password in the pop-up window

.. image:: images/device_administrators.png
   :width: 400


Syslog IP Address
~~~~~~~~~~~~~~~~~

Syslog is used to send traffic, threat and other log updates to an external system.

1. Go to Device --> Server Profiles --> Syslog

2. Click on the Sample_Syslog_Profile link and edit the IP address

.. image:: images/device_syslog.png
   :width: 600


Email Server Profile
~~~~~~~~~~~~~~~~~~~~

The email profile is used to send key alerts to select recipients.

1. Go to Device --> Server Profiles --> Email

2. Click on the Sample_Email_Profile link and edit the from, to, and gateway values in the pop-up window.

.. image:: images/device_email.png
   :width: 600


Object tab edits
~~~~~~~~~~~~~~~~

----------------------------------------------------------------------

The following edits are found under the ``Objects`` tab

.. image:: images/objects_tab.png
   :width: 600


From here the following edits can be made:


Addresses
~~~~~~~~~

The template uses two address objects for sinkhole values, one each for IPv4 and IPv6. These are referenced in
security rules.

1. Go to Objects --> Address

2. Click on the Sinkhole IPv4 and IPv6 links and edit the IP address

.. image:: images/objects_addresses.png
   :width: 600


Anti-Spyware Security Profiles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The templates define multiple named Anti-Spyware profiles all appended with ``-AS``. Each of these profiles must be
updated with new sinkhole address if non-default values are required.

These values should match the sinkhole IP addresses configured under ``Addresses``.

1. Go to Objects --> Security Profiles --> Anti-Spyware

.. image:: images/objects_spyware.png
   :width: 800

2. Click on one of the template specific profiles ending in ``-AS``

3. Click on the DNS Signatures tab and update the IPv4 and IPv6 sinkhole addresses

.. image:: images/spyware_sinkholes.png
   :width: 400

----------------------------------------------------------------------

GUI variable edits: Panorama
----------------------------


The steps below are for edits to the Panorama configuration. Variable edits in the GUI will include both the Panorama
system edits and managed firewall device-group and template configurations.


Panorama tab edits
~~~~~~~~~~~~~~~~~~

----------------------------------------------------------------------

The following edits are found under the ``Panorama`` tab

.. image:: images/panorama_tab.png
   :width: 600


From here the following edits can be made:


Panorama > Hostname
~~~~~~~~~~~~~~~~~~~

1. Go to Panorama --> Setup --> Management

2. Click the ``gear`` icon to edit the Panorama hostname

.. image:: images/setup_management.png
   :width: 600


Panorama > DNS and NTP servers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Go to Panorama --> Setup --> Services

2. Click the ``gear`` icon to edit the server values

3. Choose the Services (DNS) and NTP tabs accordingly

.. image:: images/setup_services.png
   :width: 600


Panorama > Management Interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This configuration is specific to the Panorama management interface when statically defined.

1. Go to Panorama --> Setup --> Interfaces

2. Click on the ``Management`` link

3. Edit the management interface attributes

.. image:: images/panorama_management.png
   :width: 600


Panorama > Superuser Administrator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The sample configuration uses the default admin/admin username and password setting. It is recommended to remove this
user and add a new superuser or at a minimum change the admin user password.

1. Go to Panorama --> Administrators

2. Select and delete the ``admin`` user account

3. Choose to ``Add`` a new user entering the username and password in the pop-up window

.. image:: images/device_administrators.png
   :width: 400


Panorama > Syslog IP Address
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Syslog is used to send traffic, threat and other log updates to an external system.

1. Go to Panorama --> Server Profiles --> Syslog

2. Click on the Sample_Syslog_Profile link and edit the IP address

.. image:: images/device_syslog.png
   :width: 600


Panorama > Email Server Profile
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The email profile is used to send key alerts to select recipients.

1. Go to Panorama --> Server Profiles --> Email

2. Click on the Sample_Email_Profile link and edit the from, to, and gateway values in the pop-up window.

.. image:: images/device_email.png
   :width: 600


Panorama > Config Bundle Export Server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Go to Panorama --> Scheduled Config Export

2. Click on the Recommended_Config_Export link

3. In the pop-up window, edit the Hostname value

.. image:: images/panorama_config_export.png
   :width: 600


Panorama Template
~~~~~~~~~~~~~~~~~

1. Go to Panorama --> Template

2. Click on the ``sample`` link and edit the name

.. image:: images/panorama_templates.png
   :width: 600


Panorama Device-Group
~~~~~~~~~~~~~~~~~~~~~

1. Go to Panorama --> Device-Groups

2. Click on the ``sample`` link and edit the name

.. image:: images/panorama_devicegroup.png
   :width: 400


Templates > Device tab edits
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

----------------------------------------------------------------------

The following edits are found under the ``Device`` tab

.. image:: images/templates_device_tab.png
   :width: 600


From here the following edits can be made:


Hostname
~~~~~~~~

1. Go to Device --> Setup --> Management

2. Click the ``gear`` icon to edit the hostname

.. image:: images/setup_management.png
   :width: 600


DNS and NTP servers
~~~~~~~~~~~~~~~~~~~

1. Go to Device --> Setup --> Services

2. Click the ``gear`` icon to edit the server values

3. Choose the Services (DNS) and NTP tabs accordingly

.. image:: images/setup_services.png
   :width: 600


Static Management Interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~

For a static management interface configuration, edit the IP address, subnet mask, default gateway.

1. Go to Device --> Setup --> Interfaces

2. Click on the ``Management`` link

3. Edit the management interface attributes

.. image:: images/setup_interfaces.png
   :width: 600


Superuser Administrator
~~~~~~~~~~~~~~~~~~~~~~~

The sample configuration uses the default admin/admin username and password setting. It is recommended to remove this
user and add a new superuser or at a minimum change the admin user password.

1. Go to Device --> Administrators

2. Select and delete the ``admin`` user account

3. Choose to ``Add`` a new user entering the username and password in the pop-up window

.. image:: images/device_administrators.png
   :width: 400


Syslog IP Address
~~~~~~~~~~~~~~~~~

Syslog is used to send traffic, threat and other log updates to an external system.

1. Go to Device --> Server Profiles --> Syslog

2. Click on the Sample_Syslog_Profile link and edit the IP address

.. image:: images/device_syslog.png
   :width: 600


Email Server Profile
~~~~~~~~~~~~~~~~~~~~

The email profile is used to send key alerts to select recipients.

1. Go to Device --> Server Profiles --> Email

2. Click on the Sample_Email_Profile link and edit the from, to, and gateway values in the pop-up window.

.. image:: images/device_email.png
   :width: 600


Device-Group > Objects tab edits
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

----------------------------------------------------------------------

The following edits are found under the ``Objects`` tab

.. image:: images/objects_tab.png
   :width: 600


From here the following edits can be made:


Addresses
~~~~~~~~~

The template uses two address objects for sinkhole values, one each for IPv4 and IPv6. These are referenced in
security rules.

1. Go to Objects --> Address

2. Click on the Sinkhole IPv4 and IPv6 links and edit the IP address

.. image:: images/objects_addresses.png
   :width: 600


Anti-Spyware Security Profiles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The templates define multiple named Anti-Spyware profiles all appended with ``-AS``. Each of these profiles must be
updated with new sinkhole address if non-default values are required.

These values should match the sinkhole IP addresses configured under ``Addresses``.

1. Go to Objects --> Security Profiles --> Anti-Spyware

.. image:: images/objects_spyware.png
   :width: 800

2. Click on one of the template specific profiles ending in ``-AS``

3. Click on the DNS Signatures tab and update the IPv4 and IPv6 sinkhole addresses

.. image:: images/spyware_sinkholes.png
   :width: 400

------------------------------------------------------------------------------------

Console variable edits: Firewall
--------------------------------

This section is specific to a non-Panorama managed NGFW.

Instead of using the GUI to make template edits for each variable value, below are steps using SET commands to make
the same candidate configuration changes.

The {{ text }} values denotes where a variable is used in the template.


Hostname
~~~~~~~~

::

   set deviceconfig system hostname {{ hostname }}


DNS and NTP Servers
~~~~~~~~~~~~~~~~~~~

::

   set deviceconfig system dns-setting servers primary {{ DNS 1 }} secondary {{ DNS 2 }}
   set deviceconfig system ntp-servers primary-ntp-server ntp-server-address {{ NTP 1 }}
   set deviceconfig system ntp-servers secondary-ntp-server ntp-server-address {{ NTP 2 }}


Static management interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   set deviceconfig system ip-address {{ ip address }} netmask {{ mask }} default-gateway {{ gateway }}


Superuser admin account
~~~~~~~~~~~~~~~~~~~~~~~

::

   set mgt-config users {{ username }} permissions role-based superuser yes
   set mgt-config users {{ username }} password

When the password command is entered, the user will be prompted for a password.


Syslog and Email Server Profiles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   set shared log-settings syslog Sample_Syslog_Profile server Sample_Syslog server {{ ip address }}
   set shared log-settings email Sample_Email_Profile server Sample_Email_Profile from {{ from }}
   set shared log-settings email Sample_Email_Profile server Sample_Email_Profile to {{ to }}
   set shared log-settings email Sample_Email_Profile server Sample_Email_Profile gateway {{ address }}

Address Objects
~~~~~~~~~~~~~~~

::

   set address Sinkhole-IPv4 ip-netmask {{ IPv4 address }}
   set address Sinkhole-IPv6 ip-netmask {{ IPv6 address }}

Anti-Spyware Security Profiles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The same commands are used across all of the template security profiles ending in ``-AS``.

::

   set profiles spyware {{ profile name }} botnet-domains sinkhole ipv4-address {{ IPv4 address }}
   set profiles spyware {{ profile name }} botnet-domains sinkhole ipv6-address {{ IPv6 address }}

----------------------------------------------------------------------------------------------

Console variable edits: Panorama
--------------------------------

This section is specific to configuration of a Panorama management system.

Instead of using the GUI to make template edits for each variable value, below are steps using SET commands to make
the same candidate configuration changes.

The {{ text }} values denotes where a variable is used in the template.

.. Note::
   The initial configurations are specific to the Panorama platform itself. The managed firewall configurations
   are added under the template and device-group configurations.


Panorama > Hostname
~~~~~~~~~~~~~~~~~~~

::

   set deviceconfig system hostname {{ hostname }}


Panorama > DNS and NTP Servers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   set deviceconfig system dns-setting servers primary {{ DNS 1 }} secondary {{ DNS 2 }}
   set deviceconfig system ntp-servers primary-ntp-server ntp-server-address {{ NTP 1 }}
   set deviceconfig system ntp-servers secondary-ntp-server ntp-server-address {{ NTP 2 }}


Panorama > Static management interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   set deviceconfig system ip-address {{ ip address }} netmask {{ mask }} default-gateway {{ gateway }}


Panorama > Superuser admin account
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   set mgt-config users {{ username }} permissions role-based superuser yes
   set mgt-config users {{ username }} password

When the password command is entered, the user will be prompted for a password.


Panorama > Syslog and Email Server Profiles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   set panorama log-settings syslog Sample_Syslog_Profile server Sample_Syslog server {{ ip address }}
   set panorama log-settings email Sample_Email_Profile server Sample_Email_Profile from {{ from }}
   set panorama log-settings email Sample_Email_Profile server Sample_Email_Profile to {{ to }}
   set panorama log-settings email Sample_Email_Profile server Sample_Email_Profile gateway {{ address }}

Panorama > Config Bundle Export Schedule
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   set deviceconfig system config-bundle-export-schedule Recommended_Config_Export protocol scp hostname {{ ip address }}

------------------------------------------------------------------------------------------------------------------

.. Note::
   The configurations below are specific to the template and device-groups for managed firewall configuration.
   The template and device-group names are default to ``sample`` for Iron-Skillet


Template > Hostname
~~~~~~~~~~~~~~~~~~~

::

   set template sample config deviceconfig system hostname {{ hostname }}


Template > DNS and NTP Servers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   set template sample config deviceconfig system dns-setting servers primary {{ DNS 1 }} secondary {{ DNS 2 }}
   set template sample config deviceconfig system ntp-servers primary-ntp-server ntp-server-address {{ NTP 1 }}
   set template sample config deviceconfig system ntp-servers secondary-ntp-server ntp-server-address {{ NTP 2 }}


Template > Static management interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is to be configured for a firewall with a static management interface.

::

   set template sample config deviceconfig system ip-address {{ ip address }}
   set template sample config deviceconfig system netmask {{ mask }}
   set template sample config deviceconfig system default-gateway {{ gateway }}


Template > Superuser admin account
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   set template sample config mgt-config users {{ username }} permissions role-based superuser yes
   set template sample config mgt-config users {{ username }} password

When the password command is entered, the user will be prompted for a password.


Template > Syslog and Email Server Profiles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   set template sample config shared log-settings syslog Sample_Syslog_Profile server Sample_Syslog server {{ ip address }}
   set template sample config shared log-settings email Sample_Email_Profile server Sample_Email_Profile from {{ from }}
   set template sample config shared log-settings email Sample_Email_Profile server Sample_Email_Profile to {{ to }}
   set template sample config shared log-settings email Sample_Email_Profile server Sample_Email_Profile gateway {{ address }}


Device-Group > Address Objects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   set device-group sample address Sinkhole-IPv4 ip-netmask {{ IPv4 address }}
   set device-group sample address Sinkhole-IPv6 ip-netmask {{ IPv6 address }}


Device-Group Anti-Spyware Security Profiles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The same commands are used across all of the template security profiles ending in ``-AS``.

::

   set device-group sample profiles spyware {{ profile name }} botnet-domains sinkhole ipv4-address {{ IPv4 address }}
   set device-group sample profiles spyware {{ profile name }} botnet-domains sinkhole ipv6-address {{ IPv6 address }}
