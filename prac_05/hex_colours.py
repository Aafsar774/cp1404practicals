colour_names = {"Absolute Zero": "0048ba","Acid Green": "#b0bf1a","AliceBlue": "#f0f8ff","Alizarin crimson": "#e32636","Amaranth": "#e52b50","Amber": "#ffbf00","Amethyst": "#9966cc","AntiqueWhite": "#faebd7","AntiqueWhite1": "#ffefdb","AntiqueWhite2": "#eedfcc"}

name = input("Enter colour name: ")
if name in colour_names:
    print(f"{name} -> {colour_names[name]}")
else:
    print("Invalid colour name")
