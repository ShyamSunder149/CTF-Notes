from pwn import xor

#single byte xor

msg = 'awesomepassword'
key = '9'

ct = b''
pt = b''

ct = xor(msg,key)
pt = xor(ct,key)


print(ct.decode())
print(pt.decode())
