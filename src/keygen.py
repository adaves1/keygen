import random
import string

def key(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    random_key = ''.join(random.choice(characters) for _ in range(length))
    return random_key
