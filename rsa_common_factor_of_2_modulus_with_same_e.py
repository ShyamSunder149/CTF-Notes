import gmpy2
from Crypto.PublicKey import RSA
from Crypto.Util.number import *
key1 = open('key1.pub','rb').read()
pub1 = RSA.importKey(key1)
key2 = open('key2.pub','rb').read()
pub2 = RSA.importKey(key2)
n = pub1.n
e1 = pub1.e
e2 = pub2.e
c1 = bytes_to_long(open('flag.txt.key1.enc','rb').read())
c2 = bytes_to_long(open('flag.txt.key2.enc','rb').read())
message1 = c1
message2 = c2
gcd, s, t = gmpy2.gcdext(e1, e2)
if s < 0:
    s = -s
    message1 = gmpy2.invert(message1, n)
if t < 0:
    t = -t
    message2 = gmpy2.invert(message2, n)
plain = gmpy2.powmod(message1, s, n) * gmpy2.powmod(message2, t, n) % n
plain = gmpy2.iroot(gmpy2.mpz(plain),3)[0] #try taking this line if the exploit doesnt work
print(long_to_bytes(plain))
