from flask import Flask
import random

app = Flask(__name__)

print(random.__name__)
print(__name__)
@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello World!</h1>' \
           '<p>This is a paragraph</p>' \
           '<img src="https://images.unsplash.com/photo-1529778873920-4da4926a72c2?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHx' \
           'zZWFyY2h8Mnx8Y3V0ZSUyMGNhdHxlbnwwfHwwfHw%3D&w=1000&q=80" width=400></img> ' \
           '<img src="https://i.imgur.com/lK6OP13.gif"></img>'

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper


@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye!"
    # return "<u><em><b>Bye!</b></em></u>"

@app.route('/<name>/<int:number>')
def greet(name, number):
   return f"Hello there {name}, you are {number} years old!"

if __name__ == "__main__":
    app.run(debug=True)


class User:
    def __init__(self, name):
        self.name = name
        self.is_loged_in = False

def is_authentificated_decorator(function):
    def wrapper(**args, **kwargs):
        if args[0].is_logged_in == True
            function(args[0])
    return wrapper

def create_blog_post(user):
    print(f"This is {user.name}'s blog post.")

new_user = User("marin")
new_user.is_logged_in = True
create_blog_post(new_user)