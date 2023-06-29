from flask import Flask, request
from markupsafe import escape
from main import Randomizer
app = Flask(__name__)

@app.route('/names', methods=['GET'])
def get_names():
    names_string = request.args.get('names')
    names = names_string.split(',')
    rand = Randomizer();
    return f"{rand.get_list_names(names)}"
