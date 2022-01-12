import string
import collections
import sets, sys

c3 = "4fd098298db95b7f1bc205b0a6d8ac15f1f821d72fbfa979d1c2148a24feaafdee8d3108e8ce29c3ce1291"

c9 = "41d9806ec1b55c78258703be87ac9e06edb7369133b1d67ac0960d8632cfb7f2e7974e0ff3c536c1871b"

ciphers = [c3, c9]

target_cipher = c3

def strxor(a, b):     
    return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b)])

final_key = [None]*150

known_key_positions = set()


for current_index, ciphertext in enumerate(ciphers):
    counter = collections.Counter()
    
    for index, ciphertext2 in enumerate(ciphers):
        if current_index != index: # don't xor a ciphertext with itself
            for indexOfChar, char in enumerate(strxor(ciphertext.decode('hex'), ciphertext2.decode('hex'))): 
                
                if char in string.printable and char.isalpha(): counter[indexOfChar] += 1 
    knownSpaceIndexes = []

    
    for ind, val in counter.items():
        
        if val >= 7: knownSpaceIndexes.append(ind)
    

    
    xor_with_spaces = strxor(ciphertext.decode('hex'),' '*150)
    for index in knownSpaceIndexes:
        
        final_key[index] = xor_with_spaces[index].encode('hex')
        
        known_key_positions.add(index)


final_key_hex = ''.join([val if val is not None else '00' for val in final_key])

output = strxor(target_cipher.decode('hex'),final_key_hex.decode('hex'))

print "Fix this sentence:"
print ''.join([char if index in known_key_positions else '*' for index, char in enumerate(output)])+"\n"

target_plaintext = "hey let's rob the bank at midnight tonight!"
print "Fixed:"
print target_plaintext+"\n"

key = strxor(target_cipher.decode('hex'),target_plaintext)

print "Decrypted msg:"
for cipher in ciphers:
    print strxor(cipher.decode('hex'),key)

print "\nPrivate key recovered: "+key+"\n"
