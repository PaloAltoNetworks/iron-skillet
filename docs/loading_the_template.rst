
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


