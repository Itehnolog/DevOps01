from passwd_class import PasswordGenerator
import os


def main():
    pas = PasswordGenerator()
    atr = ""
    while atr != "6":
        os.system('cls')
        print("""
Welcome to the Linux User Password Generator!
By default, password will be 8 characters long and contain at least one uppercase and lowercase letters,
one number, one special character (e.g., !, @, #, $, %, etc.)
      """)
        print("""Which one do you want to change:
              1. Exclude number
              2. Exclude lowercase letters
              3. Exclude uppercase letters
              4. Excluse specail chracters
              5. Change length(must be between 8 and 256)
              6. Generate password and quit
                                     """)

        atr = input("Make your choice: ")
        attributes = {"1": "include_digits",
                      "2": "include_lowercase",
                      "3": "include_uppercase",
                      "4": "include_special_chars"
                      }
        if atr in attributes:
            setattr(pas, attributes[atr], False)
        elif atr == "5":
            print(pas.change_length())
            input("Press Enter to continue")
        elif atr == "6":
            print(pas.generate_password())
            exit(0)
        else:
            print("Wrong choice!")
            input("Press Enter to continue")


if __name__ == "__main__":
    main()
