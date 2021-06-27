from pwn import xor

#xor for same lenght of key and msg

msg = 'awesomepassword'
key = 'XOR procedureee'

ct = xor(msg,key)   #xor function basically does a^b for every character in msg and key
pt = xor(ct,key)

print(ct)
print(pt)
