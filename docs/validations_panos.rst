Config Validations: PAN-OS
==========================

Validation skillets allow for assessment of the config files or system state with pass/fail outputs based on
validation skillet test rules. Each test result is mapped to its respective section in the Visual Guide for
manual review and remediation.

The following validations are provided with IronSkillet

Full Configuration Assessment
-----------------------------

`View validation test file:` |
`9.0 <https://github.com/PaloAltoNetworks/iron-skillet/blob/panos_v9.0/validations/panos/IronSkillet_assessment_panos/.meta-cnc.yaml>`_ |
`9.1 <https://github.com/PaloAltoNetworks/iron-skillet/blob/panos_v9.1/validations/panos/IronSkillet_assessment_panos/.meta-cnc.yaml>`_ |
`10.0 <https://github.com/PaloAltoNetworks/iron-skillet/blob/panos_v10.0/validations/panos/IronSkillet_assessment_panos/.meta-cnc.yaml>`_ |

Looks at a firewall xml configuration file to determine what elements recommended by IronSkillet are missing from the
analyzed config file. Types of validation tests include the following based on IronSkillet recommendations with some
elements version specific:

    + dynamic updates configured
    + use of snmpv3
    + dns and ntp configured
    + login banner configured
    + timezone set to UTC
    + auto acquire commit lock enabled
    + X-Forward-For settings
    + http range disabled
    + inspection queue related settings
    + max rows for CSV export
    + API key lifetime
    + admin attempts, timeout, and lockout
    + Wildfire file size limits configured
    + enable application block page
    + disable log suppression
    + prevent TCP evasions
    + configure password complexity
    + recommended zone protection profile
    + inclusion of IronSkillet named profiles and groups
    + logging configuration
    + EDL block rules
    + report and email scheduler related configuration


Upgrade to Newer Release Deltas [10.x]
--------------------------------------

`View validation test file:` |
`10.0 <https://github.com/PaloAltoNetworks/iron-skillet/tree/panos_v10.0/validations/panos/IronSkillet_v10x_update_panos>`_ |

Looks at a firewall xml configuration file to determine what elements recommended by IronSkillet are missing from a
recently upgraded PAN-OS version to 10.x. Types of validation tests include the following based on IronSkillet recommendations:

    + Wildfire dynamic updates set to realtime
    + AV profile using 'reset-both' for Dynamic Classification and all file types enabled
    + Anti-spyware profile DNS Security using 'sinkhole' action for malicious categories
    + URL-Filtering profile using 'block for Dynamic Classification, all engines
    + Recommended decryption profile max version set to TLSv1.3


Upgrade to Newer Release Deltas [9.x]
-------------------------------------

`View validation test file:` |
`9.0 <https://github.com/PaloAltoNetworks/iron-skillet/blob/panos_v9.0/validations/panos/IronSkillet_v90_update_panos/.meta-cnc.yaml>`_ |
`9.1 <https://github.com/PaloAltoNetworks/iron-skillet/blob/panos_v9.1/validations/panos/IronSkillet_v9x_update_panos/.meta-cnc.yaml>`_ |


Looks at a firewall xml configuration file to determine what elements recommended by IronSkillet are missing from a
recently upgraded PAN-OS version to 9.x. Types of validation tests include the following based on IronSkillet recommendations:

    + addition of panw-bulletproof-ip-list to the EDL block rules
    + API key lifetime configured
    + WF file size limits for script
    + IPv4 sinkhole address object is using FQDN
    + default-paloalto-cloud is used for the DNS security service setting in the anti-spyware profile
    + new URL categories such as newly-registered-domain, grayware and cryptocurrency have been added


