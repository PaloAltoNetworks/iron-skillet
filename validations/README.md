# IronSkillet Validations

Validation skillets allow the user to map configuration files against
a set of validation rules.

Key use cases are missing configuration elements based on best practices,
missing configuration elements for later stage config dependencies, or
potential merge conflicts of same-named rules and objects.

### Full IronSkillet configuration assessment

This validation skillet provides a comprehensive analysis of a NGFW configuration
compared to IronSkillet. This includes device hardening, security profiles,
and other recommended day one practices.

The documentation links map to the visual guide allowing the user to manually
remediate any 'fail' state config items.

### Upgrade to 9.0 Missing Elements

This is a partial validation that only looks at new items added between
PAN-OS 8.1 and 9.0. Users can opt to manually remediate missing
elements using links to the visual guide.

