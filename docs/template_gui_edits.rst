
Using the GUI to Edit the Sample Full Config
============================================


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


GUI variable edits: Firewall
----------------------------

----------------------------------------------------------------------

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
   :width: 600


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
















