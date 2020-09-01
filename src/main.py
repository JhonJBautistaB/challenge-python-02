# Resolve the problem!!
import string
import random

SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')
LOWERCASE = list(string.ascii_lowercase)
UPPERCASE = list(string.ascii_uppercase)
DIGITS = list(string.digits)


def generate_password():
    # Start coding here
    password_sec = ''
    password = []
    password_len = random.randint(8,16)
    print('Password_Len: ', password_len)

    while True:

        if password_len != len(password):
            password.append(random.choice(LOWERCASE))
            if password_len != len(password):
                password.append(random.choice(UPPERCASE))
                if password_len != len(password):
                    password.append(random.choice(DIGITS))
                    if password_len != len(password):
                        password.append(random.choice(SYMBOLS))
        else:
            break

    random.shuffle(password)
    password_sec = ''.join(password)
    print('su password es:', password_sec)

    return password_sec


def validate(password):

    if len(password) >= 8 and len(password) <= 16:
        has_lowercase_letters = False
        has_numbers = False
        has_uppercase_letters = False
        has_symbols = False

        for char in password:
            if char in string.ascii_lowercase:
                has_lowercase_letters = True
                break

        for char in password:
            if char in string.ascii_uppercase:
                has_uppercase_letters = True
                break

        for char in password:
            if char in string.digits:
                has_numbers = True
                break

        for char in password:
            if char in SYMBOLS:
                has_symbols = True
                break

        if has_symbols and has_numbers and has_lowercase_letters and has_uppercase_letters:
            return True
    return False


def run():
    password = generate_password()
    if validate(password):
        print('Secure Password')
    else:
        print('Insecure Password')


if __name__ == '__main__':
    run()
