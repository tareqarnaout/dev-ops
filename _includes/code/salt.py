import hashlib
import secrets

def create_password_hash(password):
    '''
    Creates a salted hash of a password.
    Returns both the salt and the hash.
    '''
    # Generate a random salt (16 bytes = 32 hex characters)
    salt = secrets.token_hex(16)
    
    # Combine password and salt, then hash with SHA-256
    salted_password = password + salt
    hashed_password = hashlib.sha256(salted_password.encode()).hexdigest()
    
    return salt, hashed_password

def verify_password(password, stored_salt, stored_hash):
    '''Verifies if a password matches the stored hash. '''

    # Recreate the hash using the stored salt
    salted_password = password + stored_salt
    hashed_password = hashlib.sha256(salted_password.encode()).hexdigest()
    
    # Compare with stored hash
    return hashed_password == stored_hash

# Example usage:
password1 = "mypassword"
salt, password_hash = create_password_hash(password1)
print("Salt: ", salt)
print("Hash: ", password_hash)
print()

password2 = "mypassword" # use the same password
salt2, password_hash2 = create_password_hash(password2)
print("Salt2: ", salt2)
print("Hash2: ", password_hash2) # different hash because of different salt
print()

# Verify
print("Verifying password1:", verify_password(password1, salt, password_hash)) # True
print("Verifying password1:", verify_password(password2, salt2, password_hash2)) # True
print("Verifying wrong password:", verify_password("wrongpassword", salt, password_hash)) # False
