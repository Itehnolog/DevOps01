import random
import string


class PasswordGenerator:
    
    def __init__(self) -> None:
        self.length = 8
        self.include_uppercase = True
        self.include_lowercase = True
        self.include_digits = True
        self.include_special_chars = True

    def ramdom_character(self):
        # method wich generate random character
        random.seed()
        random_list = []
        if self.include_digits:
            random_list.append(random.choice(string.digits))
        if self.include_lowercase:
            random_list.append(random.choice(string.ascii_lowercase))
        if self.include_uppercase:
            random_list.append(random.choice(string.ascii_uppercase))
        if self.include_special_chars:
            random_list.append(random.choice(string.punctuation))
        try:
            return random.choice(random_list)
        except:
            print("Wrong conditions!!! Please run csript one more time.")
            exit(0)

    def generate_password(self):
        # method wich generate random password
        password = ''
        for i in range(self.length):
            password = password + self.ramdom_character()

        return f"Yuor password is: {password}"

    def change_length(self):
        # method for chenging length of password
        try:
            self.length = int(input("Enter your length(min 8, max 256): "))
        except ValueError:
            print("Length must be only number!")
        self.check_password_length()
        return f"Password length changed to {self.length}"

    def check_password_length(self):
        # metho verifying lentgh of password - must be between 8 and 256 characters
        if self.length < 8 or self.length > 256:
            self.length = 8
            print("Wrong length! Must be between 8 and 256 characters!")
