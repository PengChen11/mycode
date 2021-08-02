#!/usr/bin/env python3

icecream= ["flavors", "salty"]

tlgclass= ["Adrian","Bikash","Chas","Chathula","Chris","Hongyi","Jauric","Joe L.","Joe V.","Josh","Justin","Karlo","Kerri-Leigh","Jason","Nicholas","Peng","Philippe","Pierre","Stephen","Yun"]

icecream.append(99)

user_choice = input("Who are you? Please input your either student ID or name: ").strip()

user_choice_validator = False

user_id = None

while not user_choice_validator:
    try:
        user_id = int(user_choice)
        
        if user_id > len(tlgclass)-1:
            user_choice = input("Bad ID. ID can not be greater than 19 or smaller than 0.")
        else:
            user_choice_validator = True
            print(f"{icecream[2]} flavors, and {tlgclass[user_id]} choose to be salty")

    except ValueError:

        if user_choice in tlgclass:

            print(f"{icecream[2]} flavors, and {user_choice} choose to be salty")
            user_choice_validator = True
        else:

            user_choice = input("Bad input. It need to be name or id:  ").strip()
