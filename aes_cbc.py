import random
from Crypto.Cipher import AES
iv = b'mainmainmainmain'
key = b'passwordpassword'
msg = b'hello world 1234'
aes = AES.new(key, AES.MODE_CBC, iv)
ct = aes.encrypt(msg)
print(ct)
cipher = AES.new(key, AES.MODE_CBC, iv)
pt = cipher.decrypt(ct)
print(pt)
