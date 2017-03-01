pytotp
======

Important: DO NOT USE. This is not a secure way to do this, and was written as a proof of concept. The code has a number of significant issues that should prevent using this, including a significant timing-attack string comparison. It is also not maintained, so this might be useful only for reference of how _not_ to do it.


Google Authenticator TOTP functions for Python

This module is a very small, easy to use way to get TOTP coges for Google Authenticator in python.

Functions and  based on those provided by:
https://github.com/chregu/GoogleAuthenticator.php

Example:

    import pytotp
    secret = pytotp.generate_secret()
    code = pytotp.get_code(secret)
    
    if pytotp.check_code(secret, '123456'):
        print('success!')
    
