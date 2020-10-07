CIS Palo Alto Firewall 9 Benchmark
==================================

Terms of Use
------------

This documentation is text taken from the Center for Information Security specific to the
Palo Alto Networks firewall

Official benchmark content:
https://www.cisecurity.org/benchmark/palo_alto_networks/

Mirroring the terms of use from the official document:
https://www.cisecurity.org/cis-securesuite/cis-securesuite-membership-terms-of-use/

Web documentation notes
-----------------------

The information captured here is a summary of each benchmark that excludes some of the section specific
intro text. For the complete set of content, please reference the office benchmark document.

The official document also includes references to the intended audience, consensus guidance, scoring, and
current acknowledgements for key contributors.

Associated CIS Controls are captured in the benchmark document and currently omited from this web documentation
with an emphasis on audit and remediation.


1.1.1.1 Syslog logging should be configured
-------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
Scored

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1

Description
^^^^^^^^^^^
Syslog logging is a standard logging protocol that is widely supported.
It is recommended for a level 1 deployment only, as syslog does not support encryption.

Rationale
^^^^^^^^^
Sending all system logs to a remote host is recommended to provide protected, long term storage and archiving.
This also places a copy of the logs in a second location, in case the primary (on the firewall) logs are compromised.
Storing logs on a remote host also allows for more flexible log searches and log processing,
as well as many methods of triggering events or scripts based on specific log events or combinations of events.
Finally, remote logging provides many organizations with the opportunity to combine logs from disparate infrastructure
in a SIEM (Security Information and Event Management) system.

Logging to an external system is also usually required by most regulatory frameworks.

Audit
^^^^^
Navigate to Device > Server Profiles > Syslog

Ensure that a valid Syslog profile is configured, and that it points to
a valid Syslog host.

Navigate to Device > Log Settings

Under System, verify that at least one Syslog entry exists and
that at least one entry has "All Logs" selected. Each Syslog entry must have a valid Syslog Profile attached.

Under Configuration, verify that at least one Syslog entry exists and that at least one entry has "All Logs" selected.
Each Syslog entry must have a valid Syslog Profile attached.

Under User-ID, verify that at least one Syslog entry exists
and that at least one entry has "All Logs" selected. Each Syslog entry must have a valid Syslog Profile attached.

Under HIP Match (Host Information Profile), verify that at least one Syslog entry exists and that at least one entry
has "All Logs" selected. Each Syslog entry must have a valid Syslog Profile attached.

Under IP-Tag, verify that at
least one Syslog entry exists and that at least one entry has "All Logs" selected. Each Syslog entry must have a
valid Syslog Profile attached.

Remediation
^^^^^^^^^^^
Navigate to Device > Server Profiles > Syslog

Choose Add

Assign a Name to the Profile. Choose Add, and assign a
server name in the Name field, add an IP address or FQDN in the Syslog Server field. Edit other fields as appropriate
for your server.

Repeat if multiple Syslog destinations are required.

Navigate to Device > Log Settings

Under System, add an entry. Define a Name and a Filter setting.
Under Forward Methods, add a Syslog Profile in the Syslog section.
Ensure that at least one of the Log Settings Configuration entries has it's Filter setting at All Logs

Under Configuration, add an entry. Define a Name and a Filter setting. Under Forward Methods, add a Syslog Profile in the
Syslog section. Ensure that at least one of the Log Settings Configuration entries has it's Filter setting at
All Logs

Under User-ID, add an entry. Define a Name and a Filter setting. Under Forward Methods, add a Syslog Profile
in the Syslog section. Ensure that at least one of the Log Settings Configuration entries has it's Filter setting at
All Logs

Under HIP Match (Host Information Profile), add an entry. Define a Name and a Filter setting.
Under Forward Methods, add a Syslog Profile in the Syslog section. Ensure that at least one of the Log Settings
Configuration entries has it's Filter setting at All Logs

Under IP-Tag, add an entry. Define a Name and a
Filter setting. Under Forward Methods, add a Syslog Profile in the Syslog section.
Ensure that at least one of the Log Settings Configuration entries has it's Filter setting at All Logs

Impact
^^^^^^
Failure to properly store and archive logs for critical infrastructure leaves an organization without the tools
required to establish trends in events or activity, or to retrospectively analyze security or operational events
beyond the log timespan stored on the firewall. Not having remote logs also puts many organizations outside of
compliance with many regulatory frameworks. Finally, not logging to a remote host leaves organizations without
recourse in the event of a compromise of logs on the primary device. It is imperative that organizations log critical
infrastructure appropriately, store and archive these logs in a central location, and have a robust set of tools to
analyze logs both in real time and after the fact.

Default Value
^^^^^^^^^^^^^
By default no external logging is defined

References
^^^^^^^^^^
1. “PAN-OS Administrator's Guide 9.0 (English) - Configure Syslog Monitoring” -
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/monitoring/use-syslog-for-monitoring/configure-syslog-monitoring.html

1.1.1.2 SNMPv3 traps should be configured 
------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 2 

Description
^^^^^^^^^^^
SNMP v3 can be used for remote logging, and is the recommended protocol in higher security situations as it fully
supports encryption of logs.

Rationale
^^^^^^^^^
Sending all system logs to a remote host is recommended to provide protected, long term storage and archiving.
This also places a copy of the logs in a second location, in case the primary (on the firewall) logs are compromised.
Storing logs on a remote host also allows for more flexible log searches and log processing, as well as many methods
of triggering events or scripts based on specific log events or combinations of events. Finally, remote logging
provides many organizations with the opportunity to combine logs from disparate infrastructure in a
SIEM (Security Information and Event Management) system. Logging to an external system is also usually required by
most regulatory frameworks.

Audit
^^^^^
Navigate to Device > Server Profiles > SNMP Traps

Ensure that a valid SNMP profile is configured, that version V3 is
selected, and that it points to a valid SNMPv3 host. User, EngineID and Password fields should be completed
appropriately

Navigate to Device > Log Settings

Under System, verify that at least one SNMP entry exists,
corresponding to an SNMPv3 Server Profile and that at least one entry has "All Logs" selected.

Under Configuration,
verify that at least one SNMP entry exists, corresponding to a SNMPv3 Server Profile and that at least one entry has
"All Logs" selected.

Under User-ID, verify that at least one SNMP entry exists, corresponding to a SNMPv3
Server Profile and that at least one entry has "All Logs" selected.

Under HIP Match (Host Information Profile),
verify that at least one SNMP entry exists, corresponding to a SNMPv3 Server Profile and that at least one entry
has "All Logs" selected.

Under IP-Tag, verify that at least one SNMP entry exists, corresponding to a SNMPv3 Server
Profile and that at least one entry has "All Logs" selected.

Remediation
^^^^^^^^^^^
Navigate to Device > Server Profiles > SNMP Trap

Choose Add Assign a Name to the Profile, and specify version V3.

Choose Add, and assign a server name in the Name field, add an IP address or FQDN in the SNMP Manager field.
Edit the Password fields as appropriate for your server.

Repeat if multiple Syslog destinations are required.

Navigate to Device > Log Settings

Under System, add an entry. Define a Name and a Filter setting. Under Forward Methods,
add a SNMP Profile in the SNMP section.vEnsure that at least one of the Log Settings
Configuration entries has its Filter setting at All Logs

Under Configuration, add an entry. Define a Name and a Filter setting.
Under Forward Methods, add a SNMP Profile in the SNMP section.
Ensure that at least one of the Log Settings Configuration entries has its Filter setting at All Logs

Under User-ID, add an entry. Define a Name and a Filter setting. Under Forward Methods, add a SNMP Profile in the
SNMP section. Ensure that at least one of the Log Settings Configuration entries has its Filter setting at All Logs

Under HIP Match (Host Information Profile), add an entry. Define a Name and a Filter setting. Under Forward Methods,
add a SNMP Profile in the SNMP section. Ensure that at least one of the Log Settings Configuration
entries has its Filter setting at All Logs

Under IP-Tag, add an entry. Define a Name and a Filter setting. Under Forward Methods, add a SNMP Profile
in the SNMP section. Ensure that at least one of the Log Settings Configuration entries has its Filter
setting at All Logs

Impact
^^^^^^
Failure to properly store and archive logs for critical infrastructure leaves an organization without the tools
required to establish trends in events or activity, or to retrospectively analyze security or operational events
beyond the log timespan stored on the firewall. Not having remote logs also puts many organizations outside of
compliance with many regulatory frameworks. Finally, not logging to a remote host leaves organizations without
recourse in the event of a compromise of logs on the primary device. It is imperative that organizations log
critical infrastructure appropriately, store and archive these logs in a central location, and have a robust
set of tools to analyze logs both in real time and after the fact. Not encrypting log data as it transits the
network allows an attacker to mount a "MiTM" (Monkey in the Middle) attack, which allows them to intercept and/or
modify logs as they transit from the source to the destination.

Default Value
^^^^^^^^^^^^^
By default no external logging is defined 

References
^^^^^^^^^^
1. “PAN-OS Administrator's Guide 9.0 (English) - Forward Traps to an SNMP Manager” -
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/monitoring/snmp-monitoring-and-traps/forward-traps-to-an-snmp-manager#

1.1.2 Ensure 'Login Banner' is set 
-----------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1 

Description
^^^^^^^^^^^
Configure a login banner, ideally approved by the organization’s legal team. This banner should, at minimum,
prohibit unauthorized access, provide notice of logging or monitoring, and avoid using the word “welcome” or
similar words of invitation.

Rationale
^^^^^^^^^
Through a properly stated login banner, the risk of unintentional access to the device by unauthorized users
is reduced. Should legal action take place against a person accessing the ignorance.

Audit
^^^^^
Navigate to Device > Setup > Management > General Settings.

Verify that Login Banner is set appropriately for your organization.

Remediation
^^^^^^^^^^^
Navigate to Device > Setup > Management > General Settings.

Set Login Banner as appropriate for your organization.

Default Value
^^^^^^^^^^^^^
Not configured 

References
^^^^^^^^^^
1. “How to Configure the Device Login Banner” -
https://live.paloaltonetworks.com/docs/DOC-7964


1.1.3 Ensure 'Enable Log on High DP Load' is enabled 
-----------------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1 

Description
^^^^^^^^^^^
Enable the option 'Enable Log on High DP Load' feature.
When this option is selected, a system log entry is created when the utilization.

Rationale
^^^^^^^^^
services accessed through the device can occur. Logging this event can help with troubleshooting system performance. 

Audit
^^^^^
Navigate to Device > Setup > Management > Logging and Reporting Settings > Log Export and Reporting.

Verify Enable Log on High DP Load is checked.

Remediation
^^^^^^^^^^^
Navigate to Device > Setup > Management > Logging and Reporting Settings > Log Export and Reporting.

Set the Enable Log on High DP Load box to checked.

Impact
^^^^^^
Sustained attacks, especially volumetric DOS and DDOS attacks will often affect CPU utilization.
This setting will generate an event that is easily monitored for and alerted on. While setting CPU utilization
watermarks in a Network Management System is a standard practice, this setting does not depend on even having
an NMS, it doesn't require anything other than standard logging to implement.

Default Value
^^^^^^^^^^^^^
Not enabled   

References
^^^^^^^^^^
1. "What is Enable Log on High DP Load" - https://live.paloaltonetworks.com/docs/DOC-4075 


1.2.1 Ensure 'Permitted IP Addresses' is set to those necessary for device management 
--------------------------------------------------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1 

Description
^^^^^^^^^^^
Permit only the necessary IP addresses to be used to manage the device. 

Rationale
^^^^^^^^^
Management access to the device should be restricted to the IP addresses or subnets used by firewall administrators.
Permitting management access from other IP addresses increases the risk of unauthorized access through password
guessing, stolen credentials, or other means.

Audit
^^^^^
Navigate to Device > Setup > Interfaces > Management.

Verify that Permitted IP Addresses is limited only to those necessary for device management.

Remediation
^^^^^^^^^^^
Navigate to Device > Setup > Interfaces > Management.

Set Permitted IP Addresses to only those necessary for device management for the SSH and HTTPS protocols.
If no profile exists, create one that has these addresses set.

Default Value
^^^^^^^^^^^^^
Not enabled (all addresses that can reach the interface are permitted)     

References
^^^^^^^^^^
1. "How to Allow Certain IP Addresses on the Management Interface" -
https://live.paloaltonetworks.com/docs/DOC-8432

2. “PAN-OS Administrator's Guide 9.0 (English) - Best Practices for Securing Administrative Access":
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/getting-started/best-practices-for-securing-administrative-access.html#


1.2.2 Ensure 'Permitted IP Addresses' is set for all management profiles where SSH, HTTPS, or SNMP is enabled 
--------------------------------------------------------------------------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1 

Description
^^^^^^^^^^^
For all management profiles, only the IP addresses required for device management should be specified. 

Rationale
^^^^^^^^^
If a Permitted IP Addresses list is either not specified or is too broad, an attacker may gain the ability to
attempt management access from unintended locations, such as the Internet. The “Ensure 'Security Policy'
denying any/all traffic exists at the bottom of the security policies ruleset” recommendation in this
benchmark can provide additional protection by requiring a security policy specifically allowing device
management access.

Audit
^^^^^
Navigate to Network > Network Profiles > Interface Management.

In each profile, for each of the target protocols (SNMP, HTTPS, SSH), verify that Permitted IP Addresses is
limited to those necessary for device management.

Remediation
^^^^^^^^^^^
Navigate to Network > Network Profiles > Interface Management.

In each profile, for each of the target protocols (SNMP, HTTPS, SSH), set Permitted IP Addresses to only
include those necessary for device management. If no profile exists, create one that has these options set.


Default Value
^^^^^^^^^^^^^
Not enabled 

References
^^^^^^^^^^
1. "How to Allow Certain IP Addresses on the Management Interface" -
https://live.paloaltonetworks.com/docs/DOC-8432

2. “PAN-OS Administrator's Guide 9.0 (English) - Best Practices for Securing Administrative Access":
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/getting-started/best-practices-for-securing-administrative-access.html#


1.2.3 Ensure HTTP and Telnet options are disabled for the management interface
------------------------------------------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1 

Description
^^^^^^^^^^^
HTTP and Telnet options should not be enabled for device management. 

Rationale
^^^^^^^^^
Management access over cleartext services such as HTTP or Telnet could result in a compromise of administrator
credentials and other sensitive information related to device management. Theft of either administrative credentials
or session data is easily accomplished with a "Man in the Middle" attack.

Audit
^^^^^
Navigate to Device > Setup > Interfaces > Management.

Verify that the HTTP and Telnet options are both unchecked.

Remediation
^^^^^^^^^^^
Navigate to Device > Setup > Interfaces > Management.

Set the HTTP and Telnet boxes to unchecked.


Default Value
^^^^^^^^^^^^^
Not set. (HTTP and Telnet are disabled by default) 

References
^^^^^^^^^^
1.  "How to Configure a Layer 3 Interface to act as a Management Port" -
https://live.paloaltonetworks.com/t5/Configuration-Articles/How-to-Configure-a-Layer-3-Interface-to-act-as-a-Management-Port/ta-p/59024

2. “PAN-OS Administrator's Guide 9.0 (English) - Best Practices for Securing Administrative Access":
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/getting-started/best-practices-for-securing-administrative-access.html#


1.2.4 Ensure HTTP and Telnet options are disabled for all management profiles 
------------------------------------------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1 

Description
^^^^^^^^^^^
HTTP and Telnet options should not be enabled for device management. 

Rationale
^^^^^^^^^
Management access over cleartext services such as HTTP or Telnet could result in a compromise of administrator
credentials and other sensitive information related to device management.

Audit
^^^^^
Navigate to Network > Network Profiles > Interface Management.

For each Interface Management profile verify that the HTTP and Telnet options are both unchecked.

Remediation
^^^^^^^^^^^
Navigate to Network > Network Profiles > Interface Management.

For each Profile, set the HTTP and Telnet boxes to unchecked.


References
^^^^^^^^^^
1. “PAN-OS Administrator's Guide 9.0 (English) - Best Practices for Securing Administrative Access":
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/getting-started/best-practices-for-securing-administrative-access.html#

2. “PAN-OS Administrator's Guide 9.0 (English) - Use Interface Management Profiles to Restrict Access":
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/networking/configure-interfaces/use-interface-management-profiles-to-restrict-access.html#


1.2.5 Ensure valid certificate is set for browser-based administrator interface 
--------------------------------------------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Not Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 2 

Description
^^^^^^^^^^^
In most cases, a browser HTTPS interface is used to administer the Palo Alto appliance.
The certificate used to secure this session should satisfy the following criteria:

1. A valid certificate from a trusted source should be used. While a certificate from a trusted Public
Certificate Authority is certainly valid, one from a trusted Private Certificate Authority is absolutely
acceptable for this purpose.

2. The certificate should have a valid date. It should not have a "to" date in the past (it should not be expired),
and should not have a "from" date in the future.

3. The certificate should use an acceptable cipher and encryption level.

Rationale
^^^^^^^^^
If a certificate that is self-signed, expired, or otherwise invalid is used for the browser HTTPS interface,
administrators in most cases will not be able to tell if their session is being eavesdropped on or injected
into by a "Man in the Middle" attack.

Audit
^^^^^
Verify that the certificate used to secure HTTPS sessions meets the criteria by reviewing the appropriate certificate:

Navigate to Device > Certificate Management > Certificates

Verify that this Certificate is properly applied to the Management Interface:

Navigate to Device > Setup > Management > General Settings > SSL/TLS Service Profile

