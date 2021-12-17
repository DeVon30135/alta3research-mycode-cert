#!/usr/bin/python3
from flask import Flask, redirect, url_for, request, render_template
import yaml

app = Flask(__name__)

@app.route("/")
@app.route("/start")
def start():
    return render_template("select_fusion.html")

@app.route("/fuse", methods = ["POST", "GET"])
def fuse():
    #Parse data and redirect to frutimal
    if request.method == "POST":
        animal = request.form.get("animal")
        fruit = request.form.get("fruit")
        combination = animal + "-" + fruit
        print(combination)
        return redirect(url_for("fruitimal", fusion = combination))

    elif request.method == "GET":
        return "WOW"

@app.route("/fruitimal/<fusion>")
def fruitimal(fusion):
    #Load animal info from yaml
    with open("fruitimals.yml", "r") as info:
        bestiary = yaml.load(info)
    beast = bestiary[0][fusion]
    print(beast['image'])
    #Return results rendered to template
    return render_template("fusion_result.html", fruitimal = beast)

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application

