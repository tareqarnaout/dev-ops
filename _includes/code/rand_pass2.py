import random
def random_password(length=4, path="/usr/share/dict/words"):
    '''
    Generate a random passowrd by concatenating `length` words 
    from the given dictionary file.
    The default dictionary file is /usr/share/dict/words, which 
    is available on most Unix systems.
    '''
    with open(path, 'r') as file:
        words = file.read().splitlines()          

    chosen_words = []
    for _ in range(length):
        chosen_words.append(' ' + random.choice(words))
        
    password = ''.join(chosen_words)
    return password
