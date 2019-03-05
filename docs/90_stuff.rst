

9.0 Update Items
================

New release model
-----------------

At initial release, focus on ability to run based on prior release features

Then as best practices are created, add those into the templates post-release


8.1 fixes
---------

    + move packet cap xml element in spyware profile

    + update to use the pan cloud dns feature in spyware profile


9.0 new features
----------------

    + new url categories (risk, new domain)

        * set new categories to alert

        * over time move to custom dual category blocks (eg. parked + high)


    + API key lifetime

        * check with PM on recommended first value, set high and tune down
        * in minutes --> 525,600 is 1 year

    + WF file sizes

        * new file type script, set to max 2000 file size

    + AV profile and http2

        * set http2 decoder same as http for each profile

    + Exporting log data

        * set max lines for csv output to supported maximum

