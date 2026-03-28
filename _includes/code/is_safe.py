
def is_safe(password, path="common_passwords.txt"):
    ''' Criteria:
        1. At least 8 characters long
        2. Not in the file of common passwords. 
           The file must contain one password per line.
        3. Contains at least one from each of the following:
           lowercase letters, uppercase letters, numbers, special characters.
    '''
    if len(password) < 8:
        return False
    
    # read common passwords from file and check if password is in the list
    with open(path, 'r') as f:
        common_passwords = f.read().splitlines()
    if password in common_passwords:
        return False
    
    # count how many of the 4 character types are present
    lowercase = uppercase = numbers = special = 0
    for c in password:
        if c.islower():
            lowercase = 1
        elif c.isupper():
            uppercase = 1
        elif c.isdigit():
            numbers = 1
        else:
            special = 1

    # all 4 types must be present
    if lowercase + uppercase + numbers + special < 4:
        return False
    return True