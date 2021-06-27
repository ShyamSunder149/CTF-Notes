from Crypto.Cipher import AES #import AES

key = 'awesomepassword1'

cipher = AES.new(key, AES.MODE_ECB) #declaration of aes in ecb mode

msg =cipher.encrypt('helloworld123456')
print(msg)

msg =cipher.decrypt(msg)
print(msg.decode())

#NOTE aes only accepts key of lenght 16,24 or 32 and msg of lenght as multiple of 16 bits if u dont have proper msg u have to do padding



