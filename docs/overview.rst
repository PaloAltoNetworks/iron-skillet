IronSkillet Overview
=====================

Welcome to the IronSkillet day one configuration templates library.

The next-generation firewall configuration templates are based on existing `best practice recommendations`_
from Palo Alto Networks.

.. _best practice recommendations: https://www.paloaltonetworks.com/documentation/best-practices


Instead of extensive and detailed 'how to' documentation, the templates provide an easy to implement
configuration model that is use case agnostic.
The emphasis is on key security elements such as dynamic updates, security profiles, rules, and logging that
should be consistent across deployments.


Why use day one templates?
--------------------------

Palo Alto Networks has expertise in both security prevention and its own product portfolio. Best practice documentation
is designed to provide knowledge sharing of this expertise to customers and partners. This sharing helps improve security posture
across various scenarios.

The templates play a complementary role by taking common best practices recommendations and compiling them into pre-built
day one configurations that can be readily loaded into Panorama or a next-generation firewall. The benefits include:

    + Faster time to implement
    + Reduce configuration errors
    + Improve security posture


Using the templates
-------------------

The templates are available on GitHub specific to each PAN-OS software version.

`View github repo:` |
`10.0 <https://github.com/PaloAltoNetworks/iron-skillet/tree/panos_v10.0>`_ |
`9.1 <https://github.com/PaloAltoNetworks/iron-skillet/tree/panos_v9.1>`_ |
`9.0 <https://github.com/PaloAltoNetworks/iron-skillet/tree/panos_v9.0>`_ |
`8.1 <https://github.com/PaloAltoNetworks/iron-skillet/tree/panos_v8.1>`_ |

.. Note::
    versions 8.0 and 8.1 are still available but no longer will be updated

Use the branch specific to the software release for your deployment.

The library consists of a set of XML and set configuration templates grouped by:

    + ``panos`` for stand-alone next-gen firewall deployments
    + ``panorama`` for Panorama system and managed device configurations

The templates in each device-type folder include:

    + ``snippets`` for more granular configuration elements
    + ``full config file`` to use for bootstrap or full import + load into a device
    + ``set commands`` for traditional CLI configuration

There are also validation skillets for analysis of existing configurations

    + ``full assessment`` to see what IronSkillet elements are missing
    + ``9.x upgrade from 8.1`` to check for new skillet additions
    + ``10.x upgrade from 9.x`` to check for new skillet additions

Validation insights currently require applications such as panHandler (https://panhandler.readthedocs.io) for
analysis and results output.

Quick start using IronSkillet players
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

User can opt to use one of the :ref:`ironskillet_players` to render and load configurations. These apps and tools
are a great starting point to begin using IronSkillet.


Quick start using loadable configurations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The repo contains a set of ready-to-go loadable configurations that use IronSkillet placeholder values.
Formats include both XML and set commands.

The XML file can be imported and loaded easily to Panorama or a firewall. The set command model requires 'copy-and-paste'
from the CLI.

More information for loading and editing these configurations can be found at: :ref:`using_default_configs`.

Excel set command spreadsheet
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Also included for easy loading is an Excel formula-based spreadsheet with set commands. A variable value worksheet can be
edited to update the spreadsheet using localized values for various configuratino attributes.

More information for using the spreadsheet can be found at: :ref:`using_the_spreadsheet`.



Jinja-based XML snippet and set command templates
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Scripting or automation-centric users may prefer to use the base template files.
These are variable-based templates using a Jinja ``{{ variable }}`` notation.

The XML snippets with metadata are designed to use API-based configuration loading into Panorama or the firewall and
can be coupled with workflow tools for repeatable deployments.

Sample utilities are provided in the ``tools`` directory to create loadable configurations using these base templates.

See the sections :ref:`creating_loadable_configs` and :ref:`loading_templates` for more information.


.. Note::
    Day one templates are not complete configuration templates. To insert the device into the network requires interface, zone, routing,
    and other settings outside the scope of the day one templates. Also not included are use-case specific items such as whitelist security rules,
    userID settings, and decryption policies that can be deployment and use case specific.


What is next after loading a template?
--------------------------------------

Based on the deployment scenario, the next steps may include:

    + GUI configuration of additional configuration elements specific to the deployment use case

    + API/scripted loading of additional configuration elements

In cases where the use case configuration has been merged with the templates, no further actions may be required.
A key example would be interface, NAT, zone, and security rule additions for a simple Internet gateway deployments.


Where can I find complete reference use case configurations?
------------------------------------------------------------

The initial release of the templates are use case agnostic.
However, as the community creates and shared reference configurations, they will be shared across the community
as an extension of the iron-skillet configurations.