Remediation
^^^^^^^^^^^
Create or acquire a certificate that meets the stated criteria and set it:

Navigate to Device > Certificate Management > Certificates

Import an appropriate Certificate for your administrative session, from a trusted Certificate Authority.

Navigate to Device > Certificate Management > SSL/TLS Service Profile

Choose or import the certificate you want to use for the web based administrative session.

Navigate to Device > Setup > Management > General Settings > SSL/TLS Service Profile

Choose the Service Profile that you have configured

Impact
^^^^^^
If the default self-signed certificate is used, an administrator will not be able to clearly tell if their
HTTPS session is being hijacked or not. Using a trusted certificate ensures that the session is
both encrypted and trusted.

Default Value
^^^^^^^^^^^^^
A self-signed certificate is installed by default for the administrative interface. 

References
^^^^^^^^^^

1. "How to Configure a Certificate for Secure Web GUI Access" -
https://live.paloaltonetworks.com/t5/Configuration-Articles/How-to-configure-a-certificate-for-secure-web-gui-access/ta-p/68653

2. “PAN-OS Administrator's Guide 9.0 (English) - Best Practices for Securing Administrative Access":
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/getting-started/best-practices-for-securing-administrative-access.html#

Notes
^^^^^

Verify that the clock is both accurate and reliable on both the Palo Alto and on the administrative workstations
before setting the SSL/TLS Service Profile. Inaccurate or mismatched clocks will result in certificate errors
and can result in loss of HTTPS administrative access.

1.3.1 Ensure 'Minimum Password Complexity' is enabled 
-----------------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1 

Description
^^^^^^^^^^^
This checks all new passwords to ensure that they meet basic requirements for strong passwords. 

Rationale
^^^^^^^^^
Password complexity recommendations are derived from the USGCB (United States Government Configuration Baseline),
Common Weakness Enumeration, and benchmarks published by the CIS (Center for Internet Security).
Password complexity adds entropy to a password, in comparison to a simple password of the same length.
A complex password is more difficult to attack, either directly against administrative interfaces or cryptographically,
against captured password hashes. However, making a password of greater length will generally have a greater impact
in this regard, in comparison to making a shorter password more complex.

Audit
^^^^^
Navigate to Device > Setup > Management > Minimum Password Complexity.

Verify Enabled is checked Ensure that the various password settings to values that are appropriate to your organization.
Non-zero values should be set for Minimum Uppercase, Lowercase and Special Characters.
"Block Username Inclusion" should be enabled.

Remediation
^^^^^^^^^^^
Navigate to Device > Setup > Management > Minimum Password Complexity.

Set Enabled to be checked Set that the various password settings to values that are appropriate to your organization.
It is suggested that there at least be some special characters enforced, and that a minimum length be set.
Ensure that non-zero values are set for Minimum Uppercase, Lowercase and Special Characters.
"Block Username Inclusion" should be enabled. Operationally, dictionary words should be avoided for
all passwords - passphrases are a much better alternative.

Impact
^^^^^^
Simple passwords make an attacker's job very easy. There is a reasonably short list of commonly used admin
passwords for network infrastructure, not enforcing password lengths and complexity can lend itself
to making an attacker's brute force attack successful.

Default Value
^^^^^^^^^^^^^
Not enabled. 

References
^^^^^^^^^^
1. “PAN-OS Administrator's Guide 9.0 (English) - Best Practices for Securing Administrative Access” -
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/getting-started/best-practices-for-securing-administrative-access.html


1.3.2 Ensure 'Minimum Length' is greater than or equal to 12 
-------------------------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1 

Description
^^^^^^^^^^^
This determines the least number of characters that make up a password for a user account. 

Rationale
^^^^^^^^^
A longer password is much more difficult to attack, either directly against administrative interfaces or cryptographically,
against captured password hashes. Making a password of greater length will generally have a greater impact in this
regard, in comparison to making a shorter password more complex. Passphrases are a commonly used recommendation,
to make longer passwords more palatable to end users. Administrative staff however generally use "password safe"
applications, so a long and complex password is more easily implemented for most infrastructure administrative interfaces.

Audit
^^^^^
Navigate to Device > Setup > Management > Minimum Password Complexity.

Verify Minimum Length is greater than or equal to 12

Remediation
^^^^^^^^^^^
Navigate to Device > Setup > Management > Minimum Password Complexity.

Set Minimum Length to greater than or equal to 12

Impact
^^^^^^
Longer passwords are much more difficult to attack. This is true of attacks against the administrative interfaces
themselves, or of decryption attacks against captured hashes. A longer password will almost always have a more
positive impact than a shorter but more complex password.

Default Value
^^^^^^^^^^^^^
Not enabled.   

References
^^^^^^^^^^
1. “PAN-OS Administrator's Guide 9.0 (English) - Best Practices for Securing Administrative Access” -
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/getting-started/best-practices-for-securing-administrative-access.html

1.3.3 Ensure 'Minimum Uppercase Letters' is greater than or equal to 1 
-----------------------------------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1 

Description
^^^^^^^^^^^
This checks all new passwords to ensure that they contain at least one English uppercase character (A through Z). 

Rationale
^^^^^^^^^
This is one of several settings that, when taken together, ensure that passwords are sufficiently complex as to
thwart brute force and dictionary attacks.

Audit
^^^^^
Navigate to Device > Setup > Management > Minimum Password Complexity

Verify Minimum Uppercase Letters is greater than or equal to 1

Remediation
^^^^^^^^^^^
Navigate to Device > Setup > Management > Minimum Password Complexity

Set Minimum Uppercase Letters to greater than or equal to 1

Default Value
^^^^^^^^^^^^^
Not enabled. 

References
^^^^^^^^^^
1. “PAN-OS Administrator's Guide 9.0 (English) - Best Practices for Securing Administrative Access” -
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/getting-started/best-practices-for-securing-administrative-access.html


1.3.4 Ensure 'Minimum Lowercase Letters' is greater than or equal to 1 
-----------------------------------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1 

Description
^^^^^^^^^^^
This checks all new passwords to ensure that they contain at least one English lowercase character (a through z). 

Rationale
^^^^^^^^^
This is one of several settings that, when taken together, ensure that passwords are sufficiently complex as to
thwart brute force and dictionary attacks.

Audit
^^^^^
Navigate to Device > Setup > Management > Minimum Password Complexity

Verify Minimum Lowercase Letters is greater than or equal to 1

Remediation
^^^^^^^^^^^
Navigate to Device > Setup > Management > Minimum Password Complexity

Set Minimum Lowercase Letters to greater than or equal to 1


Default Value
^^^^^^^^^^^^^
Not enabled. 

References
^^^^^^^^^^
1. “PAN-OS Administrator's Guide 9.0 (English) - Best Practices for Securing Administrative Access” -
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/getting-started/best-practices-for-securing-administrative-access.html


1.3.5 Ensure 'Minimum Numeric Letters' is greater than or equal to 1 
---------------------------------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1 

Description
^^^^^^^^^^^
This checks all new passwords to ensure that they contain at least one base 10 digit (0 through 9). 

Rationale
^^^^^^^^^
This is one of several settings that, when taken together, ensure that passwords are sufficiently complex as to
thwart brute force and dictionary attacks.

Audit
^^^^^
Navigate to Device > Setup >Management > Minimum Password Complexity`

Verify Minimum Numeric Letters is greater than or equal to 1

Remediation
^^^^^^^^^^^
Navigate to Device > Setup > Management > Minimum Password Complexity

Set Minimum Numeric Letters to greater than or equal to 1

Impact
^^^^^^
nan

Default Value
^^^^^^^^^^^^^
Not enabled. 

References
^^^^^^^^^^
1. “PAN-OS Administrator's Guide 9.0 (English) - Best Practices for Securing Administrative Access” -
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/getting-started/best-practices-for-securing-administrative-access.html

Notes
^^^^^
nan

1.3.6 Ensure 'Minimum Special Characters' is greater than or equal to 1 
------------------------------------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1 

Description
^^^^^^^^^^^
This checks all new passwords to ensure that they contain at least one non-alphabetic character
(for example,!, $, #, %).

Rationale
^^^^^^^^^
This is one of several settings that, when taken together, ensure that passwords are sufficiently complex as to
thwart brute force and dictionary attacks.

Audit
^^^^^
Navigate to Device > Setup > Management > Minimum Password Complexity

Verify Minimum Special Characters is greater than or equal to 1

Remediation
^^^^^^^^^^^
Navigate to Device > Setup > Management > Minimum Password Complexity

Set Minimum Special Characters to greater than or equal to 1


Default Value
^^^^^^^^^^^^^
Not enabled. 

References
^^^^^^^^^^
1. “PAN-OS Administrator's Guide 9.0 (English) - Best Practices for Securing Administrative Access” -
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/getting-started/best-practices-for-securing-administrative-access.html


1.3.7 Ensure 'Required Password Change Period' is less than or equal to 90 days 
--------------------------------------------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1 

Description
^^^^^^^^^^^
This defines how long a user can use a password before it expires. 

Rationale
^^^^^^^^^
The longer a password exists, the higher the likelihood that it will be compromised by a brute force attack,
by an attacker gaining general knowledge about the user and guessing the password, or by the user sharing the password.

Audit
^^^^^
Navigate to Device > Setup > Management > Minimum Password Complexity.

Verify Required Password Change Period (days) is less than or equal to 90

Remediation
^^^^^^^^^^^
Navigate to Device > Setup > Management > Minimum Password Complexity.

Set Required Password Change Period (days) to less than or equal to 90

Impact
^^^^^^
Failure to change administrative passwords can result in a slow "creep" of people who have access.
Especially in a situation with high staff turnover (for instance, in a NOC or SOC situation), administrative
passwords need to be changed frequently. Administrative credentials should not be shared across multiple devices.
In a NOC/SOC situation, it's important to not share administrative credentials between operators
(names accounts should be used), and in particular administrative credentials should never be shared across
different customer infrastructures.

Default Value
^^^^^^^^^^^^^
Not enabled.   

References
^^^^^^^^^^
1. “PAN-OS Administrator's Guide 9.0 (English) - Best Practices for Securing Administrative Access” -
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/getting-started/best-practices-for-securing-administrative-access.html

Notes
^^^^^
This guidance is currently under some debate in the community. If the password length is sufficient and
password complexity is enforced, then in many organizations it is likely that the password change period can be
increased to 6, 9 or even 12 months.

1.3.8 Ensure 'New Password Differs By Characters' is greater than or equal to 3 
--------------------------------------------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1 

Description
^^^^^^^^^^^
This checks all new passwords to ensure that they differ by at least three characters from the previous password. 

Rationale
^^^^^^^^^
This is one of several settings that, when taken together, ensure that passwords are sufficiently complex as to
thwart brute force and dictionary attacks.

Audit
^^^^^
Navigate to Device > Setup > Management > Minimum Password Complexity

Verify New Password Differs By Characters is set to greater than or equal to 3

Remediation
^^^^^^^^^^^
Navigate to Device > Setup > Management > Minimum Password Complexity

Set New Password Differs By Characters to 3 or more

Impact
^^^^^^
This prevents the use of passwords that fall into a predictable pattern. Especially in situations that involve
staff turnover, having a pattern to password changes should be avoided.

Default Value
^^^^^^^^^^^^^
Not enabled. 

References
^^^^^^^^^^
1. “PAN-OS Administrator's Guide 9.0 (English) - Best Practices for Securing Administrative Access” -
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/getting-started/best-practices-for-securing-administrative-access.html


1.3.9 Ensure 'Prevent Password Reuse Limit' is set to 24 or more passwords 
---------------------------------------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1 

Description
^^^^^^^^^^^
This determines the number of unique passwords that have to be most recently used for a user account before a previous
password can be reused.

Rationale
^^^^^^^^^
The longer a user uses the same password, the greater the chance that an attacker can determine the password through
brute force attacks. Also, any accounts that may have been compromised will remain exploitable for as long as the
password is left unchanged. If password changes are required but password reuse is not prevented, or if users
continually reuse a small number of passwords, the effectiveness of a good password policy is greatly reduced.
While current guidance emphasizes password length above frequent password changes, not enforcing password re-use
guidance adds the temptation of using a small pool of passwords, which can make an attacker's job easier
across an entire infrastructure.

Audit
^^^^^
Navigate to Device > Setup > Management > Minimum Password Complexity.

Verify Prevent Password Reuse Limit is greater than or equal to 24

Remediation
^^^^^^^^^^^
Navigate to Device > Setup > Management > Minimum Password Complexity.

Set Prevent Password Reuse Limit to greater than or equal to 24


Default Value
^^^^^^^^^^^^^
Not enabled. 

References
^^^^^^^^^^
1. “PAN-OS Administrator's Guide 9.0 (English) - Best Practices for Securing Administrative Access” -
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/getting-started/best-practices-for-securing-administrative-access.html


1.3.10 Ensure 'Password Profiles' do not exist 
-----------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1 

Description
^^^^^^^^^^^
Password profiles that are weaker than the recommended minimum password complexity settings must not exist. 

Rationale
^^^^^^^^^
As password profiles override any 'Minimum Password Complexity' settings defined in the device, they generally
should not exist. If these password profiles do exist, they should enforce stronger password policies than what
is set in the 'Minimum Password Complexity' settings.

Audit
^^^^^
Navigate to Device > Password Profiles.

Verify Password Profiles weaker than the recommended minimum password complexity settings do not exist.

Remediation
^^^^^^^^^^^
Navigate to Device > Password Profiles.

Ensure Password Profiles weaker than the recommended minimum password complexity settings do not exist.


Default Value
^^^^^^^^^^^^^
Not configured 

References
^^^^^^^^^^
1. “PAN-OS Administrator's Guide 9.0 (English) - Best Practices for Securing Administrative Access” -
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/getting-started/best-practices-for-securing-administrative-access.html


1.4.1 Ensure 'Idle timeout' is less than or equal to 10 minutes for device management 
--------------------------------------------------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1 

Description
^^^^^^^^^^^
Set the Idle Timeout value for device management to 10 minutes or less to automatically close inactive sessions. 

Rationale
^^^^^^^^^
An unattended computer with an open administrative session to the device could allow an  

Audit
^^^^^
Navigate to Device > Setup > Management > Authentication Settings. Verify Idle Timeout is less than or equal to 10. 

Remediation
^^^^^^^^^^^
Navigate to Device > Setup > Management > Authentication Settings. Set Idle Timeout to less than or equal to 10.

Default Value
^^^^^^^^^^^^^
Not configured 

References
^^^^^^^^^^
1. “How to Change the Admin Session Timeout Value” -
https://live.paloaltonetworks.com/docs/DOC-5557

2. “PAN-OS Administrator's Guide 9.0 (English) - Device - Setup - Management” -
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-web-interface-help/device/device-setup-management#


1.4.2 Ensure 'Failed Attempts' and 'Lockout Time' for Authentication Profile are properly configured 
-----------------------------------------------------------------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1 

Description
^^^^^^^^^^^
Configure values for Failed Login Attempts and Account Lockout Time set to organization-defined values
(for example, 3 failed attempts and a 15 minute lockout time). Do not set Failed Attempts and Lockout
Time in the Authentication Settings section; any Failed Attempts or Lockout Time settings within the selected
Authentication Profile do not apply in the Authentication Settings section.

Rationale
^^^^^^^^^
From the other point of view, if lockout settings are configured in the Authentication Settings section it may be
possible for an attacker to continuously lock out all administrative accounts from accessing the device.
This potential situation indicates the importance of using named administrative accounts, instead of the default,
single shared "admin" account.

Audit
^^^^^
Navigate to Device > Authentication Profile.

Verify Failed Attempts is set a non-zero organization-defined value.

Verify Lockout Time is set to a non-zero organization-defined value.

Remediation
^^^^^^^^^^^
Navigate to Device > Authentication Profile.

Set Failed Attempts to the non-zero organization-defined value.

Set Lockout Time to the non-zero organization-defined value.


Default Value
^^^^^^^^^^^^^
Not configured    

References
^^^^^^^^^^
1. “PAN-OS Administrator's Guide 9.0 (English) - Device - Setup - Management” -
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-web-interface-help/device/device-setup-management#

2. “PAN-OS Administrator's Guide 9.0 (English) - Authentication Profile" -
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-web-interface-help/device/device-authentication-profile.html

Notes
^^^^^

Both values must be set. If either value is not set, account lockout does not occur.


1.5.1 Ensure 'V3' is selected for SNMP polling 
-----------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1 

Description
^^^^^^^^^^^
For SNMP polling, only SNMPv3 should be used. 

Rationale
^^^^^^^^^
SNMPv3 utilizes AES-128 encryption, message integrity, user authorization, and device authentication security
features. SNMPv2c does not provide these security features. If an SNMPv2c community string is intercepted or
otherwise obtained, an attacker could gain read access to the firewall. Note that SNMP write access is not possible.

Audit
^^^^^
Navigate to Device > Setup > Operations > Miscellaneous > SNMP Setup

Verify V3 is selected.

Remediation
^^^^^^^^^^^
Navigate to Device > Setup > Operations > Miscellaneous > SNMP Setup

Select V3. In order to be usable, the User and View sections of this dialog should also be completed.
These settings need to match the settings in the organization's NMS (Network Management System)

Impact
^^^^^^
Any clear-text administrative protocol (such as SNMPv2) can expose valuable information to any attacker that
is in a position to eavesdrop on that protocol.

Default Value
^^^^^^^^^^^^^
Not configured   

References
^^^^^^^^^^
1. “How to Setup SNMPv3 Polling” -
https://live.paloaltonetworks.com/t5/Configuration-Articles/How-to-Configure-SNMPv3-Polling/ta-p/58225


1.6.1 Ensure 'Verify Update Server Identity' is enabled 
--------------------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1 

Description
^^^^^^^^^^^
This setting determines whether or not the identity of the update server must be verified before performing an
update session. Note that if an SSL Forward Proxy is configured to intercept the update session, this option may
need to be disabled (because the SSL Certificate will not match).

Rationale
^^^^^^^^^
Verifying the update server identity before package download ensures the packages originate from a trusted source.
Without this, it is possible to receive and install an update from a malicious source.

Audit
^^^^^
Navigate to Device > Setup > Services > Services.

Verify that the Verify Update Server Identity box is checked.

Remediation
^^^^^^^^^^^
Navigate to Device > Setup > Services > Services.

Set the Verify Update Server Identity box to checked.

Impact
^^^^^^
This setting protects the device from an "evilgrade" attack, where a successful DNS attack can redirect the
firewall to an attacker-controlled update server, which can then serve a modified update.

Default Value
^^^^^^^^^^^^^
Not configured  

References
^^^^^^^^^^
1. “PAN-OS Administrator's Guide 9.0 (English) - Install Content Updates" -
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/software-and-content-updates/install-content-and-software-updates.html


1.6.2 Ensure redundant NTP servers are configured appropriately 
----------------------------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1 

Description
^^^^^^^^^^^
These settings enable use of primary and secondary NTP servers to provide redundancy in case of a failure
involving the primary NTP server.

Rationale
^^^^^^^^^
NTP enables the device to maintain an accurate time and date when receiving updates from a reliable NTP server.
Accurate timestamps are critical when correlating events with other systems, troubleshooting, or performing
investigative work. Logs and certain cryptographic functions, such as those utilizing certificates, rely on
accurate time and date parameters. In addition, rules referencing a Schedule object will not function as intended
if the device’s time and date are incorrect.

For additional security, authenticated NTP can be utilized. If Symmetric Key authentication is selected,
only SHA1 should be used, as MD5 is considered severely compromised.

Most organizations will maintain a pair of internal NTP servers for all internal time services.
These servers will either be self-contained atomic clocks, or will collect time from a known reliable source
(often GPS or a well-known internet server pool will be used).

Audit
^^^^^
Navigate to Device > Setup > Services > Services.

Verify Primary NTP Server Address is set appropriately.

Verify Secondary NTP Server Address is set appropriately.

Remediation
^^^^^^^^^^^
Navigate to Device > Setup > Services > Services.

Set Primary NTP Server Address appropriately.

Set Secondary NTP Server Address appropriately.


Default Value
^^^^^^^^^^^^^
Not configured  

References
^^^^^^^^^^
1. “The NIST Authenticated NTP Service” -
http://www.nist.gov/pml/div688/grp40/authntp.cfm

2. “PAN-OS Administrator's Guide 9.0 (English) - Global Services Settings" -
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-web-interface-help/device/device-setup-services/global-services-settings.html

3. "How to Configure Authenticated NTP" -
https://live.paloaltonetworks.com/t5/Configuration-Articles/How-to-Configure-Authenticated-NTP/ta-p/54495


1.6.3 Ensure that the Certificate Securing Remote Access VPNs is Valid 
-----------------------------------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Not Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1, Level 2

Description
^^^^^^^^^^^
The Certificate used to secure Remote Access VPNs should satisfy the following criteria:

It should be a valid certificate from a trusted source. In almost cases this means a trusted Public Certificate
Authority, as in most cases remote access VPN users will not have access to any Private Certificate
Authorities for Certificate validation.

The certificate should have a valid date. It should not have a "to" date in the past (it should not be expired),
and should not have a "from" date in the future.

The key length used to encrypt the certificate should be 2048 bits or more.

The hash used to sign the certificate should be SHA-2 or better.

When the Certificate is applied, the TLS version should be

Rationale
^^^^^^^^^
If presented with a certificate error, the end user in most cases will not be able to tell if their session
is using a self-signed or expired certificate, or if their session is being eavesdropped on or injected into
by a "Man in the Middle" attack. This means that self-signed or invalid certificates should never be used for
VPN connections.

Audit
^^^^^
Verify that the certificate being used to secure the VPN meets the criteria listed above:

Navigate to Device > Certificate Management > Certificates

Ensure that a valid certificate is applied to the HTTPS portal:

Navigate to Network > GlobalProtect > Portals > Portal Configuration >
(Select the Portal being assessed) > Authentication > SSL/TLS Profile

Ensure that a valid certificate is applied to the GlobalProtect Gateway:

Navigate to Network > GlobalProtect > Gateways > (Select the Gateway being Assessed) > Authentication >
SSL/TLS Service Profile Ensure that the correct Certificate is selected.

Ensure that the Minimum TLS version is configured to be 1.1 or higher (TLSv1.2 is recommended).

Remediation
^^^^^^^^^^^
Create a CSR and install a certificate from a public CA (Certificate Authority) here:

Navigate to Device > Certificate Management > Certificates

Apply a valid certificate to the HTTPS portal:

Navigate to Network > GlobalProtect > Portals > Portal Configuration > Authentication > SSL/TLS Profile

Apply a valid certificate to the GlobalProtect Gateway:

Navigate to Network > GlobalProtect > Gateways > Authentication > SSL/TLS Service Profile

Configure the Service Profile to use the correct certificate

Ensure that the Minimum TLS version is set to 1.1 or 1.2 (1.2 is recommended).

Impact
^^^^^^
Not using a trusted Certificate, issued by a trusted Public Certificate Authority means that clients
establishing VPN sessions will always see an error indicating an untrusted Certificate.
This means that they will have no method of validating if their VPN session is being hijacked by a
"Monkey in the Middle" (MitM) attack. It also "trains" them to bypass certificate warnings for other services,
making MitM attacks easier for those other services as well.

Default Value
^^^^^^^^^^^^^
Not configured 

References
^^^^^^^^^^

1. “PAN-OS Administrator's Guide 9.0 (English) - GlobalProtect Certificate Best Practices" -
https://docs.paloaltonetworks.com/globalprotect/9-0/globalprotect-admin/get-started/enable-ssl-between-globalprotect-components/globalprotect-certificate-best-practices.html

2. “PAN-OS Administrator's Guide 9.0 (English) - Deploy Server Certificates to the GlobalProtect Components" -
https://docs.paloaltonetworks.com/globalprotect/9-0/globalprotect-admin/get-started/enable-ssl-between-globalprotect-components/deploy-server-certificates-to-the-globalprotect-components.html#


2.1 Ensure that IP addresses are mapped to usernames 
-----------------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 2 

Description
^^^^^^^^^^^
Configure appropriate settings to map IP addresses to usernames. Mapping userids to IP addresses is what permits
the firewall to create rules based on userids and groups rather than IP addresses and subnets, as well as log events
by userids rather than IP addresses or DNS names. The specifics of how to achieve IP-to-username mapping is highly
dependent on the environment. It can be enabled by integrating the firewall with a domain controller,
Exchange server, captive portal, Terminal Server, User-ID Agent, XML API, or syslog data from a variety of devices.

Rationale
^^^^^^^^^
Understanding which user is involved in a security incident allows appropriate personnel to move quickly between
the detection and reaction phases of incident response. In environments with either short DHCP lease times, or
where users may move frequently between systems, the ability to analyze or report, or alert on events based on
user accounts or user groups is a tremendous advantage. For forensics tasks when DHCP lease information may
not be available, the Source User information may be the only way to tie together related data.

Audit
^^^^^
To validate if this recommendation has been met, look at the Source User column in the URL Filtering or Traffic logs
(Monitor > Logs > URL Filtering and Logs > Traffic Logs, respectively.) User traffic originating
from a trusted zone should identify a username.

Remediation
^^^^^^^^^^^
To Set User-ID Agents:

Navigate to Device > User Identification > User-ID Agents

Set the Name, IP Address and Port of the User-ID Agent`

