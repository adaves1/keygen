import random

def key(length=16):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    key = ''.join(random.choice(characters) for _ in range(length))
    return key

def complex_key(ulength=20, parts=4, cpparts=5):
    c = parts / cpparts * (ulength)
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    key = ''.join(random.choice(characters) for _ in range(ulength * c))
    print(f"Complex Key Shift: {c}")
    return key

def product_key(length=20):
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    key = ''.join(random.choice(characters) for _ in range(length))
    keyh = '-'.join([key[i:i+5] for i in range(0, length, 5)])
    return keyh.rstrip('-')

def digit_key(length=10):
    num = "0123456789"
    key = ''.join(random.choice(num) for _ in range(length))
    return key

def letter_key(length=10):
    letter = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = ''.join(random.choice(letter) for _ in range(length))
    return key

def letter_uppercase_key(length=10):
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = ''.join(random.choice(characters) for _ in range(length))
    return key

def letter_lowercase_key(length=10):
    characters = "abcdefghijklmnopqrstuvwxyz"
    key = ''.join(random.choice(characters) for _ in range(length))
    return key

def punctuation_key(length=10):
    characters = r"!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    key = ''.join(random.choice(characters) for _ in range(length))
    return key

class Bases:

    def bin_key(length=5):
        characters = "01"
        key = ''.join(random.choice(characters) for _ in range(length))
        return key

    def binary_key(length=5):
        characters = "01"
        key = ''.join(random.choice(characters) for _ in range(length))
        return key

    def ter_key(length=5):
        characters = "012"
        key = ''.join(random.choice(characters) for _ in range(length))
        return key

    def ternary_key(length=5):
        characters = "012"
        key = ''.join(random.choice(characters) for _ in range(length))
        return key

    def quarter_key(length=5):
        characters = "0123"
        key = ''.join(random.choice(characters) for _ in range(length))
        return key

    def quarternary_key(length=5):
        characters = "0123"
        key = ''.join(random.choice(characters) for _ in range(length))
        return key

    def qui_key(length=5):
        characters = "01234"
        key = ''.join(random.choice(characters) for _ in range(length))
        return key

    def quinary_key(length=5):
        characters = "01234"
        key = ''.join(random.choice(characters) for _ in range(length))
        return key

    def se_key(length=5):
        characters = "012345"
        key = ''.join(random.choice(characters) for _ in range(length))
        return key

    def senary_key(length=5):
        characters = "012345"
        key = ''.join(random.choice(characters) for _ in range(length))
        return key

    def se_key(length=5):
        characters = "012345"
        key = ''.join(random.choice(characters) for _ in range(length))
        return key

    def senary_key(length=5):
        characters = "012345"
        key = ''.join(random.choice(characters) for _ in range(length))
        return key

    def septe_key(length=5):
        characters = "0123456"
        key = ''.join(random.choice(characters) for _ in range(length))
        return key

    def septenary_key(length=5):
        characters = "0123456"
        key = ''.join(random.choice(characters) for _ in range(length))
        return key

    def no_key(length=5):
        characters = "012345678"
        key = ''.join(random.choice(characters) for _ in range(length))
        return key

    def nonary_key(length=5):
        characters = "012345678"
        key = ''.join(random.choice(characters) for _ in range(length))
        return key

    def dec_key(length=5):
        characters = "0123456789"
        key = ''.join(random.choice(characters) for _ in range(length))
        return key

    def decimal_key(length=5):
        characters = "0123456789"
        key = ''.join(random.choice(characters) for _ in range(length))
        return key

    def undec_key(length=5):
        characters = "0123456789A"
        key = ''.join(random.choice(characters) for _ in range(length))
        return key

    def undecimal_key(length=5):
        characters = "0123456789A"
        key = ''.join(random.choice(characters) for _ in range(length))
        return key

    def duodec_key(length=5):
        characters = "0123456789AB"
        key = ''.join(random.choice(characters) for _ in range(length))
        return key

    def duodecimal_key(length=5):
        characters = "0123456789AB"
        key = ''.join(random.choice(characters) for _ in range(length))
        return key

    def tridec_key(length=5):
        characters = "0123456789ABC"
        key = ''.join(random.choice(characters) for _ in range(length))
        return key

    def tridecimal_key(length=5):
        characters = "0123456789ABC"
        key = ''.join(random.choice(characters) for _ in range(length))
        return key

    def tetradec_key(length=5):
        characters = "0123456789ABCD"
        key = ''.join(random.choice(characters) for _ in range(length))
        return key

    def tetradecimal_key(length=5):
        characters = "0123456789ABCD"
        key = ''.join(random.choice(characters) for _ in range(length))
        return key

    def pentadec_key(length=5):
        characters = "0123456789ABCDE"
        key = ''.join(random.choice(characters) for _ in range(length))
        return key

    def pentadecimal_key(length=5):
        characters = "0123456789ABCDE"
        key = ''.join(random.choice(characters) for _ in range(length))
        return key

    def hex_key(length= 5):
        characters = "0123456789abcdefABCDEF"
        key = ''.join(random.choice(characters) for _ in range(length))
        return key

    def hexadecimal_key(length= 5):
        characters = "0123456789abcdefABCDEF"
        key = ''.join(random.choice(characters) for _ in range(length))
        return key

    def oct_key(length=5):
        characters = "01234567"
        key = ''.join(random.choice(characters) for _ in range(length))
        return key

    def octal_key(length=5):
        characters = "01234567"
        key = ''.join(random.choice(characters) for _ in range(length))
        return key

def mix_key(length=20):
    characters = r"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    key = ''.join(random.choice(characters) for _ in range(length))
    return key
