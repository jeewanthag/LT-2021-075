import hashlib
import sys

if len(sys.argv)> 1 :
	text_to_hash = sys.argv[1]
else:
	text_to_hash = ""

salt = "Km5d5ivMy8iexuHcZrsDc".encode()


hash_out=hashlib.pbkdf2_hmac('sha512',text_to_hash.encode(), salt,200000)
print(hash_out.hex())
