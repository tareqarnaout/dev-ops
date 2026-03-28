import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
    
print(' mypassword: ', hash_password("mypassword"))
print(' mypassword: ', hash_password("mypassword"))  # same output as above
print('mypassword1: ', hash_password("mypassword1")) # different output
print('          1: ', hash_password("1")) # different output
print('          2: ', hash_password("2")) # different output