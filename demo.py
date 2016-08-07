import logging
from flask import Flask
from flask_ask import Ask, statement, question


app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)


@ask.launch
def welcome():
    return statement("Hello, world to PyLadies")
    
    
@ask.intent("AddIntent", convert={'x': int, 'y': int})
def add(x, y):
    the_sum = x + y
    text = "The sum is {}".format(the_sum)
    return statement(text)
