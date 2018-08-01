# this dictionary contains a list of variables with default values
# these are found in the xml configs with {{ value }}

xmlvar = {
    # These are default username and password values for the sample outputs
    # The user will be prompted for the actual password when the script is run
    "ADMINISTRATOR_USERNAME": "iron-skillet",
    "ADMINISTRATOR_PASSWORD": "fortheloveofallthingsholychangeme",
    # MY_CONFIGDIR is the prefix to the my_template output folder
    "MYCONFIG_DIR": "sample-cloud-AWS",
    "FW_NAME": "sample",
    "DEVICE_GROUP": "sample",
    "TEMPLATE": "sample",
    "DNS_1": "8.8.8.8",
    "DNS_2": "8.8.4.4",
    "NTP_1": "0.pool.ntp.org",
    "NTP_2": "1.pool.ntp.org",
    "SINKHOLE_IPV4": "72.5.65.111",
    "SINKHOLE_IPV6": "2600:5200::1",
    "EMAIL_PROFILE_GATEWAY": "192.0.2.1",
    "EMAIL_PROFILE_FROM": "test@yourdomain.com",
    "EMAIL_PROFILE_TO": "test@yourdomain.com",
    "SYSLOG_SERVER": "192.0.2.2",
    # IP address or hostname for config bundle export
    "CONFIG_EXPORT_IP": "192.0.2.3",
    # MGMT_TYPE values: static, dhcp-cloud, or dhcp-client
    # If static: IP, mask, and default-gateway added to config
    # If dhcp-cloud: includes dhcp-client requires for cloud deployments
    # If dhcp-client: these values are ignored
    "MGMT_TYPE": "dhcp",
    "MGMT_IP": "192.168.55.10",
    "MGMT_MASK": "255.255.255.0",
    "MGMT_DG": "192.168.55.2",
    # Panorama Management IP Address Info
    # Set CONFIG _PANORAMA_IP to yes to include in config
    # If set to no will not add which may be required for partial config loads
    "CONFIG_PANORAMA_IP": "yes",
    # Panorama types are cloud or standard
    # Cloud adds in initcfg bootstrap elements for Panorama
    "PANORAMA_TYPE": "cloud",
    "PANORAMA_NAME": "panorama-cloud",
    "PANORAMA_IP": "192.168.55.7",
    "PANORAMA_MASK": "255.255.255.0",
    "PANORAMA_DG": "192.168.55.2",

}
