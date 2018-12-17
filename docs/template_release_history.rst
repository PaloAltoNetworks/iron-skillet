Template Release History
========================

Template content updates are high level. Details can be found in the template guides.

1.0.4
-----

Released January 4, 2019

Template Content

    + updated virus profiles from 'default' to 'reset-both' so explicit blocking


1.0.3
-----

Released Oct 3, 2018

Template Content

    + added a default security profile group based on the Outbound group


Documentation

    + fixed errors in the tools installation instructions


1.0.2
-----

Released August 30, 2018

Template Content

    + modified device_system type=dhcp configuration elements to fix dhcp-client commit error


1.0.1
-----

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
-----

Released: May 10, 2018

    + first release on github
    + xml snippets and full config
    + static pdf documentation