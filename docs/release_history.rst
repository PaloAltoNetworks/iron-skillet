
Release and Update History
==========================

Includes:

    + template releases
    + tools updates
    + documentation revisions


Template Release History
------------------------

Template content updates are high level. Details can be found in the template guides.

1.0.5
^^^^^

Released March 18, 2019

Template Content

    + added max lines for log csv output


1.0.4
^^^^^

Released January 8, 2019

Template Content

    + updated virus profiles from 'default' to 'reset-both' so explicit blocking
    + added set commands template as text file and Excel spreadsheet
    + loadable default configurations include full xml and set commands
    + update to the template stack snippet including <config> tree elements
    + removed GTP logging elements since not supported on all hardware platforms


1.0.3
^^^^^

Released Oct 3, 2018

Template Content

    + added a default security profile group based on the Outbound group


Documentation

    + fixed errors in the tools installation instructions


1.0.2
^^^^^

Released August 30, 2018

Template Content

    + modified device_system type=dhcp configuration elements to fix dhcp-client commit error


1.0.1
^^^^^

Released: August 7, 2018

Template Content

    + Device settings updates to increase security hardening

        * Prevent TCP and UDP buffer overflow and multi-part HTTP download evasions
        * Enable high DP load logging
        * Prevent App-ID buffer overflow evasion
        * set bypass-exceed-queue to 'no'
        * Prevent TCP and MPTCP evasions

    + Include default login banner

    + Correct url-filtering Alert-All profile to include command-and-control

    + Set default interzone action to a drop instead of deny

    + include firewall management interface options for dhcp-client, standard or cloud models

    + include Panorama options for standard or cloud deployments

    + using a tag attribute for the template version numbering


Documentation

    + moved docs to readthedocs.io
    + move to release-specific documentation


Template Archive

    + moved to release branch per software release in github


1.0.0
^^^^^

Released: May 10, 2018

    + first release on github
    + xml snippets and full config
    + static pdf documentation



Tools Release Updates
---------------------


Jan 8, 2019
^^^^^^^^^^^

    + moved config variables from a python dictionary to a yaml format
    + updated existing tools to support the yaml variables file
    + added a utility to create the Excel spreadsheet from the set conf file
    + removed the creation of default snippets output to loadable configs
    + renamed the output from 'my configs' to 'loadable configs' for clarity


Oct 3, 2018
^^^^^^^^^^^

    + modified variable model to support python 3.5 instead of 3.6 and later


August 7, 2018
^^^^^^^^^^^^^^


    + added the build_full_config utility to create a full template from the config snippets

    + added the build_my_config utility

        * provide simple variable substituions using the my_variable inputs
        * store output into the my_config folder with unique naming

May 3, 2019
^^^^^^^^^^^

    + fixed tools issue so will load the panw edl based security rules

Documentation Revisions
-----------------------

Documentation revisions outside of template-tooling updates. These are documented by date, not verison.

March 18, 2019
^^^^^^^^^^^^^^

    + added instructions to remove security profiles for reduced capacity VM-50
    + updated with inclusion of max csv lines for log output


Jan 8, 2019
^^^^^^^^^^^

    + simplified repo main README for non-python users
    + added documentation for the SET command spreadsheet
    + added next-level directory README files for added context
    + general edits for using tools based on tools changes
    + added description for Panorama template variations in Panorama template docs


Nov 2, 2018
^^^^^^^^^^^

    + added instructions for editing the full configuration template variables in the GUI
    + added instructions for editing the full configuration template variables using the console


Oct 3, 2018
^^^^^^^^^^^

    + fixed errors in the tools installation instructions


August 7, 2018
^^^^^^^^^^^^^^

    + moved docs to readthedocs.io
    + move to release-specific documentation


May 10, 2018
^^^^^^^^^^^^

    + first release on github
    + static pdf documentation
