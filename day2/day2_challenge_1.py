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

hero={'name':{'alias':'Batman','real name':'Bruce Wayne'},'background':{'origin':'Parents got murdered, got angry. Is super rich.','family':{'parents':'dead','siblings':None},'age':32,'number of deaths':19},'powers':['ninja training','money','batsuit'],'enemies':['joker','two face','scarecrow','poison ivy'],'allies':['cat woman','red robin','nightwing'],'rivals':['joker'],'weaknesses':['poverty','strict moral code']}
def show_batman_details():
    while True:
        batman_stat = input("\nWhat statistic do you want to know about Batman? (enemies, allies, rivals, powers, or weaknesses or exit)").strip().lower()

        if batman_stat in hero.keys():
            print(f"\nBatman's {batman_stat} are:")
            for el in hero[batman_stat]:
                print(el)

        elif batman_stat == "exit":
            print("\nOk, Bye-bye")
            quit()
        else:
            print("\nBad Input! Please try again!")



while True :
    char_name = input("\nWhich character do you want to know about? (Starlord, Mystique, She-Hulk, or exit)").strip().lower()

    if char_name.title() in marvelchars.keys():
        break;
    elif char_name == "exit":
        print("\nOk, Bye-bye")
        quit()
    else:
        print("\nBad Input! Please try again!")


while True:
    char_stat = input("\nWhat statistic do you want to know about? (real name, powers, archenemy or exit)").strip().lower()

    if char_stat in marvelchars[char_name.title()].keys():
        break;
    elif char_stat == "exit":
        print("\nOk, Bye-bye")
        quit()
    else:
        print("\nBad Input! Please try again!")

print(f"\n{char_name.title()}'s {char_stat} is: {marvelchars[char_name.title()][char_stat]}")

while True:
    see_batman = input("\nWould you like to see Batman's details? ( yes or no )").strip().lower()
    if see_batman == "no":
        print("\nOk, Bye-bye")
        quit()

    elif see_batman == "yes":
        show_batman_details()

    else:
        print("\nBad Input! Please try again!")



