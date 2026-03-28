import random
import string

def random_password(length=12):
    '''
    Generate a random passowrd of the given length.
    The password will contain at least one lowercase letter, 
    one uppercase letter, one digit, and one special character.
    If the given length is less than 12, it will be set to 12.
    '''
    if length < 12:
        length = 12  

    # ensure the password has at least one of each character type
    password = [random.choice(string.ascii_lowercase), 
                random.choice(string.ascii_uppercase),
                random.choice(string.digits),
                random.choice(string.punctuation)]

    # fill the rest of the password length with random 
    # choices from all character types
    all_chars = string.ascii_letters + 
                string.digits + string.punctuation
    for _ in range(length - 4):
        password.append(random.choice(all_chars))

    # shuffle the password to avoid predictable patterns
    random.shuffle(password)
    return ''.join(password)