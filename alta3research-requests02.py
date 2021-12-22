#!/usr/bin/python3
# Using the Bored API. More info on it can be found here: https://www.boredapi.com/about

import requests

url = "http://www.boredapi.com/api/activity"
# List of types can be found in the Bored API documentation: https://www.boredapi.com/documentation
types = ["education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork", "anything"]

# Method for generating string for GET parameters
def generate_params(type, participants):
    params = ""
    # Adds or doesn't add parameters based on user input
    if type != 10:
        params = f"?type={types[type-1]}"
    if participants != 0:
        if "?" not in params:
            params = f"?participants={participants}"
        else:
            params += f"&participants={participants}"
    return params

# This method is used to simplify the price and accessibility values returned
def simplify_activity(activity):
    # According to Bored API, the price is represented by "A factor describing the cost of the event with zero being free." 
    if activity['price'] == 0:
        activity['price'] = "free"
    elif activity['price'] == 1:
        activity['price'] = "expensive"
    else:
        if activity['price'] >= 0.5:
            activity['price'] = "slightly pricey"
        else:
            activity['price'] = "relatively cheap"
            
    # According to Bored API, the accessibility is represented by "A factor describing how possible an event is to do with zero being the most accessible."
    if activity['accessibility'] == 0:
        activity['accessibility'] = "incredibly"
    elif activity['accessibility'] == 1:
        activity['accessibility'] = "scarcely"
    else:
        if activity['accessibility'] >= 0.5:
            activity['accessibility'] = "not very"
        else:
            activity['accessibility'] = "fairly"

    return activity

def main():
    print("You're bored? Well I have something you can do.")
    
    print("Activities:")
    for act in types:
        # Printing list of activities for user to chose from along with a number to simplify choice input.
        print(f"{types.index(act)+1}. {act}")
    type_option = int(input("What type of activity would you like to do?\n"))
    participants = int(input("How many participants would you like to include? (0 for any):\n"))
    params = generate_params(type_option, participants)
    response = requests.get(url + params).json()
    activity = simplify_activity(response)

    # Print results in a more user friendly format
    print(f"Your Activity: {activity['activity']}")
    print(f"This acticity is {activity['type']} and requires {activity['participants']} participant(s).")
    print(f"It is {activity['accessibility']} accessible and the cost is {activity['price']}!")
    if activity['link']:
        # Some activities include links, but not all of them. If a link is provided this prints it out.
        print(f"You can find out more here: {activity['link']}")


if __name__ == "__main__":
    main()
