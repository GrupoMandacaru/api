from database.queries import *
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "Projeto Ecodomo :)"

@app.route('/cupulas', methods=['GET', 'POST'])
def allCupulas():
    if request.method == 'GET':
        return jsonify(get_all_cupulas())

@app.route('/cupulas/<cupula>', methods=['GET', 'POST'])
def cupula(cupula):
    if request.method == 'GET':
        return jsonify(get_cupula_info(cupula))

@app.route('/cupulas/<cupula>/data', methods=['GET', 'POST'])
def cupulaAttributes(cupula):
    if request.method == 'GET':
        args = request.args.get('limit')
        limit = int(args) if args is not None else 1
        return jsonify(get_cupula_attributes(cupula, limit))
    else:
        args = request.args.to_dict()
        return set_cupula_attribute(cupula, args)

if __name__ == '__main__':
    app.run(debug=True) 