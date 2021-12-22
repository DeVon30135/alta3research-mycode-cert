import requests

url = "http://www.boredapi.com/api/activity"
types = ["education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork", "anything"]

def main():
    print("You're bored? Well I have something you can do.")
    print("Activities:")
    for act in types:
        print(f"{types.index(act)+1}. {act}")
    type_option = int(input("What type of activity would you like to do?\n"))
    participants = int(input("How many participants would you like to include? (0 for any):\n"))
    params = ""
    
    if type_option != 10:
        params = f"?type={types[type_option-1]}"
    if participants != 0:
        if "?" not in params:
            params = f"?participants={participants}"
        else:
            params += f"&participants={participants}"
            
    act = requests.get(url + params).json()

    if act['price'] == 0:
        cost = "free"
    elif act['price'] == 1:
        cost = "expensive"
    else:
        if act['price'] >= 0.5:
            cost = "slightly pricey"
        else:
            cost = "relatively cheap"

    if act['accessibility'] == 0:
        access = "incredibly"
    elif act['accessibility'] == 1:
        access = "scarcely"
    else:
        if act['accessibility'] >= 0.5:
            access = "not very"
        else:
            access = "fairly"

    print(f"Your Activity: {act['activity']}")
    print(f"This acticity is {act['type']} and requires {act['participants']} participant(s).")
    print(f"It is {access} accessible and the cost is {cost}!")
    if act['link']:
        print(f"You can find out more here: {act['link']}")


if __name__ == "__main__":
    main()
