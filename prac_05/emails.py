"""
Emails
Estimate: 60 minutes
Actual:   70 minutes
"""

def extract_name_from_email(email) :

    name_part = email.split("@")[0]
    name_guess = name_part.replace(".", " ").replace("_", " ").title()
    return name_guess

def main():
    email_to_name = {}

    while True:
        email = input("Email: ").strip()
        if email == "":
            break

        guessed_name = extract_name_from_email(email)
        response = input(f"Is your name {guessed_name}? (Y/n) ").strip().lower()

        if response not in ("", "y"):
            guessed_name = input("Name: ").strip()

        email_to_name[email] = guessed_name

    # Print results
    for email, name in email_to_name.items():
        print(f"{name} ({email})")

main()
