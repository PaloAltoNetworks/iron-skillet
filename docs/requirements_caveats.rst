Requirements and Caveats
========================

Please read before using the IronSkillet configuration templates.

Requirements
------------

Using IronSkillet requires the following to properly load into Panorama and/or the NGFW


    * Running software version 9.0

        + `Upgrade the firewall to 9.0`_
        + `Upgrade Panorama to 9.0`_


.. _Upgrade the firewall to 9.0: https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-new-features/upgrade-to-pan-os-90.html
.. _Upgrade Panorama to 9.0: https://docs.paloaltonetworks.com/panorama/9-0/panorama-admin/set-up-panorama/install-content-and-software-updates-for-panorama.html


    * Active subscription for Threat Prevention

        + `Activate the subscription licenses`_

.. _Activate the subscription licenses: http://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/subscriptions/activate-subscription-licenses

    * Updated application and antivirus content

        + `Install content and software updates`_


.. _Install content and software updates: https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/software-and-content-updates/install-content-and-software-updates.html


.. Note::
    The links are specific to PAN-OS v9.0 and users may switch to 8.0 or 8.1 based on deployed release


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

    * Be sure to edit or the default administrative superuser account if not part of initial configuration

        + If the default account information is used, the user is notified at login

        + To change or add superuser accounts see `Configure a Firewall Administrator`_

.. _Configure a Firewall Administrator: https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/firewall-administration/manage-firewall-administrators/configure-administrative-accounts-and-authentication/configure-a-firewall-administrator-account.html#


    * The current version only supports IPv4 management interface configuration


    * IronSkillet loaded into a VM-50 will utilize the full profile capacity
        + See the section :ref:`vm50_profile_reduction` for more information


    * The Panorama full configuration template is based on a fully shared model
        + All `device-group configuration`_ at the Shared top of tree
        + Additional Panorama `template stacks`_ should include the IronSkillet template

.. _device-group configuration: https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-web-interface-help/panorama-web-interface/panorama-device-groups.html
.. _template stacks: https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-web-interface-help/panorama-web-interface/panorama-templates.html