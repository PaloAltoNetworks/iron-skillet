Template variables
==================

The configurations include options for variable substitution.
The variables provide flexibility for templates configurations to be modified specific to each deployment.

A jinja model for variables is used with the form ``{{ variable }}``


The table below lists the template variables along with placeholder or recommended settings.

=====================   ====================    =========================================================
Variable name           Default value           Description
=====================   ====================    =========================================================
FW_NAME                 test                    used for hostname and device-group/template in Panorama
DNS_1                   8.8.8.8 (Google)        primary DNS server
DNS_2                   8.8.4.4 (Google)        secondary DNS server
NTP_1                   0.pool.ntp.org          primary NTP server
NTP_2                   1.pool.ntp.org          secondary NTP server
SINKHOLE_IPV4           72.5.65.111             IPv4 sinkhole address (Palo Alto Networks)
SINKHOLE_IPV6           2600:5200::1            IPv6 sinkhole address (IPv6 bogon)
INTERNET_ZONE           internet                baseline exception for reports
EMAIL_PROFILE_GATEWAY   192.0.2.1               email profile gateway address; NET-1 default
EMAIL_PROFILE_FROM      test@yourdomain.com     from address for email alerts
EMAIL_PROFILE_TO        test@yourdomain.com     to address for email alerts
SYSLOG_SERVER           192.0.2.2               syslog IP address; NET-1 unroutable default
CONFIG_EXPORT_IP        192.0.2.3               config bundle export target from Panorama; NET-1 default
=====================   ====================    =========================================================