Enable User Identification for each monitored zone that will have user accounts:

Navigate to Network > Zone, for each relevant zone enable User Identification

To Set Terminal Services Agents: Navigate to Device > Terminal Services Agents

Set the Name, IP Address and Port of the Terminal Services Agent

Enable User Identification for each monitored zone that will have Terminal Servers:

Navigate to Network > Zone, enable User Identification


References
^^^^^^^^^^
1. “Best Practices for Securing User-ID Deployments” -
https://live.paloaltonetworks.com/docs/DOC-7912

2. “How to Configure Group Mapping settings?” -
https://live.paloaltonetworks.com/docs/DOC-4994

3. “PAN-OS Administrator's Guide 9.0 (English) - User-ID” -
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/user-id

4. https://paloaltonetworks.com/content/dam/paloaltonetworks-com/en_US/assets/pdf/tech-briefs/techbrief-user-id.pdf

2.2 Ensure that WMI probing is disabled 
----------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 2 

Description
^^^^^^^^^^^
Disable WMI probing if it is not required for User-ID functionality in the environment. 

Rationale
^^^^^^^^^
WMI probing normally requires a domain administrator account. A malicious user could capture the encrypted
password hash for offline cracking or relayed authentication attacks. Relying on other forms of user identification,
such as using UserID Agents or security log monitoring, mitigates this risk. In addition, it is easy to
mis-configure this feature such that it is enabled on untrusted interfaces. This can result in a domain administrator
account and the associated password hash being sent to untrusted hosts on the internet, where malicious users can
then capture that hash for offline cracking.

Audit
^^^^^
Navigate to Device > User Identification > User Mapping > Palo Alto Networks User ID Agent Setup.

Verify that Enable Probing is not checked.

Remediation
^^^^^^^^^^^
Navigate to Device > User Identification > User Mapping > Palo Alto Networks User ID Agent Setup.

Set Enable Probing so it is unchecked.

Impact
^^^^^^
While this removes the exposure of having the WMI user account password being compromised, it also reduces the
effectiveness of user identification during operation of the firewall (applying rules and policies).
This trade-off should be weighed carefully for all installations.

Default Value
^^^^^^^^^^^^^
Not configured  

References
^^^^^^^^^^
1. “R7-2014-16: Palo Alto Networks User-ID Credential Exposure” -
https://blog.rapid7.com/2014/10/14/palo-alto-networks-userid-credential-exposure/

2. “Best Practices for Securing User-ID Deployments” -
https://live.paloaltonetworks.com/docs/DOC-7912

3. “PAN-OS Administrator's Guide 9.0 (English) - Client Probing" -
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/user-id/user-id-concepts/user-mapping/client-probing

2.3 Ensure that User-ID is only enabled for internal trusted interfaces 
------------------------------------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1 

Description
^^^^^^^^^^^
Only enable the User-ID option for interfaces that are both internal and trusted. There is rarely a legitimate
need to allow WMI probing (or any user-id identification) on an untrusted interface. The exception to this is
identification of remote-access VPN users, who are identified as they connect.

Rationale
^^^^^^^^^
PAN released a customer advisory in October of 2014 warning of WMI probing on untrusted interfaces with User-ID
enabled. This can result in theft of the password hash for the account used in WMI probing.

Audit
^^^^^
Navigate to Network > Network Profiles > Interface Management.

Verify that User-ID is only enabled for interfaces that are both internal and trusted.

Remediation
^^^^^^^^^^^
Navigate to Network > Network Profiles > Interface Management.

Set User-ID to be checked only for interfaces that are both internal and trusted; uncheck it for all other interfaces.

Impact
^^^^^^
If WMI probing is enabled without limiting the scope, internet hosts that are sources or destinations of traffic
will be probed, and the password hash of the configured Domain Admin account can be captured by an outside
attacker on such a host.

Default Value
^^^^^^^^^^^^^
By default WMI probing and all User-ID functions are disabled.    

References
^^^^^^^^^^
1. “Customer advisory: Security Impact of User-ID Misconfiguration” -
https://live.paloaltonetworks.com/docs/DOC-8125

2. “R7-2014-16: Palo Alto Networks User-ID Credential Exposure” -
https://blog.rapid7.com/2014/10/14/palo-alto-networks-userid-credential-exposure/

3. “Best Practices for Securing User-ID Deployments” -
https://live.paloaltonetworks.com/docs/DOC-7912

4. “User-ID Best Practices” - https://live.paloaltonetworks.com/docs/DOC-6591

5. “PAN-OS Administrator's Guide 9.0 (English) - Client Probing" -
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/user-id/user-id-concepts/user-mapping/client-probing


2.4 Ensure that 'Include/Exclude Networks' is used if User-ID is enabled 
-------------------------------------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1 

Description
^^^^^^^^^^^
If User-ID is configured, use the Include/Exclude Networks section to limit the User-ID scope to operate only on
trusted networks. There is rarely a legitimate need to allow WMI probing or other User identification on an
untrusted network.

Rationale
^^^^^^^^^
The Include/Exclude Networks feature allow users to configure boundaries for the User-ID service. By using the
feature to limit User-ID probing to only trusted internal networks, the risks of privileged information disclosure
through sent probes can be reduced. Note that if an entry appears in the Include/Exclude Networks section, an
implicit exclude-all-networks policy will take effect for all other networks.

Audit
^^^^^
Navigate to Device > User Identification > User Mapping > Include/Exclude Networks.

Verify that all trusted internal networks have a Discovery value of Include.

Verify that all untrusted external networks have a Discovery value of Exclude.

Note that any value in the trusted networks list implies that all other networks are untrusted.

Remediation
^^^^^^^^^^^
Navigate to Device > User Identification > User Mapping > Include/Exclude Networks.

Set all trusted internal networks to have a Discovery value of Include.

Set all untrusted external networks to have a Discovery value of Exclude.

Note that any value in the trusted networks list implies that all other networks are untrusted.

Impact
^^^^^^
Not restricting the networks subject to User Identification means that the administrative credentials
(userid and password hash) used for this task will transit untrusted networks, or be sent to untrusted hosts.
Capturing these credentials exposes them to offline cracking attacks.

Default Value
^^^^^^^^^^^^^
Not configured 

References
^^^^^^^^^^
1. Best Practices for Securing User-ID Deployments -
https://live.paloaltonetworks.com/docs/DOC-7912


2.5 Ensure that the User-ID Agent has minimal permissions if User-ID is enabled 
--------------------------------------------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1 

Description
^^^^^^^^^^^
If the integrated (on-device) User-ID Agent is utilized, the Active Directory account for the agent should only
be a member of the Event Log Readers group, Distributed COM Users group, and Domain Users group.
If the Windows User-ID agent is utilized, the Active Directory account for the agent should only be a member of the
Event Log Readers group, Server Operators group, and Domain Users group.

Rationale
^^^^^^^^^
As a principle of least privilege, user accounts should have only minimum necessary permissions.
If an attacker compromises a User-ID service account with domain admin rights, the organization is at far greater
risk than if the service account were only granted minimum rights.

Audit
^^^^^
Navigate to Active Directory Users and Computers for the Active Directory under consideration.

Verify that the service account for the User-ID agent is not a member of any groups other
than Event Log Readers, Distributed COM Users, and Domain Users (for the integrated, on-device User-ID agent) or
Event Log Readers, Server Operators, and Domain Users (for the Windows User-ID agent.)

Remediation
^^^^^^^^^^^
Navigate to Active Directory Users and Computers. Set the service account for the User-ID agent
so that it is only a member of the Event Log Readers, Distributed COM Users, and Domain Users
(for the integrated, on-device User-ID agent) or the Event Log Readers, Server Operators, and Domain Users
groups (for the Windows User-ID agent.)

Impact
^^^^^^
Using accounts with full administrative privileges when those rights are not required is always a bad idea.
This is particularly true for service accounts of this type, which in many organizations do not see strong
passwords or frequent password changes. In addition, service passwords are stored in the Windows Registry,
and are recoverable with the user of appropriate malicious tools. The principal of least privilege means that
any compromised accounts of this type have less value to an attacker, and expose fewer assets based on their rights.

Default Value
^^^^^^^^^^^^^
Not configured 

References
^^^^^^^^^^
1. “Best Practices for Securing User-ID Deployments” -
https://live.paloaltonetworks.com/docs/DOC-7912

2. “User-ID Best Practices” - https://live.paloaltonetworks.com/docs/DOC-6591

3. “PAN-OS Administrator's Guide 9.0 (English) - Configure User Mapping Using the Windows User-ID Agent” -
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/user-id/map-ip-addresses-to-users/configure-user-mapping-using-the-windows-user-id-agent.html

4. “PAN-OS Administrator's Guide 9.0 (English) - Configure User Mapping Using the PAN-OS Integrated User-ID Agent” -
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/user-id/map-ip-addresses-to-users/configure-user-mapping-using-the-pan-os-integrated-user-id-agent.html


2.6 Ensure that the User-ID service account does not have interactive logon rights 
-----------------------------------------------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1 

Description
^^^^^^^^^^^
Restrict the User-ID service account from interactively logging on to systems in the Active Directory domain. 

Rationale
^^^^^^^^^
In the event of a compromised User-ID service account, restricting interactive logins forbids the attacker from
utilizing services such as RDP against computers in the Active Directory domain of the organization. This reduces
the impact of a User-ID service account compromise.

Audit
^^^^^
Navigate to Active Directory Group Policies. Verify that Group Policies restricts the interactive logon privilege for
the User-ID service account. or Navigate to Active Directory Managed Service Accounts. Verify that Managed Service
Accounts restricts the interactive logon privilege for the User-ID service account.

