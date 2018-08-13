Creating Loadable Configurations
================================

The base templates are designed for variable substitution.
The variables provide flexibility for templates configurations to be modified specific to each deployment.

A jinja model for variables is used with the form ``{{ variable }}``


.. Warning::
    The configuration templates for device and Panorama system include jinja 'if' conditionals.
    These are used by the build_my_config.py tool to determine what IP information should be added regarding
    the management interface.

    If the tool or jinja formats will not be used, remove the {% text %} statements.
    The user will also have to manually replace the variables in order for the config to load and commit


Variables list and descriptions
-------------------------------

The table below lists the template variables along with placeholder or recommended settings.

======================   =======================  ==========================================================
Variable name            Default value            Description
======================   =======================  ==========================================================
ADMINISTRATOR_USERNAME   admin                    superuser id; prompted when using build_my_config tool
ADMINISTRATOR_PASSWORD   admin                    superuser password; prompted and hashed in build_my_config
MYCONFIG_DIR             sample_my_config         my_config folder prefix when use build_my_config tool
FW_NAME                  sample                   used for hostname and device-group/template in Panorama
TEMPLATE                 sample                   Panorama sample template name
DEVICE_GROUP             sample                   Panorama sample device-group name
DNS_1                    8.8.8.8 (Google)         primary DNS server
DNS_2                    8.8.4.4 (Google)         secondary DNS server
NTP_1                    0.pool.ntp.org           primary NTP server
NTP_2                    1.pool.ntp.org           secondary NTP server
SINKHOLE_IPV4            72.5.65.111              IPv4 sinkhole address (Palo Alto Networks)
SINKHOLE_IPV6            2600:5200::1             IPv6 sinkhole address (IPv6 bogon)
INTERNET_ZONE            internet                 baseline exception for reports
EMAIL_PROFILE_GATEWAY    192.0.2.1                email profile gateway address; NET-1 default
EMAIL_PROFILE_FROM       test@yourdomain.com      from address for email alerts
EMAIL_PROFILE_TO         test@yourdomain.com      to address for email alerts
SYSLOG_SERVER            192.0.2.2                syslog IP address; NET-1 unroutable default
CONFIG_EXPORT_IP         192.0.2.3                config bundle export target from Panorama; NET-1 default
MGMT_TYPE                dhcp-client              Firewall mgmt IP type (dhcp-client or static)
MGMT_IP                 192.168.55.10            Firewall mgmt IP if type=static
MGMT_MASK                255.255.255.0            Firewall netmask if type=static
MGMT_DG                  192.168.55.2             Firewall default gateway if type=static
CONFIG_PANORAMA_IP       yes                      For build_my_config, determine if Panorama IP to be added
PANORAMA_TYPE            standard                 Used in order to set mgmt interface for standard or cloud
PANORAMA_IP              192.168.55.7             Panorama IP if to be added to my_config
PANORAMA_MASK            255.255.255.0            Panorama netmask if to be added to my_config
PANORAMA_DG              192.168.55.2             Panorama default gateway if to be added to my_config
======================   =======================  ==========================================================




Build My Configuration python utility
-------------------------------------

The tools folder in the iron-skillet repo contains a simple python utility for variable substitution.

This tools folder can be found at |repotools|

The directions below detail how to use the utility in a python virtual environment on Mac or Linux.
Similar instructions can work for Windows with python and pip installed.

.. NOTE::
    This tool is designed for Python 3.6 or layer.

Install build_my_config.py
~~~~~~~~~~~~~~~~~~~~~~~~~~


.. highlight:: bash

The initial steps are an overview to clone the repo and activate a python virtual environment.

::

    $ git clone |repourl|
    $ cd iron-skillet
    $ iron-skillet/python -m venv env
    $ source env/bin/activate
    (env)$ pip install -r requirements.txt

The virtual environment name is ``env`` and if active will likely be shown to the left of the command prompt.
If successful, the iron-skillet templates and tools are now ready to use.

Update the variable values
~~~~~~~~~~~~~~~~~~~~~~~~~~

Change into the tool directory, update the my_variables.py file then run build_my_configs.py.
The example shows the vi text editor but any text editor may be used.

::

    (env)$ cd tools
    (env)$ vi my_variables.py

Edit the my_variables.py file for your local deployment and save.

Key variables to edit include:

    + my_config folder prefix: text name specific to the configuration output

    + management interface type: static, dhcp-client, dhcp-cloud based on firewall deployment

    + Panorama deployment type: standard or cloud based on Panorama deployment


Run the application
~~~~~~~~~~~~~~~~~~~

Ensure the variable values are correct and run the application.

::

    (env)$ python3 build_my_config.py
    >>> Enter the superuser administrator account username:
    >>> Enter the superuser administrator account password:

This will run the python utility and output full and snippet xml config files.
Loadable configs are stored in the my_configs directory.
The config folder prefix is based on the MYCONFIG_DIR variable name.

.. Warning::
    You will be prompted for a username/password that will be used in the configuruation file.
    A hash is created for the password so it is unreadable and the default admin/admin is removed.
    Remember the user/password information before committing to a running firewall or Panorama.




