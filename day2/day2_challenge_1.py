#!/usr/bin/env python3

marvelchars= {
    "Starlord":
        {"real name": "Peter Quill",
        "powers": "dance moves",
        "archenemy": "Thanos"},

    "Mystique":
        {"real name": "Raven Darkholme",
        "powers": "shape shifter",
        "archenemy": "Professor X"},

    "She-Hulk":
        {"real name": "Jennifer Walters",
        "powers": "super strength & intelligence",
        "archenemy": "Titania"}
             }

while True :
    char_name = input("Which character do you want to know about? (Starlord, Mystique, She-Hulk)").strip().lower()

    if char_name.title() in marvelchars.keys():
        break;
    else:
        print("Bad Input! Please try again!")


while True:
    char_stat = input(" What statistic do you want to know about? (real name, powers, archenemy)").strip().lower()

    if char_stat in marvelchars[char_name.title()].keys():
        break;
    else:
        print("Bad Input! Please try again!")

print(f"{char_name.title()}'s {char_stat} is: {marvelchars[char_name.title()][char_stat]}")
