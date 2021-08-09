#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

def get_house_name(url):
    try:
        res_dict = requests.get(url).json()
        return res_dict["name"]
    except:
        print("Sorry, we can't retrive the name of the house")


def get_book_name(url):
    try:
        res_dict = requests.get(url).json()
        return res_dict["name"]
    except:
        print("Sorry, we can't retrive the name of the book")


def main():
    char_details = {
                "name": None,
                "allegiances": [],
                "appeared in books":[]
                }
    ## Ask user for input
    got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

    ## Send HTTPS GET to the API of ICE and Fire character resource
    try:
        res_dict = requests.get(AOIF_CHAR + got_charToLookup).json()

        char_details = {
            "name": res_dict["name"],
            "allegiances": [],
            "appeared in books":[]
            }

        if (res_dict["allegiances"]) != 0:
            try:
                for appegiancy_url in res_dict["allegiances"]:
                    house_name = get_house_name(appegiancy_url)
                    char_details["allegiances"].append(house_name)
            except:
                print("Something went wrong when trying to get the appegiancy name")

        if (res_dict["books"]) != 0:
            try:
                for book_url in res_dict["books"]:
                    book_name = get_book_name(book_url)
                    char_details["appeared in books"].append(book_name)
            except:
                print("Something went wrong when trying to get the book name")

    except:
        print('Something went wrong when trying to retrive the charator for you')

    pprint.pprint(char_details)
    return char_details

if __name__ == "__main__":
        main()

