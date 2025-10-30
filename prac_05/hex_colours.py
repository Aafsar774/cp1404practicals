colour_names = {"Absolute Zero": "0048ba","Acid Green": "#b0bf1a","AliceBlue": "#f0f8ff","Alizarin crimson": "#e32636","Amaranth": "#e52b50","Amber": "#ffbf00","Amethyst": "#9966cc","AntiqueWhite": "#faebd7","AntiqueWhite1": "#ffefdb","AntiqueWhite2": "#eedfcc"}

name_lower = {name.lower(): code for name, code in colour_names.items()}

def main():
    while True:
        name = input("Enter colour name: ").strip()
        if not name:  # blank ends the loop
            break
        key = name.lower()
        if key in name_lower:
            print(f"{name} = {name_lower[key]}\n")
        else:
            print("Invalid colour name.Try again!\n")

main()