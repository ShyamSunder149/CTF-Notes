from pwn import *
from binascii import unhexlify
from Crypto.Cipher import AES

re = remote('gc1.eng.run',30529)


context.log_level = 'DEBUG'
re.recvline()
re.recvuntil(b'\n')
c = re.recvline()
c = c.strip(b'\n')
c = unhexlify(c.strip(b'\n'))
re.recv(1024)
p1 = (c[:16]+b'b'*64)
re.sendline(str(p1.hex()))
c1 = re.recvline()
c1 = unhexlify(c1.strip(b'\n'))
re.recv(1024)
key1 = xor(c1[:16],p1[16:32])
part1 = xor(key1,c[16:32])
key2 = xor(c1[16:32],p1[32:48])
part2 = xor(key2,c[32:48])
key3 = xor(c1[32:48],p1[48:52])
part3 = xor(key3,c[48:52])
print(part1+part2+part3)
print(len(c1))
print(len(c))
