VM-50 Security Profile Limits
=============================

IronSkillet includes a broad set of security profiles to simplify the usage in security policies. However, the VM-50 limits
the number of security profiles that can be configured to 38 resulting in possible commit errors if this limit is exceeded.

.. Note::
    If > 49 profiles, the user may see an error message that the number of profiles (39) exceeds capacity (38). This is
    an error in the message output and the user will have to remove enough profiles for the 38 count limit.

.. Note::
    Make sure the firewall is licensed. An unlicensed firewall will allow only 20 profiles, far below what is configured
    with IronSkillet.


The `delete` commands below can be used to delete security profiles and profile groups from an IronSkillet template load
that may not be required for a basic VM-50 configuration yet allow for a reduced number of profiles.

Copy/paste all or part of these commands into the console before any of the profiles or profiles groups are referenced by
other items in the configuration. This will leave the Outbound, Inbound, and Alert-Only profiles in the configuration.

This frees up space for nine other security profiles not part of IronSkillet.

.. parsed-literal::

    delete profile-group Internal
    delete profiles virus Internal-AV
    delete profiles spyware Internal-AS
    delete profiles vulnerability Internal-VP
    delete profiles file-blocking Internal-FB
    delete profiles wildfire-analysis Internal-WF
    delete profiles virus Exception-AV
    delete profiles spyware Exception-AS
    delete profiles vulnerability Exception-VP
    delete profiles url-filtering Exception-URL

