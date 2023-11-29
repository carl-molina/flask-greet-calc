from flask import Flask


app = Flask(__name__)

@app.get('/welcome')
def welcome():
    print('this in terminal?')
    return "welcome"

@app.get('/welcome/home')
def welcome_home():
    print('this in terminal? 1')
    return 'welcome home'

@app.get('/welcome/back')
def welcome_back():
    return 'welcome back'

