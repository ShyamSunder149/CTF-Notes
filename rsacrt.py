from Crypto.Util.number import *

#Chinese Remainder theorem

msg = b'awesomepassword'

p = 10277651387301176987572317325479097395047746036448092597109087343402502311748817759127432792050163773397965509536015380001091183626070519891565314233610391
q = 11477990785403537825829714057028719300154941210754987809122684684976720343684073323701864241970563388461724325124916887772253666524224907489155204051884923
n = p*q
e = 2
phi = (p-1)*(q-1)
msg = bytes_to_long(msg)
print(msg)

while(e<phi):						#How e is calculated
	if(GCD(e,phi)==1):				#GCD is a inbuilt function to give gcd of 2 numbers
		break
	else:
		e=e+1


ciphertext = pow(msg,e,n)
print(ciphertext)

d = inverse(e,phi)


dp = d%(p-1)
dq = d%(q-1)
qinv = inverse(q,p)

#private keys(dp,dq,p,q,qinv)


x1 = pow(ciphertext,dp,p)
x2 = pow(ciphertext,dq,q)
h = (qinv*(x1-x2))%p
plaintext = x2+h*q
print(plaintext)