Remediation
^^^^^^^^^^^
Navigate to Active Directory Group Policies.

Set Group Policies to restrict the interactive logon privilege for the User-ID service account.

or Navigate to Active Directory Managed Service Accounts.

Set Managed Service Accounts to restrict the interactive logon privilege for the User-ID service account.

Default Value
^^^^^^^^^^^^^
Not configured 

References
^^^^^^^^^^
1. “Best Practices for Securing User-ID Deployments” -
https://live.paloaltonetworks.com/docs/DOC-7912

2. “PAN-OS Administrator's Guide 9.0 (English) - Configure User Mapping Using the Windows User-ID Agent” -
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/user-id/map-ip-addresses-to-users/configure-user-mapping-using-the-windows-user-id-agent.html

3. “PAN-OS Administrator's Guide 9.0 (English) - Configure User Mapping Using the PAN-OS Integrated User-ID Agent” -
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/user-id/map-ip-addresses-to-users/configure-user-mapping-using-the-pan-os-integrated-user-id-agent.html

4. “User-ID Best Practices” -
https://live.paloaltonetworks.com/docs/DOC-6591



2.7 Ensure remote access capabilities for the User-ID service account are forbidden. 
-------------------------------------------------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Not Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1 

Description
^^^^^^^^^^^
Restrict the User-This capability could be made available through a variety of technologies, such as VPN,
Citrix GoToMyPC, or TeamViewer. Remote services that integrate authentication with the -ID service account to
gain remote access.

Rationale
^^^^^^^^^
In the event of a compromised User-a service account compromise. 

Audit
^^^^^
Auditing is operating-system dependent. For instance, in Windows Active Directory, this account should not be
included in any group that grants the account access to VPN or Wireless access. In addition, domain administrative accounts should not have remote desktop (RDP) access to all domain member workstations.

Remediation
^^^^^^^^^^^
Remove this account from all groups that might grant remote access to the network, or to any network services or
hosts. Remediation is operating-system dependent. For instance, in Windows Active Directory, this account should be
removed from any group that grants the account access to VPN or Wireless access. In addition, domain administrative
accounts by default have remote desktop (RDP) access to all domain member workstations - this should be explicitly
denied for this account.


Default Value
^^^^^^^^^^^^^
Not configured   

References
^^^^^^^^^^
1. “Best Practices for Securing User-ID Deployments” -
https://live.paloaltonetworks.com/docs/DOC-7912

2. “User-ID Best Practices” -
https://live.paloaltonetworks.com/docs/DOC-6591

3. “PAN-OS Administrator's Guide 9.0 (English) - Configure User Mapping Using the Windows User-ID Agent” -
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/user-id/map-ip-addresses-to-users/configure-user-mapping-using-the-windows-user-id-agent.html

4. “PAN-OS Administrator's Guide 9.0 (English) - Configure User Mapping Using the PAN-OS Integrated User-ID Agent” -
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/user-id/map-ip-addresses-to-users/configure-user-mapping-using-the-pan-os-integrated-user-id-agent.html

2.8 Ensure that security policies restrict User-ID Agent traffic from crossing into untrusted zones 
----------------------------------------------------------------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1 

Description
^^^^^^^^^^^
Create security policies to deny Palo Alto User-ID traffic originating from the interface configured for the UID
Agent service that are destined to any untrusted zone.

Rationale
^^^^^^^^^
If User-ID and WMI probes are sent to untrusted zones, the risk of privileged information disclosure exists.
The information disclosed can include the User-ID Agent service account name, domain name, and encrypted password
hashes sent in User-ID and WMI probes. To prevent this exposure, msrpc traffic originating from the firewall to
untrusted networks should be explicitly denied. This security policy should be in effect even for environments not
currently using WMI probing to help guard against possible probe misconfigurations in the future. This setting is a
"fail safe" to prevent exposure of this information if any of the other WMI User control settings are misconfigured.

Audit
^^^^^
Navigate to Device > Setup > Services > Services Features > Service Route Configuration > Customize.

Click on the protocol in use (IPv4and/or IPv6). Click UID Agent.

Click on the address object for the UID Agent's IP address.

Verify SOURCE/NAME is set to 'Deny msrpc to untrusted'.

Verify SOURCE/ZONE is set to 'INSIDE'.

Verify SOURCE/Address is set to the Address object for the UID Agent.

Verify DESTINATION/ZONE is set to 'GUEST' and 'OUTSIDE'.

Verify DESTINATION/Address is set to 'any'.

Verify DESTINATION/Application is set to 'msrpc'.

Verify DESTINATION/Service is set to 'application-default'.

Verify DESTINATION/Action is set to 'Block' (red circle with diagonal line).

Remediation
^^^^^^^^^^^
Navigate to Device > Setup > Services > Services Features > Service Route Configuration > Customize.

Click on the protocol in use (IPv4and/or IPv6).

Click UID Agent.

Click on the address object for the UID Agent's IP address.

Set SOURCE/NAME to 'Deny msrpc to untrusted'.

Set SOURCE/ZONE to 'INSIDE'.

Set SOURCE/Address to the Address object for the UID Agent.

Set DESTINATION/ZONE to 'GUEST' and 'OUTSIDE'.

Set DESTINATION/Address to 'any'. Set DESTINATION/Application to 'msrpc'.

Set DESTINATION/Service to 'application-default'.

Set DESTINATION/Action to 'Block' (red circle with diagonal line).



References
^^^^^^^^^^
1. “Best Practices for Securing User-ID Deployments” -
https://live.paloaltonetworks.com/docs/DOC-7912

2. “User-ID Best Practices” -
https://live.paloaltonetworks.com/docs/DOC-6591

3. “PAN-OS Administrator's Guide 9.0 (English) - Configure User Mapping Using the Windows User-ID Agent” -
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/user-id/map-ip-addresses-to-users/configure-user-mapping-using-the-windows-user-id-agent.html

4. “PAN-OS Administrator's Guide 9.0 (English) - Configure User Mapping Using the PAN-OS Integrated User-ID Agent” -
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/user-id/map-ip-addresses-to-users/configure-user-mapping-using-the-pan-os-integrated-user-id-agent.html

3.1 Ensure a fully-synchronized High Availability peer is configured 
---------------------------------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1 

Description
^^^^^^^^^^^
Ensure a High Availability peer is fully synchronized and in a passive or active state. 

Rationale
^^^^^^^^^
To ensure availability of both the firewall and the resources it protects, a High Availability peer is required.
In the event a single firewall fails, or when maintenance such as a software update is required, the HA peer can
be used to automatically fail over session states and maintain overall availability

Audit
^^^^^
Navigate to Device > High Availability > General.

In the General. >Data Link (HA2) section, verify that the correct interface is selected.

Verify the desired protocol (IPv4 or IPv6) is selected.

Verify the correct Transport is selected.

Verify the Enable Session Synchronization box is checked.

Remediation
^^^^^^^^^^^
Navigate to Device > High Availability > General.

Click General. Click Data Link (HA2).

Select the correct interface.

Select the desired protocol (IPv4 or IPv6).

Select the correct Transport.

Set the Enable Session Synchronization box to be checked.

Choose Save Configuration.

Impact
^^^^^^
Not configuring High Availability (HA) correctly directly impacts the Availability of the system. With HA in
place, standard maintenance such as OS updates, network and power cabling can be accomplished with no outage
or a minimum impact.

Default Value
^^^^^^^^^^^^^
Not Configured  

References
^^^^^^^^^^
1. “PAN-OS Administrator's Guide 9.0 (English) - High Availability" -
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-web-interface-help/device/device-high-availability.html

3.2 Ensure 'High Availability' requires Link Monitoring and/or Path Monitoring 
-------------------------------------------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1 

Description
^^^^^^^^^^^
Configure Link Monitoring and/or Path Monitoring under High Availability options. If Link Monitoring is utilized,
all links critical to traffic flow should be monitored.

Rationale
^^^^^^^^^
If Link or Path Monitoring is not enabled, the standby router will not automatically take over as active if a
critical link fails on the active firewall. Services through the firewall could become unavailable as a result.

Audit
^^^^^
To verify Link Monitoring from GUI: Navigate to Device > High Availability > Link and Path Monitoring.

In the Link Monitoring section, verify the correct interfaces are in the Link Group and Group Failure Conditions

Under the Link Monitoring section, verify Failure Condition is set to Any.

Verify Enabled button is checked.

To verify Path Monitoring from GUI:

Navigate to Device > High Availability > Link and Path Monitoring.

In the Path Monitoring section, verify Option is set correctly.

Verify Failure Condition is set to Any.

Verify Name, IP Address, Failure Condition is set correctly.

Verify Default setting is set to Any.

Verify Enabled button is checked.

Remediation
^^^^^^^^^^^
To set Link Monitoring from GUI: Navigate to Device > High Availability > Link and Path Monitoring.

Click Link Monitoring.

Set the correct interfaces to the Link Group and Group Failure Conditions.

Click Link Monitoring.

Set Failure Condition to Any.

Check Enabled button.

To set Path Monitoring from GUI:

Navigate to Device > High Availability > Link and Path Monitoring.

Click Path Monitoring.

Set Option correctly.

Set Failure Condition to Any.

Set Name, IP Address, Failure Condition correctly.

Set Default setting to Any.

Check Enabled button.

Impact
^^^^^^
Not configuring High Availability (HA) correctly directly impacts the Availability of the system. With HA in place,
standard maintenance such as OS updates, network and power cabling can be accomplished with no outage or a minimum
impact. Without Link and Path monitoring in particular, failover will only occur when the primary device fails
completely. Link and path monitoring permits failover if a critical interface loses link (either due to cabling
or an upstream switch failover), or if a route or path fails (indicating an upstream issue that affects local Layer 3).

Default Value
^^^^^^^^^^^^^
Not Configured 

References
^^^^^^^^^^
1. “PAN-OS Administrator's Guide 9.0 (English) - High Availability" -
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-web-interface-help/device/device-high-availability.html

3.3 Ensure 'Passive Link State' and 'Preemptive' are configured appropriately 
------------------------------------------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1 

Description
^^^^^^^^^^^
Set the Passive Link State to auto, and uncheck the Preemptive option to disable it. 

Rationale
^^^^^^^^^
Simultaneously enabling the 'Preemptive' option and setting the 'Passive Link State' option to 'Shutdown' could
cause a 'preemptive loop' if Link and Path Monitoring are both configured. This will negatively impact the
availability of the firewall and network services, should a monitored failure occur.

Audit
^^^^^
To ensure Active/Passive Settings are configured correctly:

Navigate to Device > High Availability > General > Active/Passive Settings.

Verify Passive Link State is set to auto.

To ensure Election Settings are configured correctly:

Navigate to Device > High Availability > Election Settings.

Verify Preemptive is disabled.

Remediation
^^^^^^^^^^^
To set Active/Passive Settings correctly:

Navigate to Device > High Availability > General > Active/Passive Settings.

Set Passive Link State to auto.

To set Election Settings correctly:

Navigate to Device > High Availability > Election Settings.

Set Preemptive to be disabled.

Impact
^^^^^^
Incorrectly configuring this setting will adversely affect availability, rather than positively affect it.   

Default Value
^^^^^^^^^^^^^
Not Configured 

References
^^^^^^^^^^
1. “PAN-OS Administrator's Guide 9.0 (English) - High Availability" -
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-web-interface-help/device/device-high-availability.html

4.1 Ensure 'Antivirus Update Schedule' is set to download and install updates hourly 
-------------------------------------------------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1 

Description
^^^^^^^^^^^
Set Antivirus Update Schedule to download and install updates hourly. 

Rationale
^^^^^^^^^
New antivirus definitions may be released at any time. With an hourly update schedule, the firewall can ensure
threats with new definitions are quickly mitigated. A daily update schedule could leave an organization vulnerable
to a known virus for nearly 24 hours, in a worst-case scenario. Setting an appropriate threshold value reduces
the risk of a bad definition file negatively affecting traffic.

Audit
^^^^^
Navigate to Device > Dynamic Updates > Antivirus Update Schedule.

Verify that Action is set to Download and Install.

Verify that Recurrence is set to Hourly.

Remediation
^^^^^^^^^^^
Navigate to Device > Dynamic Updates > Antivirus Update Schedule.

Set Action to Download and Install.

Set Recurrence to Hourly.

Default Value
^^^^^^^^^^^^^
Not Configured       

References
^^^^^^^^^^
1. “Tips for Managing Content Updates” -
https://live.paloaltonetworks.com/docs/DOC-1578

2. “PAN-OS Administrator's Guide 9.0 (English) -Dynamic Content Updates" -
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/software-and-content-updates/dynamic-content-updates.html

3. “PAN-OS Administrator's Guide 9.0 (English) - Install Content Updates" -
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/software-and-content-updates/install-content-and-software-updates.html


4.2 Ensure 'Applications and Threats Update Schedule' is set to download and install updates at daily or shorter intervals 
---------------------------------------------------------------------------------------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1 

Description
^^^^^^^^^^^
Set the Applications and Threats Update Schedule to download and install updates at daily or shorter intervals. 

Rationale
^^^^^^^^^
New Applications and Threats file versions may be released at any time. With a frequent update schedule, the firewall
can ensure threats with new signatures are quickly mitigated, and the latest application signatures are applied.

Audit
^^^^^
Navigate to Device > Dynamic Updates > Application and Threats Update Schedule. Verify that Action is set to
Download and Install. Verify that Recurrence is set to Daily, Hourly or Every 30 Minutes

Remediation
^^^^^^^^^^^
Navigate to Device > Dynamic Updates > Application and Threats Update Schedule.

Set Action to Download and Install.

Set Recurrence to Daily, Hourly or Every 30 Minutes


Default Value
^^^^^^^^^^^^^
This setting is by default set to Weekly. 

References
^^^^^^^^^^
1. “Tips for Managing Content Updates” -
https://live.paloaltonetworks.com/docs/DOC-1578

2. “PAN-OS Administrator's Guide 9.0 (English) -Dynamic Content Updates" -
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/software-and-content-updates/dynamic-content-updates.html

3. “PAN-OS Administrator's Guide 9.0 (English) - Install Content Updates" -
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/software-and-content-updates/install-content-and-software-updates.html

5.1 Ensure that WildFire file size upload limits are maximized 
---------------------------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1 

Description
^^^^^^^^^^^
Increase WildFire file size limits to the maximum file size supported by the environment.
An organization with bandwidth constraints or heavy usage of unique files under a supported file type may require
lower settings. The recommendations account for the CPU load on smaller platforms. If an organization consistently has
CPU to spare, it's recommended to set some or all of these values to the maximum.

Rationale
^^^^^^^^^
Increasing file size limits allows the devices to forward more files for WildFire analysis. This increases the
chances of identifying, and later preventing, threats in larger files. The default values are configured for files
small enough that the majority of files are not assessed by Wildfire.

Audit
^^^^^
Navigate to Device > Setup > WildFire.

Navigate to the General Settings sections.

Verify the maximum size for each file type are larger than the defaults, to a size that is as large enough to
account for "large" files, but not large enough to affect performance of the hardware.

Remediation
^^^^^^^^^^^
Navigate to Device > Setup > WildFire.

Click the General Settings edit icon.

Set the maximum size for each file type are larger than the defaults,
to a size that is as large enough to account for "large" files, but not large enough to affect performance of the
hardware.

In PAN-OS 9.x, the default file sizes for WildFire are:

    * pe (Portable Executable) - 16MB
    * apk (Android Application)- 10MB
    * pdf (Portable Document Format) - 3072KB
    * ms-office (Microsoft Office)  16384KB
    * jar (Packaged Java class file)  5MB
    * flash (Adobe Flash)  5MB
    * MacOSX (DMG/MAC-APP/MACH-O PKG files)  10MB
    * archive (RAR and 7z files)  50MB
    * linux (ELF files)  50MB
    * script (JScript, VBScript, PowerShell, and Shell Script)- 20KB

In PAN-OS 9.x, the maximum file sizes for Wildfire are:

    * pe (Portable Executable) - 50MB
    * apk (Android Application)- 50MB
    * pdf (Portable Document Format) - 51200KB
    * ms-office (Microsoft Office)  51200KB
    * jar (Packaged Java class file)  20MB
    * flash (Adobe Flash)  10MB  MacOSX (DMG/MAC-APP/MACH-O PKG files)  50MB
    * archive (RAR and 7z files)  50MB  linux (ELF files)  50MB
    * script (JScript, VBScript, PowerShell, and Shell Script)- 4096KB

Impact
^^^^^^
With the default values known, an attacker has only to send an infected file slightly over the "maximum" size
for that filetype to evade detection at the perimeter. Many of the values are significantly lower than is typical
for each file size.

Default Value
^^^^^^^^^^^^^
In PAN-OS 9.x, the default file sizes for WildFire are:

    * pe (Portable Executable) - 16MB
    * apk (Android Application)- 10MB
    * pdf (Portable Document Format) - 3072KB
    * ms-office (Microsoft Office)  16384KB
    * jar (Packaged Java class file)  5MB
    * flash (Adobe Flash)  5MB
    * MacOSX (DMG/MAC-APP/MACH-O PKG files)  10MB
    * archive (RAR and 7z files)  50MB
    * linux (ELF files)  50MB
    * script (JScript, VBScript, PowerShell, and Shell Script)- 20KB


References
^^^^^^^^^^
1. “Wildfire Administrator's Guide 9.0 (English) - Increased Wildfire File Forwarding Capacity" -
https://docs.paloaltonetworks.com/wildfire/u-v/wildfire-whats-new/wildfire-features-in-panos-90/increased-wildfire-file-forwarding-capacity

