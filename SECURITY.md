# Security Policy

## Overview

Bad Apple takes security and privacy very seriously, and goes to great lengths to help protect its visitors. Some of the many measures in place to protect our users include:

- Only pushing data to our servers that is meant to be public anyways
- Implementing a strict logging policy, whereby all logs containing identifying information on our legitimate users (such as IP addresses) are shredded every 24 hours. By default, all other logs are also shredded within a day, and no log is allowed to last more than two weeks. The shredding process involves removing the file and writing-over the disc space it occupied 7 times with randomized data, rendering the file totally unrecoverable.
- Running our website as an onion service (and with no dependency on JavaScript)
- Only allowing secure, end-to-end encrypted connections to our website
- Automatically encrypting all submitted tips in memory, before saving them (temporarily) to the database. The tips are encrypted with asymmetric cryptography, and the private keys needed to view those tips are stored securely, independently, and offline.
- Hosting our own DNS records (and using DNSSEC)
- Not using analytics or resources hosted by anyone other than ourselves



## Reporting a Vulnerability

Please report security vulnerabilities to Admin@BadApple.tools, or by [Submitting a Tip](https://badapple.tools/Tip/). Do **NOT** create an issue or discussion to report a security vulnerability.

When reporting a vulnerability via email, you are welcome to use [our GPG key](https://raw.githubusercontent.com/P5vc/ServerConfigurations/main/modules/gpg/BadAppleTips1.asc), if the contents of the email is sensitive. If you choose to report the vulnerability by submitting a tip, there is no need to encrypt your message, as all submitted messages are automatically encrypted. For high severity vulnerabilities that require immediate action, email and/or Signal (+1 (336) 439-8765) are preferred, as they are checked more frequently.
