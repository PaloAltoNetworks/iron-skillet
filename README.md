# Day One Templates for Panorama and Panos devices.

The Palo Alto Networks NGFW provides a wealth of features and capabilities well beyond what is provided in a legacy or single function firewall. Although highly beneficial from a security posture and operations perspective, the learning curve for the various features can be higher than a single function device.

Best practice recommendations for configuration can be found online for Internet Gateway, Datacenter, Wildfire, L4-L7 evasions and other use cases.

[Best Practice Recommendations](https://www.paloaltonetworks.com/documentation/best-practices)

While useful as suggestions and recommendations, the user is still required to manually use the GUI or CLI to configuration each recommendation.

The goal of iron-skillet is to create a template model for the most common, user agnostic elements. These templates can be easily loaded into a firewall or Panorama minimizing time to configure and user error. The repo stores the raw xml for each configuration element along with a full configuration file.

Loading the configuration snippets can be done in multiple ways using the xml format. See the repo wiki for more information.
[Iron Skillet Github Wiki](https://github.com/PaloAltoNetworks/iron-skillet/wiki "Iron Skillet Wiki")

### Version Support
The templates are specific to PAN-OS and Panorama 8.0 and also can be used for 8.1. Currently no template support for 7.1 or prior releases.

### Custom Reports
The folder custom reports contains additional reports that can be loaded along with the base templates. Currently the reports support a single zone exception with additional work and toolkits to add in multiple zones/subnets to provide a better data experience.

# Support Policy
The code and templates in the repo are released under an as-is, best effort, support policy. These scripts should be seen as community supported and Palo Alto Networks will contribute our expertise as and when possible. We do not provide technical support or help in using or troubleshooting the components of the project through our normal support options such as Palo Alto Networks support teams, or ASC (Authorized Support Centers) partners and backline support options. The underlying product used (the VM-Series firewall) by the scripts or templates are still supported, but the support is only for the product functionality and not for help in deploying or using the template or script itself. Unless explicitly tagged, all projects or work posted in our GitHub repository [](at https://github.com/PaloAltoNetworks) or sites other than our official Downloads page on [](https://support.paloaltonetworks.com) are provided under the best effort policy.
