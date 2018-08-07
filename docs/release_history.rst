Release History
===============

Template content updates are high level. Details can be found in the template guides.


version 1.0.1
-------------

Released: August 7, 2018

Template Content
~~~~~~~~~~~~~~~~

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

Tools
~~~~~

    + added the build_full_config utility to create a full template from the config snippets

    + added the build_my_config utility
        * provide simple variable substituions using the my_variable inputs
        * store output into the my_config folder with unique naming


Documentation
~~~~~~~~~~~~~

    + moved docs to readthedocs.io
    + move to release-specific documentation


Template Archive
~~~~~~~~~~~~~~~~

    + moved to release branch per software release in github



version 1.0.0
-------------

Released: May 10, 2018

    + first release on github
    + xml snippets and full config
    + static pdf documentation