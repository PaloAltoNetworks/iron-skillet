
New PAN-OS Version  Updates
===========================


8.1 Update Items
----------------

This includes changes from the 8.0 IronSkillet configurations

.. _allow-http-range: https://github.com/PaloAltoNetworks/iron-skillet/blob/ab1c2719ad9153652008733613373dcac252c7bb/templates/panos/snippets/device_setting.xml#L4

Syntax changes
~~~~~~~~~~~~~~

    + allow-http-range_ in device settings


8.1 new features
~~~~~~~~~~~~~~~~

    + WF file sizes

        * new file type script, set to max 2000 file size [available in later releases]


9.0 Update Items
-----------------

This includes changes from the 8.1 IronSkillet configurations


Syntax changes
~~~~~~~~~~~~~~

    + move packet cap xml element in spyware profile

    + remove url 'block' stand-alone entry

    + custom url categories

        * add 'type' value to allow config to commit

    + sinkhole IPv4 address uses FQDN instead of IP value


9.0 new features
~~~~~~~~~~~~~~~~

Security profiles
^^^^^^^^^^^^^^^^^

    + new url categories (risk, new domain)

        * set new categories to alert

        * over time move to custom dual category blocks (eg. parked + high)

    + new pan cloud dns option in spyware profile

        * action = sinkhole with single packet capture

    + AV profile and http2

        * set http2 decoder same as http for each profile


Device settings
^^^^^^^^^^^^^^^

    + API key lifetime

        * Iniially set to a high value with configuration variable
        * Default in minutes --> 525,600 is 1 year

9.1 new features
~~~~~~~~~~~~~~~~

Security profiles
^^^^^^^^^^^^^^^^^

    + new url categories (grayware, cryptocurrency)

        * set grayware to block

        * set cryptocurrency to alert

.. Note::
    these are shown with their initial 9.1 release but also supported in prior PAN-OS releases

