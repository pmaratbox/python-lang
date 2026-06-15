import hashlib

password = b"password"
salt = b"salt"
iterations = 1000
dklen = 32

dk = hashlib.pbkdf2_hmac("sha256", password, salt, iterations, dklen)
print(dk.hex())
