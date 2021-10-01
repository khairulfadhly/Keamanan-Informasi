from cryptography.fernet import Fernet

file = open('mykey.txt', 'rb')
key = file.read()
file.close()

#Membaca file pesan.txt
with open('mytext.txt', 'rb') as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.encrypt(data)

#Output pesanencrypted.txt
with open('mytextencrypted.txt', 'wb') as f:
    f.write(encrypted)
