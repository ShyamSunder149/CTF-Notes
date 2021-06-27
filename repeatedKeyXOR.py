
from pwn import xor

pt = "Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"
key = "ICE"
output = b''

#generalized format for forming repeated key as of the lenght of the msg

ptlen = len(pt)
keylen = len(key)

if(ptlen%keylen!=0):
	key = "ICE"*(int((ptlen/len(key))+1))
else:
	key = "ICE"*(int(ptlen/len(key)))

for i,j in zip(pt,key):
	output += xor(i,j)

print(output)
