import random


def generate_password(lenght):
    password = ""
    for _ in range(lenght):
        char = chr(random.randint(33,125))
        password += char
    return password

print("\nWelcome to strong password generator\n")
while True:

    lenght = int(input("Enter required lenght of password: "))
    print(f"Password: {generate_password(lenght)}")
    
    another = input("\nDo you want to generate another password? \
                    1. yes\
                    2.no and exit\
                    Choose 1 or 2: ")
                    
    if another == "2":
        print("Thanks for using our password generator")
        break