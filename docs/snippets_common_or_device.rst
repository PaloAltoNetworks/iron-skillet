
Common or per-device elements
=============================

Many of the configuration elements are common between Panorama and panos.
The variance is the xpath branch naming where the elements sits in the config tree.

.. Note::
    The '*' at the end of a template name denotes multiple files with the same leading text


Common snippets
---------------

These xml files are common across both platforms

    + address
    + device_setting
    + device_system
    + email_scheduler_simple
    + external_list
    + profile_group
    + profiles_*
    + report_group_simple
    + tag
    + zone_protection*


The rest are device specific based on xpath reference or configuration settings.
Examples are deltas between rule configuration with pre/post in Panorama and
log forwarding targets as Panorama or syslog.


Firewall specific
-----------------

    + log_settings_profiles
    + reports_simple
    + rulebase_*
    + shared_log_settings


Panorama specific
-----------------

    + log_collector_group
    + log_settings_profiles
    + panorama*
    + post_rulebase*
    + pre_rulebase*
    + reports_simple
    + shared_log_settings


