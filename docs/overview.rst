Iron Skillet Overview
=====================

Welcome to the Iron Skillet day one configuration templates library.

The next-generation firewall configuration templates are based on existing `best practice recommendations`_
from Palo Alto Networks.

.. _best practice recommendations: https://www.paloaltonetworks.com/documentation/best-practices


Instead of extensive and detailed 'how to' documentation, the templates provide an easy to implement
configuration model that is use case agnostic.
The emphasis is on key security elements such as dynamic updates, security profiles, rules, and logging that
should be consistent across deployments.

.. Note::
    These are not complete configuration templates. To insert the device into the network requires interface, zone, routing,
    and other settings outside the scope of the day one templates. Also not included are use-case specific items such as whitelist security rules,
    userID settings, and decryption policies that can be deployment and use case specific.


Why use day one templates?
--------------------------

Palo Alto Networks has expertise in both security prevention and its own product portfolio. Best practice documentation is designed to
provide knowledge sharing of this expertise to customers and partners. This sharing helps improve security posture
across various scenarios.

The templates play a complementary role by taking common best practices recommendations and compiling them into pre-built
day one configurations that can be readily loaded into Panorama or a next-generation firewall. The benefits include:

    + Faster time to implement
    + Reduce configuration errors
    + Improve security posture


How can the templates be utilized?
----------------------------------

The templates are available on GitHub at |repourl|.

Select the branch specific to the software release for your deployment.

The library consists of a set of xml configuration templates grouped by:

    + ``panos`` for stand-alone next-gen firewall deployments
    + ``panorama`` for Panorama system and managed device configurations

The templates in each device folder include:

    + ``snippets`` for more granular configuration elements
    + ``snippets with variables`` for snippet elements with variables for local value substitution
    + ``full config file`` to use for bootstrap or full import + load into a device
    + ``full config with variables`` to have a full file that supports local variable substitution

More details about methods for loading the templates are in the section 'Loading Templates'


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
