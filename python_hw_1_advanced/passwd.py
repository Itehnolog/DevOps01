import random
import string


def ramdom_character():
    # function wich generate random character
    random.seed()
    random_list = []
    random_list.append(random.choice(string.ascii_lowercase))
    random_list.append(random.choice(string.ascii_uppercase))
    random_list.append(random.choice(string.digits))
    random_list.append(random.choice(string.punctuation))
    return random.choice(random_list)


password = ''
print("""
Welcome to the Linux User Password Generator!
The password will be contain at least one uppercase letter
The password will be contain at least one lowercase letter
The password will be contain at least one number
The password will be contain at least one special character (e.g., !, @, #, $, %, etc.)
      """)

try:
    length_of_password = int(
        input("""
Please enter the desired password length
(The length of your password must be between 4 and 256.): """))
    print()
    if length_of_password <= 4 or length_of_password >= 256:
        print("Wrong input! The length of your password must be between 4 and 256!")
        exit()
except ValueError:
    print("Wrong input! You must enter only numbers!")
    exit()

#
password = password + \
    random.choice(string.ascii_lowercase) + \
    random.choice(string.ascii_uppercase) + \
    random.choice(string.digits) + random.choice(string.punctuation)

for i in range(length_of_password-4):
    password = password + ramdom_character()

password = ''.join(random.sample(password, len(password)))
print(f"Generated password is: {password}")
print()
