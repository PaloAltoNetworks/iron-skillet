General device configuration
============================

This section provides templated configurations for general device settings.


Security-related Device Settings
--------------------------------

.. _device_setting: https://github.com/scotchoaf/iron-skillet/blob/rev-1.0.1/v8/panos/snippets-variables/device_setting.xml

device_setting_.xml

General device settings that effect security posture. Found in Device > Setup in the GUI.

- X-Forwarded-For: To ensure that attackers can’t read and exploit the XFF values in web request packets that exit the firewall.
Enable the firewall to use XFF values in policies and in the source user fields of logs Remove XFF values from outgoing web requests.

- Wildfire: set optimal file size limits for Wildfire uploads and show verdict responses for grayware, malware and phishing


- Session rematch: the firewall will go through all the existing sessions and apply the new security policy to any matching traffic

- Notify User: user should be notified when web-application is blocked; enables the application response page 

- Log Suppression: disabled to ensure unique log entries even if similar session types



Docker
------

.. _Docker: https://docker.io

The fastest way to start this tool is using Docker_. New container images are built periodically and will always be up
to date.

.. code-block:: bash
    docker build -t panos_bootstrapper:v0.4 .
    docker run --entrypoint python -p 8002:5000 --name panos_bootstrapper panos_bootstrapper:v0.4 /app/bootstrapper/bootstrapper.py


Standalone
----------

For local development, start the tool directly using these commands:

.. code-block:: bash
    export FLASK_APP=./bootstrapper/bootstrapper.py
    flask run --host=0.0.0.0 --port=5002

This will start the API and listen on all interfaces on port 5002. Browsing to http://localhost:5002 will show the
OpenAPI 2.0 documentation.


System Configuration
--------------------

device_system.xml
System configuration settings for dynamic updates and network services (eg. DNS, NTP).
   Update schedule settings: Turn on all telemetry settings; recommended dynamic updates schedule for threats, AV, and Wildfire
Use SNMPv3
Set default DNS and NTP values
Set timezone to UTC


Logging
-------

Logging best practice configurations for logging output and forwarding profiles.
Configure Logging profiles before Security Rules
The template creates a log forwarding profile call default. This profile is referenced in the template security rules and should be configured before the security rules.
Logging can be Deployment Dependent
The destination in the logging profile is templated to a syslog server. This can vary based on actual deployment scenarios.
log_settings_profiles.xml
Log forward profile referenced in security rules to determine where to forward log related events.
Forward all log activity to syslog (see the reference syslog configuration in shared_log_settings.xml)
Email malicious and phishing Wildfire verdicts to the address in the email profile (see shared_log_settings.xml)
shared_log_settings.xml
Device event logging including sample profiles for email and syslog forwarding.
Reference syslog profile that can be edited for a specific IP address and UDP/TCP port Reference email profile that can be edited for specific email domain and user information System, configuration, user, HIP, and correlation log forwarding to syslog
Email critical system events to the email profile