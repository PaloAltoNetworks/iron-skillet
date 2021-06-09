# Playlist with Skillet Includes

Starting with IronSkillet 10.1, skillets are now available in a playlist format. In this new playlist model, it is 
possible to reference a set of sub-skillets from a submodule though skillet includes. A git submodule allows content 
from one repository to be easily accessed and updated from another repository. For IronSkillet, the 
playlists in this directory reference sub-skillets from a submodule called 
[ironskillet-components](https://github.com/PaloAltoNetworks/ironskillet-components). In 
ironskillet-components, there is a set of panos sub-skillets and a set of panorama sub-skillets that contain the XML 
snippets used in IronSkillet. See the panos and panorama template pages for details on what is included in each sub-skillet.


Several playlists were created for panos and panorama using the sub-skillets from ironskillet-componenets, which allows 
for flexibility in choosing which XML snippets are pushed in a configuration. The playlist model allows for both the full 
IronSkillet configuration and more targeted configurations around security policies and device hardening to be created 
and updated from the same set of snippets. Each playlist is listed below, along with a short description.


**Overview of the panos Playlists**
* `panos_full_skillet`: Traditional full IronSkillet playlist for panos
* `panos_device_hardening`: Contains only device hardening sub-skillets
    * subset of the panos_shared_full playlist
* `panos_security_profiles`: Contains only the security profile sub-skillets
    * subset of the panos_shared_full playlist
* `panos_alert_only`: Contains only the alert only security profiles from the sub-skillets
    * subset of the panos_shared_full playlist

**Overview of the panorama Playlists**
* `panorama_shared_full`: Traditional full IronSkillet playlist for panorama using shared device-group and template configurations
    * used in loadable and full configs
* `panorama_shared_dgtemplate`: Contains only device group and template sub-skillets
    * subset of the panorama_shared_full playlist
    * used to add shared device-group and baseline template content without Panorama system elements
* `panorama_notshared_full`: Traditional full IronSkillet playlist for panorama with nothing shared
    * includes the device-group and stack containing all configuration elements
* `panorama_notshared_dgstack`: Contains only device group and template stack sub-skillets
    * subset of the panorama_notshared_full playlist
    * used to add additional device-groups and stack, each with full configuration elements
* `panorama_device_hardening`: Contains only device hardening sub-skillets
    * subset of the panorama_shared_full playlist
* `panorama_shared_security_profiles`: Contains only the security profile sub-skillets
    * subset of the panorama_shared_full playlist
  
Users are welcome to create their own playlists to mix and match elements that are not specified above. The 
[panos template](https://iron-skillet.readthedocs.io/en/docs_master/panos_template_guide.html)
and [panorama template](https://iron-skillet.readthedocs.io/en/docs_master/panorama_template_guide.html) pages 
have an overview of all the sub-skillets available in ironskillet-components to include in a playlist.

Also, see the [Playlist Includes Tutorial](https://skilletbuilder.readthedocs.io/en/latest/tutorials/tutorial_includes.html)
from [SkilletBuilder] for more information on playlists, includes, submodules, and how they all work together. The 
tutorial shows how to use the playlist model to build configurations for IronSkillet.



