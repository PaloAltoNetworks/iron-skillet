

9.0 Update Items
================

New release model
-----------------

At initial release, focus on ability to run based on prior release features

Then as best practices are created, add those into the templates post-release


Modifications from 8.1 template
-------------------------------

    + move packet cap xml element in spyware profile

    + remove url 'block' stand-alone entry

    + customer url categories

        * add 'type' value to allow config to commit


9.0 new features
----------------

Security profiles
~~~~~~~~~~~~~~~~~

    + new url categories (risk, new domain)

        * set new categories to alert

        * over time move to custom dual category blocks (eg. parked + high)

    + new pan cloud dns option in spyware profile

        * action = sinkhole with single packet capture

    + AV profile and http2

        * set http2 decoder same as http for each profile


Device settings
~~~~~~~~~~~~~~~

    + API key lifetime

        * Iniially set to a high value with configuration variable
        * Default in minutes --> 525,600 is 1 year

    + WF file sizes

        * new file type script, set to max 2000 file size

    + Exporting log data

        * set max lines for csv output to supported maximum

