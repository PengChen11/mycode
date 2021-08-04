#!/usr/bin/env python3

farms1 = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

farms2 = [{"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]},
         {"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "E Farm", "agriculture": ["bananas", "apples", "oranges"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]}]

animals = ["sheep", "cows", "pigs", "chickens", "cats", "llamas"]



def get_NE_Farm_animals(farms):
    output = []
    for farm in farms:
        if farm["name"] == "NE Farm":
            output = output + farm["agriculture"]

    return output


def get_user_chosen_farm_everything(farms):
    valid_farms = []
    for farm in farms:
        valid_farms.append(farm["name"])


    output = []

    while True:
        farm_location = input(f'Please choose a farm to see everything they have, (valid farms: {valid_farms})').strip().split(' ')[0].upper()

        farm_name = f"{farm_location} Farm"

        if farm_name in valid_farms:

            for farm in farms:
                if farm["name"] == farm_name:
                    output = output + farm["agriculture"]

            break

        else:
            print("Bad input. Please choose again.")

    return output



def get_user_chosen_farm_animals(farms):
    valid_farms = []
    for farm in farms:
        valid_farms.append(farm["name"])

    output = []

    while True:
        farm_location = input(f'Please choose a farm to see only the animals, (valid farms: {valid_farms})').strip().split(' ')[0].upper()

        farm_name = f"{farm_location} Farm"

        if farm_name in valid_farms:

            for farm in farms:
                if farm["name"] == farm_name:

                    for thing in farm["agriculture"]:
                        if thing in animals:
                            output.append(thing)

            break

        else:
            print("Bad input. Please choose again.")

    return output


def run_farms1():

    print(get_NE_Farm_animals(farms1))

    print(get_user_chosen_farm_everything(farms1))

    print(get_user_chosen_farm_animals(farms1))


def run_farms2():

    print(get_NE_Farm_animals(farms2))

    print(get_user_chosen_farm_everything(farms2))

    print(get_user_chosen_farm_animals(farms2))

run_farms1()
run_farms2()
