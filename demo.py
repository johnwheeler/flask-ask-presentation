import logging
from flask import Flask
from flask_ask import Ask, statement, question


app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)


@ask.launch
def welcome():
    greeting = "Hello PyLadies. Welcome to today's presentation: Flask-Ask, an Alexa Skills Kit framework for Python"
    return statement(greeting)


@ask.intent("AddIntent")
def add(x, y):
    the_sum = x + y
    return statement("The sum of {} plus {} is {}".format(x, y, the_sum))