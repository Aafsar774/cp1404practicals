from prac_04.list_comprehensions import names

colour_names = {"Absolute Zero": "0048ba","Acid Green": "#b0bf1a","AliceBlue": "#f0f8ff","Alizarin crimson": "#e32636","Amaranth": "#e52b50","Amber": "#ffbf00","Amethyst": "#9966cc","AntiqueWhite": "#faebd7","AntiqueWhite1": "#ffefdb","AntiqueWhite2": "#eedfcc"}


name_lower = {name.lower(): code for name, code in colour_names.items()}

def main():
    name = input("Enter colour name: ").strip()
    key = name.lower()
    if key in name_lower:
        print(f"{name} = {name_lower[key]}")
    else:
        print("Invalid colour name")

main()