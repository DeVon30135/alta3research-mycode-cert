#!/usr/bin/python3
# Images are generated from Emoji Kitchen made by Google. More info on Emoji kitchen can be found here: https://blog.google/products/android/emoji-kitchen-new-mashups-mixing-experience/

from flask import Flask, redirect, url_for, request, render_template
import yaml

app = Flask(__name__)
# Loads animal info from yaml file
with open("foodimals.yml", "r") as info:
        bestiary = yaml.safe_load(info)[0]

@app.route("/")
@app.route("/start")
def start():
    # Loads the animal select template
    return render_template("select_fusion.html")

@app.route("/fuse", methods = ["POST", "GET"])
def fuse():
    #Parse input data and redirect to frutimal
    if request.method == "POST":
        animal = request.form.get("animal")
        food = request.form.get("food")
        # Combination will look like "octopus-pineapple"
        combination = animal + "-" + food
        print(combination)
        return redirect(url_for("foodimal", fusion = combination))

    elif request.method == "GET":
        animal = request.args.get("animal").lower()
        food = request.args.get("food").lower()
        combination = animal + "-" + food
        print(combination)
        # Check if GET arguments have a valid animal
        if combination in bestiary:
            beast = bestiary[combination]
            # Returns animal name and link to see the full bio
            return f"Your animal fusion is {beast['name']}! More info can be found here: {request.url_root}foodimal/{combination}"
        else:
            return f"""The animal {combination} doesn't exist in our findings.
                    The available animals are:
                    - Deer
                    - Octopus
                    - Scorpion

                    The available foods are:
                    - Cake
                    - Hotdog
                    - Pineapple"""

@app.route("/foodimal/<fusion>")
def foodimal(fusion):
    beast = bestiary[fusion]
    # Return results rendered to template. The template handles loading items within the dictionary
    return render_template("fusion_result.html", foodimal = beast)

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application

