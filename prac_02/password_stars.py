character_length = 8

password = input(f"Enter a password (minimum {character_length} characters): ")
while len(password) < character_length:
    print(f"Password must be at least {character_length} characters!")
    password = input("Enter a password: ")

print('*' * len(password))
