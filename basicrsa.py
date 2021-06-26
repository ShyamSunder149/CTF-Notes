from Crypto.Util.number import inverse,GCD		#Crypto library for RSA
from sympy import factorint						#factorint for factoring primes

p = 3
q = 7
n = p*q
e = 2
pt = 12

print("N value:",n)
y,z = factorint(n).keys()						#Calculating factors of n using sympy or primefac
print("Factors:",y,z)

phi = (p-1)*(q-1)

while(e<phi):									#How e is calculated
	if(GCD(e,phi)==1):							#GCD is a inbuilt function to give gcd of 2 numbers
		break
	else:
		e=e+1

print("Plaintext:",pt)

k = 2											#some constant
d = inverse(e,phi)								#Caluculation of d the private key; Return the inverse of e mod phi.

ct = pow(pt,e,n)								#Following (p^e)%n for encryption
print("ciphertext:",ct)							#printing encrypted plaintext

x = pow(ct,d,n)									#following (c^d)% n for decryption
print("Plaintext again:",x)						#printing decrypted ciphertext
