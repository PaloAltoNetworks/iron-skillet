
Release and Update History
==========================

Includes:

    + template releases
    + tools updates
    + documentation revisions

10.0 Template Release History
----------------------------

Template content updates are high level. Details can be found in the template guides.

0.0.1
^^^^^
Released July 21, 2020

    + set Wildfire dynamic updates to realtime
    + Antivirus profile: reset-both for dynamic classification, all file types enabled
    + Anti-spyware profile: set DNS malicious categories to sinkhole
    + set max version of TLSv1.3 in the decryption profile
    + URL filtering profile: use ML analysis and set to dynamic classification to block
    + URL filtering profile: move 'hacking' category to alert since not malicious
    + remove sinkhole address block policy and associated address object
    + remove http partial response so now allowed
    + remove XFF global configuration; now profile or policy specific
    + remove 'no decrypt' decryption policy that checks for expired/invalid certs; too strict
    + update WF malicious reports using 'neq benign' instead of equal to malicious categories
    + remove telemetry configuration; new opt-in cert-based model in 10.0
    + add email profile protocol 'SMTP' required in configuration; TLS config is optional
    + add GlobalProtect log forwarding in log settings
    + update validation skillets based on above modifications
    + update metadata file for XML snippet skillets w/ option to skip IP address/admin user/DNS configuration elements
    + add helper commands for scripting-mode on for CLI copy-paste model
    + converted customer URL-filtering profile lingo from White-List/Black-List to Allow/Block
    + fixed Panorama set commands: include type "URL-List"
    + fix internal spyware XML snippets with medium severity as default


9.1 Template Release History
----------------------------

Template content updates are high level. Details can be found in the template guides.

0.0.3
^^^^^
Released September 16, 2020

    + URL filtering profile: move 'hacking' category to alert since not malicious
    + remove sinkhole address block policy and associated address object
    + remove http partial response so now allowed
    + remove 'no decrypt' decryption policy that checks for expired/invalid certs; too strict
    + update WF malicious reports using 'neq benign' instead of equal to malicious categories
    + update validation skillets based on above modifications
    + update metadata file for XML snippet skillets w/ option to skip IP address/admin user/DNS configuration elements
    + converted customer URL-filtering profile lingo from White-List/Black-List to Allow/Block

0.0.2
^^^^^
Released April 28, 2020

    + Update WF file size limits to match the BPA
    + validation updates including grayware check and WF file size limits
    + metadata file updates: variable clean up with toggle_hint and help_text
    + Panorama not shared skillet file reference error

0.0.1
^^^^^
Released January 22, 2020

    + first release based on v9.0
    + no release specific additions


9.0 Template Release History
----------------------------

Template content updates are high level. Details can be found in the template guides.

0.0.6
^^^^^
Released September 16, 2020

    + URL filtering profile: move 'hacking' category to alert since not malicious
    + remove sinkhole address block policy and associated address object
    + remove http partial response so now allowed
    + remove 'no decrypt' decryption policy that checks for expired/invalid certs; too strict
    + update WF malicious reports using 'neq benign' instead of equal to malicious categories
    + update validation skillets based on above modifications
    + update metadata file for XML snippet skillets w/ option to skip IP address/admin user/DNS configuration elements
    + converted customer URL-filtering profile lingo from White-List/Black-List to Allow/Block

0.0.5
^^^^^
Released April 28, 2020

    + Update WF file size limits to match the BPA
    + validation updates including grayware check and WF file size limits
    + metadata file updates: variable clean up with toggle_hint and help_text
    + Panorama not shared skillet file reference error

0.0.4
^^^^^
Released January 22, 2020

    + added grayware and cryptcurrency url categories
    + added missing User tag log settings
    + inclusion of validation skillets

0.0.3
^^^^^

Released c September, 2019

    + minor updates


0.0.2
^^^^^

Released July 30, 2019

    + Added password complexity and admin lockout elements
    + Dynamic updates for GlobalProtect
    + Opt-out default for the Palo Alto Networks EDL associated security rules
    + Removed the IPv4 and IPv6 Bogon EDLs and associated security rules
    + Updated the IPv4 sinkhole to use FQDN instead of an IP address
    + Clean up for the baseline configuration to remove IPSEC, IKE, QoS defaults
    + Clean up for URL Block and Allow category usage in profiles

0.0.1
^^^^^

Released March 15, 2019

    + migrated initial template from 8.1
    + inclusion of new features per the 9.0 new features documentation


8.x Template Release History
----------------------------

Template content updates are high level. Details can be found in the template guides.

1.0.6
^^^^^

Released July 30, 2019

    + Added password complexity and admin lockout elements
    + Dynamic updates for GlobalProtect
    + Opt-out default for the Palo Alto Networks EDL associated security rules
    + Removed the IPv4 and IPv6 Bogon EDLs and associated security rules
    + Updated the IPv4 sinkhole to use FQDN instead of an IP address
    + Clean up for the baseline configuration to remove IPSEC, IKE, QoS defaults
    + Clean up for URL Block and Allow category usage in profiles

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

Jul 21, 2020
^^^^^^^^^^^^

    + update set command and spreadsheet scripts to only use variables contained in config section
    + modify set command expect test script to use start-stop row values

Jan 22, 2020
^^^^^^^^^^^^

    + updated the build_full_config.py with the ability to merge snippets using same xpath

Jul 30, 2019
^^^^^^^^^^^^

    + added build_all.py to create all full configs and spreadsheets
    + test_set_commands.py and test_full_config.py to load and test configuration changes


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

Jul 22, 2020
^^^^^^^^^^^^

    + update viz guide with 10.0 mods and UI
    + update template text where required based on 10.0 mods

April 29, 2020
^^^^^^^^^^^^^^

    + update WF file size limit image in visual guide
    + create sidebar menu sections
    + add content for skillet players


Janurary 22, 2020
^^^^^^^^^^^^^^^^^

    + addition of visual guide for panos
    + validation skillet section added
    + add 9.1 related content links

July 30, 2019
^^^^^^^^^^^^^

    + Move docs to their own doc branch and merge as a single doc set
    + Add in associated template changes and new xml links (mgt user config and password complexity)
    + Add a release variance doc to show deltas for new releases
    + Addition of requirements and caveats to use IronSkillet
    + Pointers to PanHandler and SkilletCLI as new tools to load configurations

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
