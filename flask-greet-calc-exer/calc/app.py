# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

# responds to 4 different routes
# each route -> math operation with two numbers a and break
# URL GET-style query parameters


@app.route('/add')
def adding():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = add(a, b)
    return str(result)


@app.route('/sub')
def subtract():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = sub(a, b)
    return str(result)


@app.route('/mult')
def multiply():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = mult(a, b)
    return str(result)


@app.route('/div')
def divide():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = div(a, b)
    return str(result)


# FURTHER STUDY
function_dict = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div
}


@app.route('/math/<op_name>')
def calculate(op_name):

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = function_dict[op_name](a, b)

    return str(result)
