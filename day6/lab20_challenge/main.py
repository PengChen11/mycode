#!/usr/bin/python3

# return a url to get Mars rover photo based on user input

from modules.settings import rovers_dict
from modules.questions import rover_details
from modules.questions import get_date
from termcolor import colored

def returncreds():
    ## first I want to grab my credentials
    try:
        with open("nasa.txt", "r") as mycreds:
            nasacreds = mycreds.read()
        ## remove any newline characters from the api_key
        nasacreds = nasacreds.strip("\n")
        return nasacreds
    except:
        print(colored("No API key file found", "red"))

def main():

    base_url = "https://api.nasa.gov/mars-photos/api/v1/rovers/"

    rover_collection = list(rovers_dict.keys())
    rover_select = rover_details(rover_collection)

    rover_cameras = rovers_dict[rover_select]
    camera_select = rover_details(rover_cameras)
    data_select = get_date()

    api_key = returncreds()

    url = f"{base_url}{rover_select}/photos?camera={camera_select}&earth_date={data_select}&api_key={api_key}"

    print(url)


if __name__ == "__main__":
    main()