2. “How to Configure WildFire” -
https://live.paloaltonetworks.com/docs/DOC-3252

3. “Wildfire Administrator's Guide 9.0 (English) - Wildfire Best Practices" -
https://docs.paloaltonetworks.com/wildfire/9-0/wildfire-admin/wildfire-deployment-best-practices/wildfire-best-practices.html#

4. “Wildfire Administrator's Guide 9.0 (English) - Forward Files for Wildfire Analysis" -
https://docs.paloaltonetworks.com/wildfire/9-0/wildfire-admin/submit-files-for-wildfire-analysis/forward-files-for-wildfire-analysis.html#

5.2 Ensure forwarding is enabled for all applications and file types in WildFire file blocking profiles 
--------------------------------------------------------------------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1 

Description
^^^^^^^^^^^
Set Applications and File Types fields to any in WildFire file blocking profiles. With a WildFire license,
seven file types are supported, while only PE (Portable Executable) files are supported without a license.
For the "web browsing" application, the action "continue" can be selected. This still forwards the file to the
Wildfire service, but also presents the end user with a confirmation message before they receive the file.
Selecting "continue" for any other application will block the file (because the end user will not see the prompt).
If there is a "continue" rule, there should still be an "any traffic / any application / forward" rule
after that in the list.

Rationale
^^^^^^^^^
Selecting 'Any' application and file type ensures WildFire is analyzing as many files as possible. 

Audit
^^^^^
Navigate to Objects > Security Profiles > File Blocking.

Verify an appropriate rule exists with Applications set to any, File Type set to any, and Action set to forward.

Remediation
^^^^^^^^^^^
Navigate to Objects > Security Profiles > File Blocking.

Set a rule so that Applications is set to any, File Type is set to any, and Action is set to forward.


Default Value
^^^^^^^^^^^^^
Predefined Security Profiles exist for "basic" and "strict" File Blocking.     

References
^^^^^^^^^^
1. ““Wildfire Administrator's Guide 9.0 (English) -WildFire Best Practices” -
https://docs.paloaltonetworks.com/wildfire/9-0/wildfire-admin/wildfire-deployment-best-practices/wildfire-best-practices.html#


5.3 Ensure a WildFire Analysis profile is enabled for all security policies 
----------------------------------------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1 

Description
^^^^^^^^^^^
Ensure that all files traversing the firewall are inspected by WildFire by setting a Wildfire file blocking
profile on all security policies.

Rationale
^^^^^^^^^
Traffic matching security policies that do not include a WildFire file blocking profile will not utilize WildFire for
file analysis. Wildfire analysis is one of the key security measures available on this platform. Without Wildfire
analysis enabled, inbound malware can only be analyzed by signature - which industry wide is roughly 40-60% effective.
In a targeted attack, the success of signature-based-only analysis drops even further.

Audit
^^^^^
To verify WildFire Analysis Profile:

Navigate to Objects > Security Profiles > WildFire Analysis Profile

verify that a profile exists.

To verify File Blocking Rules:

For each Security Policy were the action is set to Allow, edit the Rule and
navigate to Actions > Profile Setting.

Ensure that the WildFire Analysis is set to Allow and verify that a profile is set.

If Group Profiles are used:  Navigate to Policies > Security

For each Security Policy were the action is set to Allow, edit the Rule and navigate to Actions > Profile Setting.

Ensure that the Profile Type is set to Group.

Navigate to Objects > Security Profile Groups.

Open the Security Profile Group used above, and ensure that the Wildfire Analysis Profile is set.

Remediation
^^^^^^^^^^^
To Set File Blocking Profile:

Navigate to Objects > Security Profiles > WildFire Analysis Profile.

Create a WildFire profile that has 'Application Any', 'File Types Any', and 'Direction Both'

To Set WildFire Analysis Rules:

Navigate to Policies > Security.  For each Security Policy Rule where the action is "Allow",
Navigate to Actions > Profile Setting > WildFire Analysis and set a WildFire Analysis profile.

Group Profiles can also be used. To take this approach:

Navigate to Objects > Security Profile Groups. Create a Security Profile Group, and ensure that (among other settings)
the Wildfire Analysis Profile is set to the created profile.

Navigate to Policies > Security. For each Security Policy Rule where the action is "Allow",
Navigate to Actions > Profile Setting. Modify the Profile Type to Group,
and set the Group Profile to the created Security Profile Group.


Default Value
^^^^^^^^^^^^^
Not Configured 

References
^^^^^^^^^^
1. “Wildfire Administrator's Guide 9.0 (English)" -
https://docs.paloaltonetworks.com/wildfire/9-0/wildfire-admin.html


5.4 Ensure forwarding of decrypted content to WildFire is enabled 
------------------------------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1 

Description
^^^^^^^^^^^
Allow the firewall to forward decrypted content to WildFire. Note that SSL Forward-Proxy must also be enabled and
configured for this setting to take effect on inside-to-outside traffic flows.

Rationale
^^^^^^^^^
As encrypted Internet traffic continues to proliferate, WildFire becomes less effective unless it is allowed to
act on decrypted content. For example, if a user downloads a malicious pdf over SSL, WildFire can only provide
analysis if 1) the session is decrypted by the firewall and 2) forwarding of decrypted content is enabled.
In today's internet, roughly 70-80% of all user traffic is encrypted. If Wildfire is not configured to analyze
encrypted content, the effectiveness of Wildfire is drastically reduced.

Audit
^^^^^
Navigate to Device > Setup > Content-ID > Content-ID Settings.

Verify that Allow forwarding of decrypted content is checked.

Remediation
^^^^^^^^^^^
Navigate to Device > Setup > Content-ID > Content-ID Settings.

Set Allow forwarding of decrypted content to be checked.

Note that SSL Forward Proxy must be configured for this setting to be effective.


Default Value
^^^^^^^^^^^^^
Not Configured      

References
^^^^^^^^^^
1. “WildFire Fails Forwarding File to Cloud for Encrypted Traffic” -
https://live.paloaltonetworks.com/docs/DOC-6845

2. “Wildfire Administrator's Guide 9.0 (English) - Forward Decrypted SSL Traffic for Wildfire Analysis" -
https://docs.paloaltonetworks.com/wildfire/9-0/wildfire-admin/submit-files-for-wildfire-analysis/forward-decrypted-ssl-traffic-for-wildfire-analysis.html#

3. “Wildfire Administrator's Guide 9.0 (English) - Wildfire Best Practices" -
https://docs.paloaltonetworks.com/wildfire/9-0/wildfire-admin/wildfire-deployment-best-practices/wildfire-best-practices.html#

5.5 Ensure all WildFire session information settings are enabled 
-----------------------------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1 

Description
^^^^^^^^^^^
Enable all options under Session Information Settings for WildFire. 

Rationale
^^^^^^^^^
Permitting the firewall to send all of this information to WildFire creates more detailed reports, thereby making
the process of tracking down potentially infected devices more efficient. This could prevent an infected system from
further infecting the environment. Environments with security policies restricting sending this data to the WildFire
cloud can instead utilize an on-premises WildFire appliance. In addition, risk can be analyzed in the context of
the destination host and user account, either during analysis or during incident response.

Audit
^^^^^
Navigate to Device > Setup > WildFire > Session Information Settings.

Verify that every option is enabled.

Remediation
^^^^^^^^^^^
Navigate to Device > Setup > WildFire > Session Information Settings.

Set every option to be enabled.


Default Value
^^^^^^^^^^^^^
All Session Information Settings are enabled by default. These include:

    * Source IP
    * Source port
    * Destination IP
    * Destination port
    * Virtual System
    * Application
    * User
    * URL
    * File name
    * Email sender
    * Email recipient
    * Email subject

References
^^^^^^^^^^
1. “Wildfire Administrator's Guide 9.0 (English)" -
https://docs.paloaltonetworks.com/wildfire/9-0/wildfire-admin.html#

2. “Wildfire Administrator's Guide 9.0 (English) - Wildfire Best Practices" -
https://docs.paloaltonetworks.com/wildfire/9-0/wildfire-admin/wildfire-deployment-best-practices/wildfire-best-practices.html

5.6 Ensure alerts are enabled for malicious files detected by WildFire 
-----------------------------------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1 

Description
^^^^^^^^^^^
Configure WildFire to send an alert when a malicious or greyware file is detected. This alert could be sent by
whichever means is preferable, including email, SNMP trap, or syslog message. Alternatively, configure the WildFire
cloud to generate alerts for malicious files. The cloud can generate alerts in addition to or instead of the local
WildFire implementation. Note that the destination email address of alerts configured in the WildFire cloud portal
is tied to the logged in account, and cannot be modified. Also, new systems added to the WildFire cloud portal will
not be automatically set to email alerts.

Rationale
^^^^^^^^^
WildFire analyzes files that have already been downloaded and possibly executed. A WildFire verdict of malicious
indicates that a computer could already be infected. In addition, because WildFire only analyzes files it has not
already seen that were not flagged by the fievade detection by desktop antivirus products.

Audit
^^^^^
Navigate to Objects > Log Forwarding.

Verify that the WildFire log type is configured to generate alerts using the desired alerting mechanism(s).

Remediation
^^^^^^^^^^^
From GUI, configure some combination of the following Server Profiles:

Configure the Email Server:

Select Device > Server Profiles > Email

Click Add Enter a name for the Profile. Select the virtual system from the Location drop down menu (if applicable)
Click Add

Configure the Syslog Server:

Select Device > Server Profiles > Syslog > Add Enter Name, Display Name, Syslog Server, Transport, Port, Format,
Facility Click OK Click Commit to save the configuration

Configure the SMTP Server:

Select Device > Server Profiles > Email Select Add, Name, Display Name, From, To, Additional Recipients,
Gateway IP or Hostname Click OK Click Commit to save the configuration

Navigate to Objects, Log Forwarding Choose Add, set the log type to "wildfire", add the filter "(verdict neq benign)",
then add log destinations for SNMP, Syslog, Email or HTTP as required.


Default Value
^^^^^^^^^^^^^
Not Configured 

References
^^^^^^^^^^
1. “WildFire Email Alerts: Subscribe or Add Additional Recipients” -
https://live.paloaltonetworks.com/docs/DOC-7740

2. “Wildfire Administrator's Guide 9.0 (English)" -
https://docs.paloaltonetworks.com/wildfire/9-0/wildfire-admin.html


5.7 Ensure 'WildFire Update Schedule' is set to download and install updates every minute 
------------------------------------------------------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1 

Description
^^^^^^^^^^^
Set the WildFire update schedule to download and install updates every minute. 

Rationale
^^^^^^^^^
WildFire definitions may contain signatures to block immediate, active threats to the environment. With a 1
minute update schedule, the firewall can ensure threats with new definitions are quickly mitigated.

Audit
^^^^^
Navigate to Device > Dynamic Updates > WildFire Update Schedule.

Verify that Action is set to Download and Install.

Verify that Recurrence is set to Every Minute.

Remediation
^^^^^^^^^^^
Navigate to Device > Dynamic Updates > WildFire Update Schedule.

Set Action to Download and Install.

Set Recurrence to Every Minute.


Default Value
^^^^^^^^^^^^^
Not Configured 

References
^^^^^^^^^^
1. “Wildfire Administrator's Guide 9.0 (English)" -
https://docs.paloaltonetworks.com/wildfire/9-0/wildfire-admin.html

2. “How to Configure WildFire” -
https://live.paloaltonetworks.com/docs/DOC-3252

3. “Tips for Managing Content Updates” -
https://live.paloaltonetworks.com/docs/DOC-1578


6.1 Ensure that antivirus profiles are set to block on all decoders except 'imap' and 'pop3' 
---------------------------------------------------------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1 

Description
^^^^^^^^^^^
Configure antivirus profiles to a value of 'block' for all decoders except imap and pop3 under both Action and
WildFire Action. If required by the organization's email implementation, configure imap and pop3 decoders to 'alert'
under both Action and WildFire Action.

Rationale
^^^^^^^^^
Antivirus signatures produce low false positives. By blocking any detected malware through the specified decoders,
the threat of malware propagation through the firewall is greatly reduced. It is recommended to mitigate malware
found in pop3 and imap through a dedicated antivirus gateway. Due to the nature of the pop3 and imap protocols,
the firewall is not able to block only a single email message containing malware. Instead, the entire session would
be terminated, potentially affecting benign email messages.

Audit
^^^^^
Navigate to Objects > Security Profiles > Antivirus

Verify that antivirus profiles have all decoders set to block for both Action and Wildfire Action.

If imap and pop3 are required in the organization, verify that the imap and pop3 decoders are set to alert
for both Action and Wildfire Action.

Remediation
^^^^^^^^^^^
Navigate to Objects > Security Profiles > Antivirus. Set antivirus profiles to have all decoders set to block for
both Action and Wildfire Action. If imap and pop3 are required in the organization, set the imap and pop3 decoders
to alert for both Action and Wildfire Action.


Default Value
^^^^^^^^^^^^^
Not Configured   

References
^^^^^^^^^^
1. “Threat Prevention Deployment Tech Note” -
https://live.paloaltonetworks.com/docs/DOC-3094

2. “PAN-OS Administrator's Guide 9.0 (English) - Security Profiles” -
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/policy/security-profiles.html

6.2 Ensure a secure antivirus profile is applied to all relevant security policies 
-----------------------------------------------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1 

Description
^^^^^^^^^^^
Create a secure antivirus profile and apply it to all security policies that could pass HTTP, SMTP, IMAP, POP3,
FTP, or SMB traffic. The antivirus profile may be applied to the security policies directly or through a profile group.

Rationale
^^^^^^^^^
By applying a secure antivirus profile to all applicable traffic, the threat of malware propagation through the
firewall is greatly reduced. Without an antivirus profile assigned to any potential hostile zone, the first
protection in the path against malware is removed, leaving in most cases only the desktop endpoint protection
application to detect and remediate any potential malware.

Audit
^^^^^
Navigate to Policies > Security. For each policy, navigate to [Policy Name] > Actions

Verify there is a secure Antivirus profile applied to all security policies passing traffic -
regardless of protocol. This can be set by Profiles or by Profile Group.

Remediation
^^^^^^^^^^^
Navigate to Policies > Security.

For each policy, navigate to [Policy Name] > Actions

Set an Antivirus profile or a Profile Group containing an AV profile for each security
policy passing traffic - regardless of protocol.

Impact
^^^^^^
Not having an AV Profile on a Security Policy allows signature-based malware to transit the security boundary
without blocks or alerts. In most cases this leaves only the Endpoint Security application to block or alert malware.

Default Value
^^^^^^^^^^^^^
No Antivirus Profiles are enabled on any default or new Security Policy 

References
^^^^^^^^^^
1. “PAN-OS Administrator's Guide 9.0 (English) - Security Policies ” -
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/policy/security-policy.html

2. “PAN-OS Administrator's Guide 9.0 (English) - Security Profiles” -
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/policy/security-profiles.html

6.3 Ensure an anti-spyware profile is configured to block on all spyware severity levels, categories, and threats 
------------------------------------------------------------------------------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1 

Description
^^^^^^^^^^^
If a single rule exists within the anti-spyware profile, configure it to block on any spyware severity level,
any category, and any threat. If multiple rules exist within the anti-spyware profile, ensure all spyware
categories, threats, and severity levels are set to be blocked. Additional rules may exist for packet capture or
exclusion purposes.

Rationale
^^^^^^^^^
Requiring a blocking policy for all spyware threats, categories, and severities reduces the risk of spyware traffic
from successfully exiting the organization. Without an anti-spyware profile assigned to any potential hostile zone,
the first protection in the path against malware is removed, leaving in most cases only the desktop endpoint
protection application to detect and remediate any potential spyware.

Audit
^^^^^
Navigate to Objects > Security Profiles > Anti-Spyware.

Verify a rule exists within the anti-spyware profile that is configured to perform the
Block Action on any Severity level, any Category, and any Threat Name.

Remediation
^^^^^^^^^^^
Navigate to Objects > Security Profiles > Anti-Spyware.

Set a rule within the anti-spyware profile that is configured to perform the Block
Action on any Severity level, any Category, and any Threat Name.


Default Value
^^^^^^^^^^^^^
Two Anti-Spyware Security Profiles are configured by default "strict" and "default". 

References
^^^^^^^^^^
1. “PAN-OS Administrator's Guide 9.0 (English) - Security Profiles":
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/policy/security-policy.html


6.4 Ensure DNS sinkholing is configured on all anti-spyware profiles in use 
----------------------------------------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1 

Description
^^^^^^^^^^^
Configure DNS sinkholing for all anti-spyware profiles in use. All internal requests to the selected sinkhole
IP address must traverse the firewall. Any device attempting to communicate with the DNS sinkhole IP address
should be considered infected.

Rationale
^^^^^^^^^
DNS sinkholing helps to identify infected clients by spoofing DNS responses for malware domain queries. Without
sinkholing, the DNS server itself may be seen as infected, while the truly infected device remains unidentified.
In addition, sinkholing also ensures that DNS queries that might be indicators of compromise do not transit
the internet, where they could be potentially used to negatively impact the "ip reputation" of the organization's
internet network subnets.

Audit
^^^^^
Navigate to Objects > Security Profiles > Anti-Spyware.

Within the each anti-spyware profile, under its DNS Signatures tab, verify the DNS Signature Source List:

Palo Alto Networks Content DNS Signatures should have as its Action on DNS Queries set to sinkhole

