from flask import Flask, request
from src.config import PORT
from src.gitapi import getBySeniority, requestUsers
from src.predict import predictUser

app = Flask(__name__)


@app.route("/")
def baseResponse():
    return {
        "hola cabron": f"que te follen"
        }

@app.route("/user/<location>/<language>/<seniority>/get", methods=["GET"])
def searchUser(location, language, seniority):
    user_chars = {"location":location, "language":language, "seniority":seniority}
    followers, repos = getBySeniority(user_chars["seniority"])
    users = requestUsers(user_chars["location"], user_chars["language"], followers, repos)
    return users


@app.route("/user/<login>/predict", methods=["GET"])
def recommend(login):
    seniority = predictUser(login)
    return seniority
    

