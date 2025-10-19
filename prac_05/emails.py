"""
Emails
Estimate: 45 minutes
Actual:
"""

def main():
    email_to_name = {}

    while True:
        email = input("Email: ").strip()
        if email == "":
            break
        name_part = email.split("@")[0]
        guessed_name = name_part.replace(".", " ").replace("_", " ").title()

        answer = input(f"Is your name {guessed_name}? (Y/n) ").strip().lower()
        if answer not in ("", "y"):
            # Ask for the correct name
            guessed_name = input("Name: ").strip()

        email_to_name[email] = guessed_name

    # Print results
    for email, name in email_to_name.items():
        print(f"{name} ({email})")

main()
