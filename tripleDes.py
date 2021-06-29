from des import DesKey

key = DesKey(b'password password passwo')

msg = b'hello world!'

ct = key.encrypt(msg,padding=True)

print(ct)

pt = key.decrypt(ct,padding=True)

print(pt.decode())
