from cryptography.fernet import Fernet
key = Fernet.generate_key()
f=Fernet(key)
token=f.encrypt(b"secret message")
print(token)
original_string=f.decrypt(token)
print(original_string)