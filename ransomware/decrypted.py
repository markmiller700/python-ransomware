import os
from cryptography.fernet import Fernet

files = []
for file in os.listdir():
    if file in ["encrypt.py", "decrypt.py", "flage.key"]:
        continue
    if os.path.isfile(file):
        files.append(file)

with open("flage.key", "rb") as key_file:
    secret_key = key_file.read()

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_decrypted = Fernet(secret_key).decrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_decrypted)