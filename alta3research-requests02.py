#!/usr/bin/python3
# Using the Bored API. More info on it can be found here: https://www.boredapi.com/about

import requests

url = "http://www.boredapi.com/api/activity"
# List of types can be found in the Bored API documentation: https://www.boredapi.com/documentation
types = ["education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork", "anything"]

def main():
    print("You're bored? Well I have something you can do.")
    
    print("Activities:")
    for act in types:
        # Printing list of activities for user to chose from along with a number to simplify choice input.
        print(f"{types.index(act)+1}. {act}")
    type_option = int(input("What type of activity would you like to do?\n"))
    participants = int(input("How many participants would you like to include? (0 for any):\n"))
    params = ""
    
    # Adds or doesn't add parameters based on user input
    if type_option != 10:
        params = f"?type={types[type_option-1]}"
    if participants != 0:
        if "?" not in params:
            params = f"?participants={participants}"
        else:
            params += f"&participants={participants}"
            
    act = requests.get(url + params).json()

    # According to Bored API, the price is represented by "A factor describing the cost of the event with zero being free." 
    #   I've tried to simplify it down for user understanding
    if act['price'] == 0:
        cost = "free"
    elif act['price'] == 1:
        cost = "expensive"
    else:
        if act['price'] >= 0.5:
            cost = "slightly pricey"
        else:
            cost = "relatively cheap"
    # According to Bored API, the accessibility is represented by "A factor describing how possible an event is to do with zero being the most accessible."
    #   I've tried to simplify it down for user understanding
    if act['accessibility'] == 0:
        access = "incredibly"
    elif act['accessibility'] == 1:
        access = "scarcely"
    else:
        if act['accessibility'] >= 0.5:
            access = "not very"
        else:
            access = "fairly"

    # Print results in a more user friendly format
    print(f"Your Activity: {act['activity']}")
    print(f"This acticity is {act['type']} and requires {act['participants']} participant(s).")
    print(f"It is {access} accessible and the cost is {cost}!")
    if act['link']:
        # Some activities include links, but not all of them. If a link is provided this prints it out.
        print(f"You can find out more here: {act['link']}")


if __name__ == "__main__":
    main()
