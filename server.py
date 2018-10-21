from database.queries import *
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return "Projeto Ecodomo :)"

@app.route('/cupulas', methods=['GET', 'POST'])
def get_cupulas():
    if request.method == 'GET':
        return jsonify(get_all_cupulas())
    # else:
    #     cupula = request.form.get('name')
    #     return setDome(cupula)

@app.route('/cupulas/<cupula>', methods=['GET', 'POST'])
def get_cupula_atts(cupula):
    if request.method == 'GET':
        return jsonify(get_cupula_attributes(cupula))

if __name__ == '__main__':
    app.run(debug=True)