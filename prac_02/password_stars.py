character_length = 8
def main():
    password = get_password(character_length)
    print_asterisks(password)

def get_password(character_length):
    password = input(f"Enter a password (minimum {character_length} characters): ")
    while len(password) < character_length:
        print(f"Password must be at least {character_length} characters!")
        password = input("Enter a password: ")
    return password

def print_asterisks(password):
    print('*' * len(password))

main()

