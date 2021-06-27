from pwn import xor

#single byte xor bruteforcing ascii characters

msg = 'awesomepassword'

ct = b''
pt = b''

for i in range(128):
	print(xor(chr(i),msg))
