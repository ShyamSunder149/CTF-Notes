from pwn import xor

#single byte xor

msg = 'awesomepassword'
key = '9'

ct = b''
pt = b''

for i in msg:
	ct += xor(i,key)

for i in ct:
	pt += xor(i,key)


print(ct.decode())
print(pt.decode())
