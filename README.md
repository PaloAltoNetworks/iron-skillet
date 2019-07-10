# Brute Force Exceptions

set of simple skillets as placeholder for IronSkillet.

These skillets are the complete 9.0 vulnerability profiles with
the exceptions included as of the commite date.

### xml snippets

this skillet can be used with panhandler or similar tools to do a quick
load of the profiles using the API

### set commands

this skillet doesn't have variables so can be loaded as is. If the profiles
are already configured, then only the exception elements can be loaded.

```NOTE:``` if a threat ID associated signature is removed from the
signature database, a commit warning will show the missing IDs. No harm
to the commit and these IDs can remain in the event they are active in the
future.