If licensed, the Palo Alto Networks Cloud DNS Security should have as its Action on DNS Queries set to sinkhole

Verify the 'Sinkhole IPv4' IP address is correct. This should be set to sinkhole.paloaltnetworks.com,
or if an internal host is set then that host IP or FQDN should be in that field Verify the 'Sinkhole IPv6'
IP address is correct. This should be set to IPv6 Loopback IP (::1), or if an internal DNS Sinkhole host is
set then that host IP or FQDN should be in that field

Navigate to Policies > Security Policies

For each outbound security Policy, in the Actions tab, verify that the Anti-Spyware setting
includes the Spyware Profile created, either explicitly or as a Group Profile

To verify correct operation of DNS Security, from an internal station make a DNS request to
each of the following hosts:

test-malware.testpanw.com to test Malware DNS Signature checks

test-c2.testpanw.com to test C2 DNS Signature checks

test-dga.testpanw.com to test DGA (Domain Generation Algorithm) DNS attack checks

test-dnstun.testpanw.com to test DNS Tunneling attack checks

Each of these DNS requests should be redirected to the configured DNS Sinkhole server IP address Each of these DNS
requests should appear in the firewall logs, under Monitor > Logs > Threat. If configured, each of these
requests should generate an alert in the organization's SIEM.

Remediation
^^^^^^^^^^^
Navigate to Objects > Security Profiles > Anti-Spyware.

Within the each anti-spyware profile, under its DNS Signatures tab, set the DNS Signature Source List:
Palo Alto Networks Content DNS Signatures should have as its Action on DNS Queries set to sinkhole

If licensed, the Palo Alto Networks Cloud DNS Security should have as its Action on DNS Queries set
to sinkhole Verify the 'Sinkhole IPv4' IP address is correct.
This should be set to sinkhole.paloaltnetworks.com, or if an internal host is set then that host IP or
FQDN should be in that field

Verify the 'Sinkhole IPv6' IP address is correct.
This should be set to IPv6 Loopback IP (::1), or if an internal DNS Sinkhole host is set then that
host IP or FQDN should be in that field Navigate to Policies > Security Policies For each outbound security
Policy, in the Actions tab, set the Anti-Spyware setting to include the Spyware Profile created,
either explicitly or as a Group Profile


Default Value
^^^^^^^^^^^^^
Not Configured   

References
^^^^^^^^^^

1. “How to Deal with Conficker using DNS Sinkhole” -
https://live.paloaltonetworks.com/docs/DOC-6628

2. “Threat Prevention Deployment Tech Note” -
https://live.paloaltonetworks.com/docs/DOC-3094

3. "PANOS Administrator's Guide 9.0 (English) - Security Profiles":
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/policy/security-profiles.html

4. "PAN-OS Administrator's Guide 9.0 (English) - DNS Security" -
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/threat-prevention/dns-security.html#

6.5 Ensure passive DNS monitoring is set to enabled on all anti-spyware profiles in use 
----------------------------------------------------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1 

Description
^^^^^^^^^^^
Enable passive DNS monitoring within all anti-spyware profiles in use. 

Rationale
^^^^^^^^^
Rationale:  and threat intelligence capabilities. This is performed without source information delivered to
PAN to ensure sensitive DNS information of the organization is not compromised.

Audit
^^^^^
Navigate to Device > Setup > Telemetry.

Ensure that Passive DNS Monitoring is enabled

Remediation
^^^^^^^^^^^
Navigate to Device > Setup > Telemetry.

Set Passive DNS Monitoring to enabled


Default Value
^^^^^^^^^^^^^
Not Configured 

References
^^^^^^^^^^
1. “What Information is Submitted to the Palo Alto Networks when Enabling the Passive DNS Feature” -
https://live.paloaltonetworks.com/docs/DOC-7256

2. "PAN-OS Administrator's Guide 9.0 (English) - DNS Security" -
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/threat-prevention/dns-security.html#


6.6 Ensure a secure anti-spyware profile is applied to all security policies permitting traffic to the Internet 
----------------------------------------------------------------------------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1 

Description
^^^^^^^^^^^
Create one or more anti-spyware profiles and collectively apply them to all security policies permitting traffic to
the Internet. The anti-spyware profiles may be applied to the security policies directly or through a profile group.

Rationale
^^^^^^^^^
By applying secure anti-spyware profiles to all applicable traffic, the threat of sensitive data exfiltration or
command-and-control traffic successfully passing through the firewall is greatly reduced. Anti-spyware profiles
are not restricted to particular protocols like antivirus profiles, so anti-spyware profiles should be applied to
all security policies permitting traffic to the Internet. Assigning an anti-spyware profile to each trusted zone
will quickly and easily identify trusted hosts that have been infected with spyware, by identifying the infection
from their outbound network traffic. In addition, that outbound network traffic will be blocked by the profile.

Audit
^^^^^
Navigate to Objects > Security Profiles > Anti-Spyware. Also navigate to Policies > Security.

Verify there are one or more anti-spyware profiles that collectively apply to all inside to outside traffic from
any address to any address and any application and service.

Remediation
^^^^^^^^^^^
Navigate to Objects > Security Profiles > Anti-Spyware. Also navigate to Policies > Security.

Set one or more anti-spyware profiles to collectively apply to all inside to outside traffic from any
address to any address and any application and service.

Default Value
^^^^^^^^^^^^^
Not Configured   

References
^^^^^^^^^^
1. “Threat Prevention Deployment Tech Note” -
https://live.paloaltonetworks.com/docs/DOC-3094

2. “PAN-OS Administrator's Guide 9.0 (English) - Security Profiles” -
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/policy/security-profiles.html


6.7 Ensure a Vulnerability Protection Profile is set to block attacks against critical and high vulnerabilities, and set to default on medium, low, and informational vulnerabilities 
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1 

Description
^^^^^^^^^^^
Configure a Vulnerability Protection Profile set to block attacks against any critical or high vulnerabilities, at
minimum, and set to default on any medium, low, or informational vulnerabilities. Configuring an alert action for
low and informational, instead of default, will produce additional information at the expense of greater log
utilization.

Rationale
^^^^^^^^^
A Vulnerability Protection Profile helps to protect assets by alerting on, or blocking, network attacks.
The default action for attacks against many critical and high vulnerabilities is to only alert on the attack
- not to block.

Audit
^^^^^
Navigate to Objects > Security Profiles > Vulnerability Protection.

Verify a Vulnerability Protection Profile is set to block attacks against any critical or high vulnerabilities
(minimum), and set to default on attacks against any medium, low, or informational vulnerabilities.

Remediation
^^^^^^^^^^^
Navigate to Objects > Security Profiles > Vulnerability Protection.

Set a Vulnerability Protection Profile to block attacks against any critical or high vulnerabilities (minimum),
and to default on attacks against any medium, low, or informational vulnerabilities.

Impact
^^^^^^
Not configuring a Vulnerability Protection Profile means that network attacks will not be logged, alerted on or blocked. 

Default Value
^^^^^^^^^^^^^
Two Vulnerability Protection Profiles are configured by default - "strict" and "default".  

References
^^^^^^^^^^

1. “Threat Prevention Deployment Tech Note” -
https://live.paloaltonetworks.com/docs/DOC-3094

2. “PAN-OS Administrator's Guide 9.0 (English) - Security Profiles” -
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/policy/security-profiles.html

6.8 Ensure a secure Vulnerability Protection Profile is applied to all security rules allowing traffic 
-------------------------------------------------------------------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1 

Description
^^^^^^^^^^^
For any security rule allowing traffic, apply a securely configured Vulnerability Protection Profile. Careful
analysis of the target environment should be performed before ction.

Rationale
^^^^^^^^^
A Vulnerability Protection Profile helps to protect assets by alerting on, or blocking network attacks. By applying a
secure Vulnerability Protection Profile to all security rules permitting traffic, all network traffic traversing
the firewall will be inspected for attacks. This protects both organizational assets from attack and organizational
reputation from damage. Note that encrypted sessions do not allow for complete inspection.

Audit
^^^^^
Navigate to Policies > Security.

For each Policy, under the Actions tab, select Vulnerability Protection.

Verify either the 'Strict' or the 'Default' profile is selected, or a custom profile that complies with
the organization's policies, legal and regulatory requirements.

Remediation
^^^^^^^^^^^
Navigate to Policies > Security.

For each Policy, under the Actions tab, select Vulnerability Protection.

Set it to use either the 'Strict' or the 'Default' profile, or a custom profile that complies with the
organization's policies, legal and regulatory requirements.

Impact
^^^^^^
Not configuring a Vulnerability Protection Profile means that network attacks will not be logged, alerted on or blocked.  

Default Value
^^^^^^^^^^^^^
Not Configured 

References
^^^^^^^^^^
1. “Threat Prevention Deployment Tech Note” -
https://live.paloaltonetworks.com/docs/DOC-3094

2. “PAN-OS Administrator's Guide 9.0 (English) - Security Policies” -
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/policy/security-policy.html

3. “PAN-OS Administrator's Guide 9.0 (English) - Security Profiles” -
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/policy/security-profiles.html

6.9 Ensure that PAN-DB URL Filtering is used 
---------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1 

Description
^^^^^^^^^^^
Configure the device to use PAN-DB URL Filtering instead of BrightCloud. 

Rationale
^^^^^^^^^
Standard URL filtering provides protection against inappropriate and malicious URLs and IP addresses.
PAN-DB URL Filtering is slightly less granular than the BrightCloud URL filtering. However the PAN-DB Filter
offers additional malware protection and PAN threat intelligence by using the Wildfire service as an additional
input, which is currently not available in the BrightCloud URL Filtering license. This makes the PAN-DB filter
more responsive to specific malware "campaigns".

Audit
^^^^^
Navigate to Device > Licenses.

Click on PAN-DB URL Filtering. Verify Active is set to Yes.

Remediation
^^^^^^^^^^^
Navigate to Device > Licenses.

Click on PAN-DB URL Filtering. Set Active to Yes.

Impact
^^^^^^
Not having an effective URL Filtering configuration can leave an organization open to legal action, internal
HR issues, non-compliance with regulatory policies or productivity loss.

Default Value
^^^^^^^^^^^^^
Not Configured     

References
^^^^^^^^^^

1. “PAN-OS Administrator's Guide 9.0 (English) - URL Filtering” -
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/url-filtering.html

2. “PAN-OS Administrator's Guide 9.0 (English) - URL Filtering Best Practices":
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/url-filtering/url-filtering-best-practices.html

6.10 Ensure that URL Filtering uses the action of “block” or “override” on the URL categories
---------------------------------------------------------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1 

Description
^^^^^^^^^^^
Ideally, deciding which URL categories to block, and which to allow, is a joint effort between IT and another
entity of authority within an organizationsuch as the legal department or administration. For most organizations,
blocking or requiring an override on the following categories represents a minimum baseline: adult, hacking,
command-and-control, copyright-infringement, extremism, malware, phishing, proxy-avoidance-and-anonymizers,
and parked. Some organizations may add "unknown" and "dynamic-dns" to this list, at the expense of some support
calls on those topics.

Rationale
^^^^^^^^^
Certain URL categories pose a technology-centric threat, such as command-and-control, copyright-infringement,
extremism, malware, phishing, proxy-avoidance-and-anonymizers, and parked. Users visiting websites in these
categories, many times unintentionally, are at greater risk of compromising the security of their system.
Other categories, such as adult, may pose a legal liability and will be blocked for those reasons.

Audit
^^^^^
Navigate to Objects > Security Profiles > URL Filtering.

Verify that all URL categories designated by the organization are listed, and the action is set to Block.

Remediation
^^^^^^^^^^^
Navigate to Objects > Security Profiles > URL Filtering.

Set a URL filter so that all URL categories designated by the organization are listed.

Navigate to the Actions tab.  Set the action to Block.

Impact
^^^^^^
Not having an effective URL Filtering configuration can leave an organization open to legal action,
internal HR issues, non-compliance with regulatory policies or productivity loss.

Default Value
^^^^^^^^^^^^^
Not Configured 

References
^^^^^^^^^^
1. “PAN-OS Administrator's Guide 9.0 (English) - Security Profiles” -
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/policy/security-profiles.html

2. “PAN-OS Administrator's Guide 9.0 (English) - URL Filtering” -
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/url-filtering.html

3. “PAN-OS Admin Guide 9.0 (English) - URL Filtering Best Practices":
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/url-filtering/url-filtering-best-practices.html

6.11 Ensure that access to every URL is logged 
-----------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1 

Description
^^^^^^^^^^^
URL filters should not specify any categories as Allow Categories. 

Rationale
^^^^^^^^^
Setting a URL filter to have one or more entries under Allow Categories will cause no log entries to be produced in
the URL Filtering logs for access to URLs in those categories. For forensic, legal, and HR purposes,
it is advisable to log access to every URL. In many cases failure to log all URL access is a violation of
corporate policy, legal requirements or regulatory requirements.

Audit
^^^^^
Navigate to Objects > Security Profiles > URL Filtering. Verify that the for all allowed categories,
that the Site Access action is set to alert

Remediation
^^^^^^^^^^^
Navigate to Objects > Security Profiles > URL Filtering.

For each permitted category, set the Site Access action to alert

Impact
^^^^^^
Not having an effective URL Filtering configuration can leave an organization open to legal action,
internal HR issues, non-compliance with regulatory policies or productivity loss.

Default Value
^^^^^^^^^^^^^
A default URL Filtering Security Profile is configured, with the following categories set to "block":

    * abused-drugs
    * adult
    * gambling
    * hacking
    * malware
    * phishing
    * questionable
    * weapons

3 Categories are set to alert in the default policy, and 58 Categories are set to allow (which means they are not logged)

References
^^^^^^^^^^

1. “PAN-OS Administrator's Guide 9.0 (English) - URL Filtering Best Practices":
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/url-filtering/url-filtering-best-practices.html

2. “PAN-OS Administrator's Guide 9.0 (English) - URL Filtering” -
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/url-filtering.html

6.12 Ensure all HTTP Header Logging options are enabled 
--------------------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1 

Description
^^^^^^^^^^^
Enable all options (User-Agent, Referrer, and X-Forwarded-For) for HTTP header logging. 

Rationale
^^^^^^^^^
Logging HTTP header information provides additional information in the URL logs, which may be useful during
forensic investigations. The User-Agent option logs which browser was used during the web session, which could
provide insight to the vector used for malware retrieval. The Referrer option logs the source webpage responsible
for referring the user to the logged webpage. The X-Forwarded-For option is useful for preserving the -checking
the Log container page only box produces substantially more information about web activity, with the expense of
producing far more entries in the URL logs. If this option remains checked, a URL filter log entry showing details
of a malicious file download may not exist.

Audit
^^^^^
Navigate to Objects > Security Profiles > URL Filtering > URL Filtering Profile > URL Filtering Settings.

Verify these four settings:

a. Log container page only box is un-checked

b. User-Agent box is checked

c. Referrer box is checked

d. X-Forwarded-For box is checked

Remediation
^^^^^^^^^^^
Navigate to Objects > Security Profiles > URL Filtering > URL Filtering Profile > URL Filtering Settings.

Set the following four settings:

a. Log container page only box is un-checked

b. Check the User-Agent box

c. Check the Referrer box

d. Check the X-Forwarded-For box

Impact
^^^^^^
Not having an effective URL Filtering configuration can leave an organization open to legal action,
internal HR issues, non-compliance with regulatory policies or productivity loss.

Default Value
^^^^^^^^^^^^^
Not Configured 

References
^^^^^^^^^^

1. “PAN-OS Administrator's Guide 9.0 (English) - URL Filtering Best Practices":
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/url-filtering/url-filtering-best-practices.html

6.13 Ensure secure URL filtering is enabled for all security policies allowing traffic to the Internet 
-------------------------------------------------------------------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1 

Description
^^^^^^^^^^^
Apply a secure URL filtering profile to all security policies permitting traffic to the Internet. The URL Filtering
profile may be applied to the security policies directly or through a profile group.

Rationale
^^^^^^^^^
URL Filtering policies dramatically reduce the risk of users visiting malicious or inappropriate websites.
In addition, a complete URL history log for all devices is invaluable when performing forensic analysis in the
event of a security incident. Applying complete and approved URL filtering to outbound traffic is a frequent
requirement in corporate policies, legal requirements or regulatory requirements.

Audit
^^^^^
To Verify URL Filtering:

For each Security Policy that transits traffic to the public internet,
navigate to Policies > Security > Security Profiles > [Policy Name] > Actions.

Verify there is a URL Filtering profile that complies with the policies of the organization
is applied to all Security Policies that transit traffic to the public internet.

Remediation
^^^^^^^^^^^
To Set URL Filtering:

For each Security Profile that transits traffic to the internet, navigate to Policies > Security >
Security Profiles > [Policy Name] > Actions. Set a URL Filtering profile that complies with the
policies of the organization is applied to all Security Policies that transit traffic to the public internet.

Impact
^^^^^^
Not having an effective URL Filtering configuration can leave an organization open to legal action,
internal HR issues, non-compliance with regulatory policies or productivity loss.

Default Value
^^^^^^^^^^^^^
Not Configured 

References
^^^^^^^^^^
1. “PAN-OS Administrator's Guide 9.0 (English) - URL Filtering Best Practices":
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/url-filtering/url-filtering-best-practices.html

6.14 Ensure alerting after a threshold of credit card or Social Security numbers is detected is enabled 
--------------------------------------------------------------------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1 

Description
^^^^^^^^^^^
This guideline is highly specific to an organization. While blocking of credit card or Social Security numbers
will not occur with the recommended settings below, careful tuning is also recommended.

