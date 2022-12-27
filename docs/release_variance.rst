
New PAN-OS Version Updates
==========================

11.0 new features
~~~~~~~~~~~~~~~~~

Security profiles
^^^^^^^^^^^^^^^^^

    + URL Filtering: Added "ransomware" and "encrypted-dns" categories with recommended enforcement settings

    + Vulnerability Protection: Enabled Cloud Inline Analysis

    + Vulnerability Protection: Enabled and Configured "SQL Injection" and "Command Injection" categories with recommended settings

10.2 new features
~~~~~~~~~~~~~~~~~

Security profiles
^^^^^^^^^^^^^^^^^

    + URL Filtering: Enable Cloud and Local Inline Categorizations

    + URL Filtering: Enable HTTP Header Logging options, User-Agent, Referer, X-Forwarded-For
    
    + Antivirus: Enable MsOffice and Shell analysis settings

    + External Dynamic Lists: Added Bulletproof and Tor Exit IP address EDLs

    + Zone Protection Profile: Added Alert Only ZPP

Device configuration
^^^^^^^^^^^^^^^^^

    + Disabled reporting of benign files

10.1 new features
~~~~~~~~~~~~~~~~~

Security profiles
^^^^^^^^^^^^^^^^^

    + Anti-spyware profile:  New DNS Security Service malicious categories set to sinkhole

    + URL Filtering: Set new real-time url category to alert


Device configuration
^^^^^^^^^^^^^^^^^^^^

    + packet buffer protection: set to allow (default)

10.0 new features
~~~~~~~~~~~~~~~~~

Security profiles
^^^^^^^^^^^^^^^^^

    + Antivirus profile: Wildfire ML dynamic classification to block all malicious file types

        * set all decoders to reset-both

        * set all file types to enabled

    + Anti-spyware profile:  DNS Security Service malicious categories set to sinkhole

    + URL Filtering: realtime page analysis; block all engines types under Dynamic Classification

Device configuration
^^^^^^^^^^^^^^^^^^^^

    + dynamic updates: set Wildfire schedule to 'realtime'

Decryption profile
^^^^^^^^^^^^^^^^^^

    + set protocol max version to TLSv1.3

Log Setting
^^^^^^^^^^^

    + GlobalProtect log forwarding




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
