from flask import Flask, request
from markupsafe import escape
from main import Randomizer
app = Flask(__name__)

@app.route('/suffled-names', methods=['GET'])
def get_shuffled_names():
    names_string = request.args.get('names')
    names = names_string.split(',')
    rand = Randomizer()
    return rand.get_list_names(names)