Rationale
^^^^^^^^^
Credit card and Social Security numbers are sensitive, and should never traverse an organization should also be
avoided whenever possible. Detecting and blocking known sensitive information is a basic protection against a
data breach or data loss. Not implementing these defenses can lead to loss of regulatory accreditation
(such as PCI, HIPAA etc.), or can lead to legal action from injured parties or regulatory bodies.

Audit
^^^^^
Navigate to Objects > Security Objects > Data Patterns.

Verify an appropriate Data Pattern has been created that accounts for sensitive information within your organization.
In most cases this will include Credit Card Numbers, and your jurisdiction's equivalent of Social Insurance Numbers.
In many cases these can simply be picked from the list of Predefined Patterns.

Navigate to Objects > Security Profiles > Data Filtering.

Verify an appropriate Data Filtering Profile has been created, using the created Data Patterns.

Ensure that an Alert Threshold is set that generates alerts appropriately. A typical starting value for Alert
Threshold is 20, but this should be adjusted after appropriate testing.

Remediation
^^^^^^^^^^^
Navigate to Objects > Security Objects > Data Patterns.

Create an appropriate Data Pattern that accounts for sensitive information within your organization.
In most cases this will include Credit Card Numbers, and your jurisdiction's equivalent of Social Insurance
Numbers. In many cases these can simply be picked from the list of Predefined Patterns.

Navigate to Objects > Security Profiles > Data Filtering.

Create appropriate Data Filtering Profile, using the created Data Patterns. Ensure that an Alert Threshold
is set that generates alerts appropriately. A typical starting value for Alert Threshold is 20,
but this should be adjusted after appropriate testing.


Default Value
^^^^^^^^^^^^^
Not Configured 

References
^^^^^^^^^^
1. “What are the Data Filtering Best Practices?” -
https://live.paloaltonetworks.com/docs/DOC-2513

2. “PAN-OS Administrator's Guide 9.0 (English) - Setting up Data Filtering" -
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/threat-prevention/set-up-data-filtering.html#

6.15 Ensure a secure Data Filtering profile is applied to all security policies allowing traffic to or from the Internet 
-------------------------------------------------------------------------------------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1 

Description
^^^^^^^^^^^
Create a secure Data Filtering profile and apply it to all security policies permitting traffic to or from the
Internet. The Data Filtering profile may be applied to security policies directly or through a profile group.

Rationale
^^^^^^^^^
A Data Filtering profile helps prevent certain types of sensitive information from traversing known sensitive
information is a basic protection against a data breach or data loss. Not implementing these defenses can lead
to loss of regulatory accreditation (such as PCI, HIPAA etc.), or can lead to legal action from injured parties
or regulatory bodies. Before starting, be very aware that Data Filtering will often block data that you didn't
anticipate, false positives will definitely occur. Even the prebuilt filters will frequently match on unintended
data in files or websites. Work very closely with your user community to ensure that required data is blocked or
alerted on, but a minimum of false positive blocks occur. As false positives occur, ensure that your user
community has a clear and timely procedure to get the configuration updated.

Audit
^^^^^
Navigate to Objects > Custom Objects > Data Patterns.

Verify that the patterns defined match the various data that you wish to monitor or make blocking decisions on.

Navigate to Objects > Security Profiles > Data Filtering

For each Filtering Profile, verify that the Data Patterns defined matches the data you wish to monitor,
with appropriate values for Alert Threshold (typically 20), Block Threshold (typically 0) and Log Severity.

Finally, navigate to Policies > Security.

Open all appropriate policies, for each Policy choose the Actions tab, and verify that the appropriate
Data Filtering Policy is applied (either as an individual Profile or as part of a Group Profile)

Remediation
^^^^^^^^^^^
Navigate to Objects > Custom Objects > Data Patterns.

Add patterns to match the various data that you wish to monitor or make blocking decisions on.

Navigate to Objects > Security Profiles > Data Filtering

Add a Filtering Profile that matches the data you wish to monitor, with appropriate values for Alert Threshold
(typically 20), Block Threshold (typically 0) and Log Severity Finally, apply the Filtering Profile to a
Security Profile.

Navigate to Policies > Security.

Edit all appropriate policies, and for each Policy choose the Actions tab,
and add the appropriate Data Filtering Policy (either as an individual Profile or as part of a Group Profile)


Default Value
^^^^^^^^^^^^^
Not Configured 

References
^^^^^^^^^^
1. “PAN-OS Administrator's Guide 9.0 (English) - Setting up Data Filtering" -
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/threat-prevention/set-up-data-filtering.html#


6.16 Ensure that a Zone Protection Profile with an enabled SYN Flood Action of SYN Cookies is attached to all untrusted zones 
------------------------------------------------------------------------------------------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1 

Description
^^^^^^^^^^^
Enable the SYN Flood Action of SYN Cookies for all untrusted zones. The Alert, Activate, and Maximum settings for
SYN Flood Protection depend highly on the environment and device used. Perform traffic analysis on the specific
environment and firewall to determine accurate thresholds. Do not rely on default values to be appropriate for an
environment. Setting these values for all interfaces is an approach that should be considered by many organizations,
as traffic floods can result from internal testing or malware as well. of new sessions per second maximum for each
platform: PA-200 = 1,000 CPS PA-500 = 7,500 CPS PA-2000 series = 15,000 CPS PA-3000 series = 50,000 CPS PA-5000
series = 120,000 CPS PA-7050 = 720,000 CPS

Rationale
^^^^^^^^^
Protecting resources and the firewall itself against DoS/DDoS attacks requires a layered approach.
Firewalls alone cannot mitigate all DoS attacks, however, many attacks can be successfully mitigated.
Utilizing SYN Cookies helps to mitigate SYN flood attacks, where the CPU and/or memory buffers of the victim
device become overwhelmed by incomplete TCP sessions. SYN Cookies are preferred over Random Early Drop.

Audit
^^^^^
From GUI:

Navigate to Network > Network Profiles > Zone Protection > Zone Protection Profile > Flood Protection tab.

Verify the SYN box is checked.

Verify the Action dropdown is SYN Cookies.

Verify Alert is 20000(or appropriate for org).

Verify Activate is 25000(50% of maximum for firewall model).

Verify Maximum is 1000000(or appropriate for org).

Navigate to Network > Zones >.

Open the zone facing any untrusted network.

Verify that Zone Protection has the Zone Protection Profile set to the Profile created.

Remediation
^^^^^^^^^^^
From GUI:

Navigate to Network > Network Profiles > Zone Protection > Zone Protection Profile > Flood Protection tab.

Check the SYN box.

Set the Action dropdown to SYN Cookies

Set Alert to 20000(or appropriate for org).

Set Activate to 25000(50% of maximum for firewall model).

Set Maximum to 1000000(or appropriate for org)

Navigate to Network > Zones >.

Open the zone facing any untrusted network, if one does not exist create it.

Set Zone Protection to the Zone Protection Profile created.

Impact
^^^^^^
Not configuring a Network Zone Protection Profile on untrusted interfaces leaves an organization exposed to
common attacks and reconnaissance from those untrusted networks. Not configuring a Zone Protection Profile
for internal networks leaves an organization vulnerable to malware, software or hardware causes of traffic
flooding from internal sources.

Default Value
^^^^^^^^^^^^^
Not Configured       

References
^^^^^^^^^^

1. “Understanding DoS Protection” -
https://live.paloaltonetworks.com/docs/DOC-5078

2. "Syn Cookie Operation” -
https://live.paloaltonetworks.com/docs/DOC-1542

3. “How to Determine if Configured DoS Classify TCP SYN Cookie Alarm, Activate and Maximal Rate is Triggered” -
https://live.paloaltonetworks.com/docs/DOC-6801

4. “Threat Prevention Deployment Tech Note” -
https://live.paloaltonetworks.com/docs/DOC-3094

5. “What are the Differences between DoS Protection and Zone Protection?” -
https://live.paloaltonetworks.com/docs/DOC-4501

6. “Application DDoS Mitigation” - https://live.paloaltonetworks.com/docs/DOC-7158

7. PANOS 9.0 Admin Guide - Zone Protection . Flood Protection:
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-web-interface-help/network/network-network-profiles/network-network-profiles-zone-protection/flood-protection.html#

6.17 Ensure that a Zone Protection Profile with tuned Flood Protection settings enabled for all flood types is attached to all untrusted zones 
-----------------------------------------------------------------------------------------------------------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 2 

Description
^^^^^^^^^^^
Enable all Flood Protection options in the Zone Protection Profile attached to all untrusted zones. The Alert,
Activate, and Maximum settings for Flood Protection depend highly on the environment and device used. Perform
traffic analysis on the specific environment and firewall to determine accurate thresholds. Do not rely on default
values to be appropriate for an environment. Setting these values for all interfaces is an approach that should be
considered by many organizations, as traffic floods can result from internal testing or malware as well.

Rationale
^^^^^^^^^
Without flood protection, it may be possible for an attacker, through the use of a botnet or other means, to
overwhelm network resources. Flood protection does not completely eliminate this risk; rather, it provides a
layer of protection. Without a properly configured zone protection profile applied to untrusted interfaces,
the protected / trusted networks are susceptible to large number of attacks. While many of these involve denial
of service, some of these attacks are designed to evade IPS systems (fragmentation attacks for instance) or to
evade basic firewall protections (source routing and record route attacks).

Audit
^^^^^
In the GUI:

Navigate to Network > Network Profiles > Zone Protection > Flood Protection.

Ensure that all settings are enabled with at least the default values.

Navigate to Network > Zones, select each untrusted zone in turn, and ensure that the Zone Protection Profile is set.

Remediation
^^^^^^^^^^^
In the GUI:

Navigate to Network > Network Profiles > Zone Protection > Flood Protection.

Set all settings to "enabled" with at least the default values.

Navigate to Network > Zones, select each untrusted zone in turn, and set the Zone Protection Profile.

Impact
^^^^^^
Not configuring and applying a Network Zone Protection Profile leaves an organization exposed to common attacks and
reconnaissance from untrusted networks. Not configuring a Zone Protection Profile for internal networks leaves an
organization vulnerable to malware, software or hardware causes of traffic flooding from internal sources.

Default Value
^^^^^^^^^^^^^
Not Configured 

References
^^^^^^^^^^
1. “Understanding DoS Protection” -
https://live.paloaltonetworks.com/docs/DOC-5078]

2. “Threat Prevention Deployment Tech Note” -
https://live.paloaltonetworks.com/docs/DOC-3094

3. “What are the Differences between DoS Protection and Zone Protection?” -
https://live.paloaltonetworks.com/docs/DOC-4501

4. PANOS 9.0 Admin Guide - Network Profiles / Zone Protection / Flood Protection :
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-web-interface-help/network/network-network-profiles/network-network-profiles-zone-protection/flood-protection.html#

6.18 Ensure that all zones have Zone Protection Profiles with all Reconnaissance Protection settings enabled, tuned, and set to appropriate actions 
----------------------------------------------------------------------------------------------------------------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1 

Description
^^^^^^^^^^^
Enable all three scan options in a Zone Protection profile. Do not configure an action of Allow for any scan type.
The exact interval and threshold values must be tuned to the specific environment. Less aggressive settings are
typically appropriate for trusted zones, such as setting an action of alert for all scan types. Attach appropriate
Zone Protection profiles meeting these criteria to all zones. Separate Zone Protection profiles for trusted and
untrusted zones is a best practice.

Rationale
^^^^^^^^^
Port scans and host sweeps are common in the reconnaissance phase of an attack. Bots scouring the Internet in search
of a vulnerable target may also scan for open ports and available hosts. Reconnaissance Protection will allow for
these attacks to be either alerted on or blocked altogether.

Audit
^^^^^
Navigate to Network > Network Profiles > Zone Protection > Zone Protection Profile > Reconnaissance Protection.

Verify that TCP Port Scan is enabled, its Action is set to block-ip, its Interval is set to 5, and its
Threshold is set to 20.

Verify that Host Sweep is enabled, its Action is set to block, its Interval is set to 10, and its
Threshold is set to 30.

Verify that UDP Port Scan is enabled, its Action is set to alert, its Interval is set to 10, and its
Threshold is set to 20.

Remediation
^^^^^^^^^^^
Navigate to Network > Network Profiles > Zone Protection > Zone Protection Profile > Reconnaissance Protection.

Set TCP Port Scan to enabled, its Action to block-ip, its Interval to 5, and its Threshold to 20.

Set Host Sweep to enabled, its Action to block, its Interval to 10, and its Threshold to 30.

Set UDP Port Scan to enabled, its Action to alert, its Interval to 10, and its Threshold to 20.

Impact
^^^^^^
Not configuring a Network Zone Protection Profile leaves an organization exposed to common attacks
and reconnaissance from untrusted networks.

Default Value
^^^^^^^^^^^^^
Not Configured 

References
^^^^^^^^^^
1. “Host Sweep Triggering Method in Zone Protection Profile” -
https://live.paloaltonetworks.com/docs/DOC-8703

2. “Understanding DoS Protection” -
https://live.paloaltonetworks.com/docs/DOC-5078

3. “Threat Prevention Deployment Tech Note” -
https://live.paloaltonetworks.com/docs/DOC-3094

4. “What are the Differences between DoS Protection and Zone Protection?” -
https://live.paloaltonetworks.com/docs/DOC-4501

5. PANOS 9.0 Admin Guide - Network Profiles / Zone Protection / Reconnaissance Protection:
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-web-interface-help/network/network-network-profiles/network-network-profiles-zone-protection/reconnaissance-protection.html#

6.19 Ensure all zones have Zone Protection Profiles that drop specially crafted packets 
----------------------------------------------------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1 

Description
^^^^^^^^^^^
For all zones, attach a Zone Protection Profile that is configured to drop packets with a spoofed IP address or a
mismatched overlapping TCP segment, and packets with malformed, strict source routing, or loose source routing
IP options set.

Rationale
^^^^^^^^^
Using specially crafted packets, an attacker may attempt to evade or diminish the effectiveness of network security
devices. Enabling the options in this recommendation lowers the risk of these attacks.

Audit
^^^^^
Navigate to

Network > Network Profiles > Zone Protection > Zone Protection Profile > Packet Based Attack Protection > TCP/IP Drop.

Verify Spoofed IP address is checked. Verify Mismatched overlapping TCP segment is checked. Under IP Option Drop,
verify that Strict Source Routing, Loose Source Routing, and Malformed are all checked. Additional options may
also be checked.

Remediation
^^^^^^^^^^^
Navigate to

Network > Network Profiles > Zone Protection > Zone Protection Profile > Packet Based Attack Protection > TCP/IP Drop.

Set Spoofed IP address to be checked. Set Mismatched overlapping TCP segment to be checked. Under IP Option Drop, s
et Strict Source Routing, Loose Source Routing, and Malformed to all be checked. Additional
options may also be set if desired.

Impact
^^^^^^
Not configuring a Network Zone Protection Profile leaves an organization exposed to common attacks and
reconnaissance from untrusted networks.

Default Value
^^^^^^^^^^^^^
Not Configured 

References
^^^^^^^^^^
1. “Understanding DoS Protection” -
https://live.paloaltonetworks.com/docs/DOC-5078

2. “Threat Prevention Deployment Tech Note” -
https://live.paloaltonetworks.com/docs/DOC-3094

3. “What are the Differences between DoS Protection and Zone Protection?” -
https://live.paloaltonetworks.com/docs/DOC-4501

4. PANOS 9.0 Admin Guide - Network Profiles / Zone Protection / Packet Based Attack Protection:
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-web-interface-help/network/network-network-profiles/network-network-profiles-zone-protection/packet-based-attack-protection.html#

6.20 Ensure that User Credential Submission uses the action of “block” or “continue” on the URL categories
----------------------------------------------------------------------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1 

Description
^^^^^^^^^^^
Ideally user names and passwords user within an organization are not used with third party sites.
ome sanctioned SAS applications may have connections to the corporate domain, in which case they will need to be
exempt from the user credential submission policy through a custom URL category.

Rationale
^^^^^^^^^
Preventing users from having the ability to submit their corporate credentials to the Internet could stop
credential phishing attacks and the potential that a breach at a site where a user reused credentials could
lead to a credential stuffing attack.

Audit
^^^^^
Navigate to Objects > Security Profiles > URL Filtering.

Choose the Categories tab. Verify that the User Credential Submitting action on all enabled URL
categories is set to either block or continue.

Under the User Credential Detection tab ensure the User Credential Detection is set to a value appropriate to
your organization, and is not set to Disabled.

Verify that the Log Severity value is set to a value appropriate to your organization and your logging or SIEM solution.

Remediation
^^^^^^^^^^^
Navigate to Objects > Security Profiles > URL Filtering.

Choose the Categories tab. Set the User Credential Submitting action on all enabled URL categories
is either block or continue, as appropriate to your organization and the category.

Under the User Credential Detection tab set the User Credential Detection value to a setting appropriate
to your organization, any value except Disabled. Set the Log Severity to a value appropriate to your
organization and your logging or SIEM solution.

Impact
^^^^^^
Not preventing users from submitting their corporate credentials to the Internet can leave them open to phishing
attacks or allow for credential reuse on unauthorized sites. Using internal email accounts provides malicious
actors with intelligence information, which can be used for phishing, credential stuffing and other attacks.
Using internal passwords will often provide authenticated access directly to sensitive information. Not only that,
but a pattern of credential re-use can expose personal information from multiple online sources.

