pytotp
======

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
    
