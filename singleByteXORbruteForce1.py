from pwn import xor

#single byte xor bruteforcing ascii characters with known plaintext

msg = 'awesomepassword'


for i in range(128):
	ct = xor(chr(i),msg)
	if b'awesome' in ct:
		print(ct)