Default Value
^^^^^^^^^^^^^
Not Configured 

References
^^^^^^^^^^
1. PAN OS 9.0 Admin Guide - URL Filtering / User Credential Detection:
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-web-interface-help/objects/objects-security-profiles-url-filtering/user-credential-detection.html#

7.1 Ensure application security policies exist when allowing traffic from an untrusted zone to a more trusted zone 
-------------------------------------------------------------------------------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1   Level 2 

Description
^^^^^^^^^^^
When permitting traffic from an untrusted zone, such as the Internet or guest network, to a more trusted zone, such
as a DMZ segment, create security policies specifying which specific applications are allowed. **Enhanced Security
Recommendation: ** Require specific application policies when allowing any traffic, regardless of the trust level
of a zone. Do not rely solely on port permissions. This may require SSL interception, and may also not be possible
in all environments.

Rationale
^^^^^^^^^
To avoid unintentionally exposing systems and services, rules allowing traffic from untrusted zones to trusted zones
should be as specific as possible. Application-based rules, as opposed to service/port rules, further tighten what
traffic is allowed to pass. Similarly, traffic from trusted to untrusted networks should have a security policy set,
with application-based rules. A "catch-all" rule that allows all applications will also allow malware traffic.
The goal should be to understand both inbound and outbound traffic, permit what is known, and block all other traffic.

Audit
^^^^^
Navigate to Policies > Security.

For all Security Policies that transit from a less trusted to a more trusted interface, that the appropriate
Application and Service values are set.

For instance, for a web server exposed to the internet from a DMZ:

Source tab: Zone set to OUTSIDE / Address set to Any

Destination tab: Zone set to DMZ / Address set to [DMZ Host Object]

Application tab: set to web-browsing

Service/URL Category tab: set Service to ether:

    * application-default or:

    * service-http and/or service-https

**Enhanced Security Recommendation: **

Assess this setting for Policies on all Interfaces,
for traffic in all directions. Ensure that for each Security Policy that the appropriate settings are set for
both Application and Service

Remediation
^^^^^^^^^^^
Navigate to Policies > Security.

For all Security Policies that transit from a less trusted to a more trusted interface,
set the Application and Service values to match the exposed application.
For instance, for a web server exposed to the internet from a DMZ:

Source tab: Zone set to OUTSIDE / Address set to Any

Destination tab: Zone set to DMZ / Address set to [DMZ Host Object]

Application tab: set to web-browsing

Service/URL Category tab: set Service to ether:

    * application-default or:
    * service-http and/or service-https

**Enhanced Security Recommendation: **
Set these values for Policies on all Interfaces, for traffic in all directions. For each Security Policy,
set the Application and Service values to match the exposed application.

Impact
^^^^^^
Setting application based rules on both inbound and outbound traffic ensures that the traffic on the protocol
and port being specified is actually the application that you expect. For outbound traffic, the days of
"we trust our users" is well past us, that statement also implies that we trust the malware on the user
workstations, which is obviously not the case. For traffic from trusted to less trusted interfaces, the applications
should be characterized over time, with the end goal being that all applications in in the rules, and a final
"block all" rule is in place. Not having this goal gives both attackers and malware the leeway they need to
accomplish their goals. Trusting only Port permissions to control traffic exposes an organization to "tunneling"
style attacks that can exfiltrate data or facilitate Command and Control (C2) sessions.

Default Value
^^^^^^^^^^^^^
Not Configured 

References
^^^^^^^^^^
1. “PAN-OS Administrator's Guide 9.0 (English) - Security Policies / Applications and Usage ” -
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-web-interface-help/policies/policies-security/applications-and-usage.html#

7.2 Ensure 'Service setting of ANY' in a security policy allowing traffic does not exist 
-----------------------------------------------------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1 

Description
^^^^^^^^^^^
Create security policies specifying application-default for the Service setting, in addition to the specific ports
desired. The Service setting of any should not be used for any policies that allow traffic.

Rationale
^^^^^^^^^
App-ID requires a number of packets to traverse the firewall before an application can be identified and either
allowed or dropped. Due to this behavior, even when an application is defined in a security policy, a service setting
of any may allow a device in one zone to perform ports scans on IP addresses in a different zone. In addition, this
recommendation helps to avoid an App-ID cache pollution attack. Because of how App-ID works, configuring the service
setting to "Any" allows some initial traffic to reach the target host before App-ID can recognize and appropriately
restrict the traffic. Setting the Service Setting to application specific at least restricts the traffic to the
target applications or protocols for that initial volume of traffic.

Audit
^^^^^
Navigate to Policies > Security.

For each exposed host, verify that a Security Policy exists with:

    * Source tab: Zone set to OUTSIDE Address set to any
    * Destination tab: Zone set to DMZ / Address set to <DMZ Host Object>
    * Application tab: Application set to web-browsing (or appropriate application)
    * Service tab: Service set to application-default. The value of any should never be used

Remediation
^^^^^^^^^^^
Remediation:

Navigate to Policies > Security.

For each exposed host, set a Security Policy exists with:

    * Source tab: Zone set to OUTSIDE Address set to any
    * Destination tab: Zone set to DMZ / Address set to <DMZ Host Object>
    * Application tab: Application set to web-browsing (or appropriate application)
    * Service tab: Service set to application-default. The value of any should never be used


Default Value
^^^^^^^^^^^^^
Not Configured 

References
^^^^^^^^^^

1. “Security Policy Guidelines” -
https://live.paloaltonetworks.com/docs/DOC-3469

2. “Security Bulletin: App-ID Cache Pollution” -
http://researchcenter.paloaltonetworks.com/2012/12/app-id-cache-pollution-response/

3. “PAN-OS Administrator's Guide 9.0 (English) - Security Policiy Overview ” -
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-web-interface-help/policies/policies-security/security-policy-overview.html#


7.3 Ensure 'Security Policy' denying any/all traffic to/from IP addresses on Trusted Threat Intelligence Sources Exists 
------------------------------------------------------------------------------------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1 

Description
^^^^^^^^^^^
Create a pair of security rules at the top of the security policies ruleset to block traffic to and from IP addresses
known to be malicious. Note: This recommendation (as written) requires a Palo Alto "Active Threat License".
Third Party and Open Source Threat Intelligence Feeds can also be used for this purpose.

Rationale
^^^^^^^^^
Creating rules that block traffic to/from known malicious sites from Trusted Threat Intelligence Sources protects
you against IP addresses that Palo Alto Networks has proven to be used almost exclusively to distribute malware,
initiate command-and-control activity, and launch attacks.

Audit
^^^^^
Navigate to Policies > Security

Verify a Security Policy exists similar to:

    * General tab: Name set to Deny to Malicious IP
    * Source tab: Source Zone set to Any,
    * Destination tab: Destination Zone set to Any,
    * Destination Address set to Palo Alto Networks - Known malicious IP addresses
    * Application tab: Application set to Any
    * Service/URL Category tab: Service set to Any
    * Actions tab: Action set to Block, Profile Type set to None
    * Verify a Security Policy exists with:
    * General tab: Name set to Deny from Malicious IP
    * Source tab: Source Zone set to Any, Source Address set to Palo Alto Networks - Known malicious IP addresses
    * Destination tab: Destination Zone set to Any
    * Application tab: Application set to Any
    * Service/URL Category tab: Service set to Any
    * Actions tab: Action set to Block, Profile Type set to None

Note: This recommendation requires a Palo Alto "Active Threat License"

Remediation
^^^^^^^^^^^
Navigate to Policies > Security

Create a Security Policy similar to:

    * General tab: Name set to Deny to Malicious IP
    * Source tab: Source Zone set to Any,
    * Destination tab: Destination Zone set to Any,
    * Destination Address set to Palo Alto Networks - Known malicious IP addresses
    * Application tab: Application set to Any
    * Service/URL Category tab: Service set to Any
    * Actions tab: Action set to Block, Profile Type set to None

Create a Security Policy similar to with:

    * General tab: Name set to Deny from Malicious IP
    * Source tab: Source Zone set to Any, Source Address set to Palo Alto Networks - Known malicious IP addresses
    * Destination tab: Destination Zone set to Any
    * Application tab: Application set to Any
    * Service/URL Category tab: Service set to Any
    * Actions tab: Action set to Block, Profile Type set to None Note:

This recommendation requires a Palo Alto "Active Threat License"

Impact
^^^^^^
While not foolproof, simply blocking traffic from known malicious hosts allows more resources to be devoted
to analyzing traffic from other sources for malicious content. This approach is a recommended part of most
"Defense in Depth" recommendations, allowing defenders to focus more deeply on traffic from uncategorized sources.

Default Value
^^^^^^^^^^^^^
Not Configured      

References
^^^^^^^^^^
1. "PAN-OS 9.0 Admin Guide: Built-in External Dynamic Lists":
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/policy/use-an-external-dynamic-list-in-policy/built-in-edls.html#

2. "PAN-OS 9.0 Admin Guide: Create Rules Based on Trusted Threat Intelligence Sources":
https://docs.paloaltonetworks.com/best-practices/9-0/internet-gateway-best-practices/best-practice-internet-gateway-security-policy/define-the-initial-internet-gateway-security-policy/step-1-create-rules-based-on-trusted-threat-intelligence-sources.html#

8.1 Ensure 'SSL Forward Proxy Policy' for traffic destined to the Internet is configured 
-----------------------------------------------------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1 

Description
^^^^^^^^^^^
Configure SSL Forward Proxy for all traffic destined to the Internet. In most organizations, including all categories
except financial-services, government and health-and-medicine is recommended.

Rationale
^^^^^^^^^
Without SSL inspection, the firewall cannot apply many of its protection features against encrypted traffic.
The amount of encrypted malware traffic continues to rise, and legitimate websites using SSL encryption are hacked
or tricked into delivering malware on a frequent basis. As encryption on the Internet continues to grow at a rapid
rate, SSL inspection is no longer optional as a practical security measure. If proper decryption is not configured,
it follows that the majority of traffic is not being fully inspected for malicious content or policy violations.
This is a major exposure, allowing delivery of exploits and payloads direct to user desktops.

Audit
^^^^^
Navigate to Policies > Decryption.

Verify SSL Forward Proxy is set for all traffic destined to the Internet.

Verify each Decryption Policy Rule:

Source tab:

    * The Source Zone and/or Source Address should include all target internal networks.
    * Source User should include all target internal users

Destination tab:

    * The Destination Zone should include the untrusted target zone (usually the internet).
    * Destination Address is typically Any for an internet destination.

Service/URL Category tab:

    * Verify that all URL Category entries are included except financial-services, government and
health-and-medicine (this list may vary depending on your organization and its policies).

Options tab:

    * Verify that the Type is set to SSL Forward Proxy

Remediation
^^^^^^^^^^^
Navigate to Policies > Decryption. Create a Policy for all traffic destined to the Internet.

This Policy should include:

Source tab:

    * The Source Zone and/or Source Address should include all target internal networks.
    * Source User should include all target internal users

Destination tab:

    * The Destination Zone should include the untrusted target zone (usually the internet).
    * Destination Address is typically Any for an internet destination.

Service/URL Category tab:

    * all URL Category entries should be included except financial-services, government and
    * health-and-medicine (this list may vary depending on your organization and its policies).

Options tab:

    * Type set to SSL Forward Proxy

Impact
^^^^^^
Failure to decrypt outbound traffic allows attackers to mask attacks, data exfiltration and/or command
and control (C2) traffic by simply using standard TLS encryption. Privacy concerns for your organization's
users will dictate that some common categories should be exempted from inspection and decryption. Personal
banking or healthcare information is almost always exempted, as are interactions with government entities.
Exemptions and inclusions to decryption policies should be negotiated internally and governed by published
Corporate Policies.

Default Value
^^^^^^^^^^^^^
Not Configured 

References
^^^^^^^^^^
1. “How to Implement SSL Decryption” -
https://live.paloaltonetworks.com/docs/DOC-1412

2. ““PAN-OS Administrator's Guide 9.0 (English) - Decryption (English)” -
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/decryption.html#

8.2 Ensure 'SSL Inbound Inspection' is required for all untrusted traffic destined for servers using SSL or TLS 
----------------------------------------------------------------------------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1 

Description
^^^^^^^^^^^
Configure SSL Inbound Inspection for all untrusted traffic destined for servers using SSL or TLS. 

Rationale
^^^^^^^^^
Without SSL Inbound Inspection, the firewall is not able to protect SSL or TLS-enabled webservers against many threats. 

Audit
^^^^^
Navigate to Policies > Decryption.

Verify SSL Inbound Inspection is set appropriately for all untrusted traffic destined for servers using SSL or TLS.

Navigate to Policies > Decryption.

For each service published to the internet (or other untrusted zones), verify the following settings:

General tab: Name set to a descriptive name

Source: Source Zone set to the target zone (Internet in many cases).
Source Address set to the target address space (Any for internet traffic)

Destination tab: Destination Zone should be set to the appropriate zone, or Any. Destination Address set to the
target host address  Options tab: Type set to SSL Inbound Inspection

Remediation
^^^^^^^^^^^
Navigate to Policies > Decryption.

Set SSL Inbound Inspection appropriately for all untrusted traffic destined for servers using
SSL or TLS.

Navigate to Policies > Decryption.

For each service published to the internet (or other untrusted zones),
create a Policy and set the following options:

General tab: Name set to a descriptive name

Source: Source Zone set to the target zone (Internet in many cases). Source Address set to the target address
space (Any for internet traffic)

Destination tab: Destination Zone should be set to the appropriate zone, or Any.
Destination Address set to the target host address

Options tab: Type set to SSL Inbound Inspection

Impact
^^^^^^
Not decrypting inbound traffic to TLS encrypted services means that inspection for many common attacks
cannot occur on the firewall. This means that all defenses against these attacks are up to the host.

Default Value
^^^^^^^^^^^^^
Not Configured 

References
^^^^^^^^^^
1. “How to Implement SSL Decryption” -
https://live.paloaltonetworks.com/docs/DOC-1412

2. “PAN-OS Administrator's Guide 9.0 (English) - Decryption (English)” -
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/decryption.html#

8.3 Ensure that the Certificate used for Decryption is Trusted 
---------------------------------------------------------------

Scored/Not Scored
^^^^^^^^^^^^^^^^^
(Not Scored)

Profile Applicability
^^^^^^^^^^^^^^^^^^^^^
Level 1   Level 2 

Description
^^^^^^^^^^^
The CA Certificate used for in-line HTTP Man in the Middle should be trusted by target users. For SSL Forward
Proxy configurations, there are classes of users that need to be considered. 1: Users that are members of the
organization, users of machines under control of the organization. For these people and machines, ensure that the
CA Certificate is in one of the Trusted CA certificate stores. This is easily done in Active Directory,
using Group Policies for instance. A MDM (Mobile Device Manager) can be used to accomplish the same task for
mobile devices such as telephones or tablets. Other central management or orchestration tools can be used for
Linux or "IoT" (Internet of Things) devices. 2: Users that are not member of the organization - often these are
classed as "Visitors" in the policies of the organization. If a public CA Certificate is a possibility for your
organization, then that is one approach. A second approach is to not decrypt affected traffic - this is easily done,
but leaves the majority of "visitor" traffic uninspected and potentially carrying malicious content.

The final approach, and the one most commonly seen, is to use the same certificate as is used for the hosting
organization. In this last case, visitors will see a certificate warning, but the issuing CA will be the
organization that they are visiting.

Rationale
^^^^^^^^^
Using a self-signed certificate, or any certificate that generates a warning in the browser, means that
members of the organization have no method of determining if they are being presented with a legitimate
certificate, or an attacker's "man in the middle' certificate. It also very rapidly teaches members of the
organization to bypass all security warnings of this type.

Audit
^^^^^
Verify the CA Certificate(s):

Navigate to Device > Certificate Management > Certificates

Verify that appropriate internal certificates are imported, and that all certificates in the
list are valid. In particular, verify the Subject, Issuer, CA, Expires, Algorithm and Usage fields
Alternatively, if an internal CA is implemented on the firewall, verify that target clients have the
root certificate for this CA imported into their list of trusted certificate authorities.

Verify the Certificate Profile needed for the SSL Forward Proxy:

Navigate to Device > Certificate Management > Certificate Profile.

Verify that an appropriate profile is created.

Remediation
^^^^^^^^^^^
Set the CA Certificate(s): Navigate to Device > Certificate Management > Certificates.

Import the appropriate CA Certificates from any internal Certificate Authorities.

Alternatively, generate a self-signed certificate for an internal CA on the firewall,
and then import the root certificate for that CA into the trusted CA list of target clients.
In an Active Directory environment this can be facilitated using a Group Policy.

Set the Certificate Profile needed for the SSL Forward Proxy:

Navigate to Device > Certificate Management > Certificate Profile.

Set the decryption profile to include the settings described in the SSL Forward Proxy guidance in this document


Default Value
^^^^^^^^^^^^^
Decryption is not enabled by default.       

References
^^^^^^^^^^
1. "How to Implement and Test SSL Decryption" -
https://live.paloaltonetworks.com/t5/Configuration-Articles/How-to-Implement-and-Test-SSL-Decryption/ta-p/59719

2. “PAN-OS Administrator's Guide 9.0 (English) - Decryption (English)” -
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/decryption.html#

3. "SSL Certificates Resource List on Configuring and Troubleshooting" -
https://live.paloaltonetworks.com/t5/Management-Articles/SSL-certificates-resource-list/ta-p/53068

4. "Certificates" -
http://palo-alto.wikia.com/wiki/Certificates
