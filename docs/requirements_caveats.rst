Requirements and Caveats
========================

Please read before using the IronSkillet configuration templates.

Requirements
------------

Using IronSkillet requires the following to properly load into Panorama and/or the NGFW

    * Software version 9.0

    * Active subscription for Threat Prevention

    * Updated application and antivirus content


.. Note::
    Threat Prevention and the antivirus content update are both required to gain access to the Palo Alto Networks
    provided External Dynamic Lists (EDLs) used in the security policies.


.. Note::
    URL Filtering, DNS Cloud Service, and Wildfire subscriptions are not required to load the configuration
    but are highly recommended as part of the best practice to utilize IronSkillet elements such as the URL
    Filtering, Spyware, and Wildifre security profiles and associated profile groups


Caveats
-------

Please review the following to understand any limitations or recommendations regarding the IronSkillet templates

    * The current version only supports IPv4 management interface configuration

    * IronSkillet loaded into a VM-50 will utilize the full profile capacity

        + See the section :ref:`vm50_profile_reduction` for more information

    * The Panorama full configuration template is based on a fully shared model

        + All device-group configuration at the Shared top of tree

        + Panorama template stacks should include the IronSkillet template

