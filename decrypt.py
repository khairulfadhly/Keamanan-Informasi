from cryptography.fernet import Fernet


file = open('mykey.txt', 'rb')
key = file.read()
file.close()


with open('mytextencrypted.txt', 'rb') as f:
    data = f.read()

fernet = Fernet(key)
decrypted = fernet.decrypt(data)


with open('myplaintext.txt', 'wb') as f:
    f.write(decrypted)
