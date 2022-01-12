from binascii import unhexlify
from Crypto.Cipher import AES

re = remote('gc1.eng.run',30193)

def encrypt(msg, iv):
    cipher = AES.new(key, AES.MODE_OFB,iv)
    ct = cipher.encrypt(msg)
    return ct if ct not in flag else b"try_harder"

def decrypt(msg, iv, key):
    cipher = AES.new(key, AES.MODE_OFB,iv)
    ct = cipher.decrypt(msg)
    return ct


context.log_level = 'DEBUG'
re.recvline()
re.recvuntil(b'\n')
c = re.recvline()
c = c.strip(b'\n')
c = unhexlify(c.strip(b'\n'))

re.recv(1024)
p1 = (c[:16]+b'b'*16)
re.sendline(str(p1.hex()))
c1 = re.recvline()
c1 = unhexlify(c1.strip(b'\n'))
re.recv(1024)
key1 = xor(c1,p1[16:])
part1 = xor(key1,c[16:32])
part2 = decrypt(c[16:32],c[:16],key1)
print(part1)
print(part2)
print(len(c))
