#!/usr/bin/python2
import math
import time
import base64
import struct
import hmac
import hashlib
import urllib
import random

pass_code_length = 6
secret_length = 10

def check_code(secret, code):
    code = str(code)
    current_time = math.floor(time.time() / 30);
    if get_code(secret, current_time) == code:
        return True
    return False
    
def get_code(secret, current_time = None):
    if not current_time:
        current_time = math.floor(time.time() / 30);
    secret = base64.b32decode(secret)
    current_time = struct.pack('>L', current_time)
    current_time = current_time.rjust(8,chr(0))
    
    hash = hmac.new(secret, current_time, hashlib.sha1).digest()
    
    offset = ord(hash[-1])
    offset = offset & 0xF
    chunk = hash[offset:offset+4]
    trunc = struct.unpack('>L', chunk)
    trunc = (trunc[0] & 0x7FFFFFFF) % (10 ** pass_code_length);
    trunc = str(trunc).rjust(6,'0')
    return trunc
    
def get_url(secret, user, hostname, size=200):
    secret = urllib.quote(secret)
    user = urllib.quote(user)
    hostname = urllib.quote(hostname)
    
    if size ** 2 > 300000:
        size = 547
    size = str(size)
    
    url = "http://chart.apis.google.com/chart?chs="+size+"x"+size+"&chld=M|0&cht=qr&chl=otpauth://totp/" + user + "@" + hostname + "%3Fsecret%3D" + secret
    return url
    
def generate_secret():
    secret = "".join(chr(random.randrange(0, 256)) for i in xrange(secret_length))
    return base64.b32encode(secret)
    
