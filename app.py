from flask import Flask, request, render_template, jsonify
import json
import sqlite3 as sql
import classify
import base64
import os
import gc

import json
import env
from classify import init

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('menu.html')

@app.route('/waste/get', methods=['GET'])
def get_wastes():
    with sql.connect('workshop.db') as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        rows = cur.execute("SELECT w.Id, w.name, m.Id as id_mat, m.name as mat FROM waste w CROSS JOIN material m on w.id_material = m.Id").fetchall()
        return json.dumps( [dict(row) for row in rows])

@app.route('/recycling/get', methods=['GET'])
def get_recycling():
    with sql.connect('workshop.db') as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        rows = cur.execute("SELECT * FROM recycling").fetchall()
        return json.dumps([dict(row) for row in rows])

@app.route('/material/get', methods=['GET'])
def get_materials():
    with sql.connect('workshop.db') as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        rows = cur.execute("SELECT m.Id, m.name, m.barCode, r.Id as id_recycling, r.name as recycling FROM material m  CROSS JOIN recycling r on m.id_recycling = r.Id").fetchall()
        return json.dumps([dict(row) for row in rows])

@app.route('/material/add', methods=['POST'])
def add_material():
    with sql.connect('workshop.db') as con:
        name = request.args.get('name')
        barCode = request.args.get('barCode')
        id_recycling = request.args.get('idRecycling')
        cur = con.cursor()
        cur.execute("INSERT INTO material (name, barCode, id_recycling) VALUES(?,?,?)", (name, barCode, id_recycling))
        con.commit()
        return ('row added')

@app.route('/waste/add', methods=['POST'])
def add_waste():
    with sql.connect('workshop.db') as con:
        name = request.args.get('name')
        id_material = request.args.get('idMaterial')
        cur = con.cursor()
        cur.execute("INSERT INTO waste (name, id_material) VALUES(?,?)", (name,id_material))
        con.commit()
        return ('row added')

@app.route('/recycling/add', methods=['POST'])
def add_recycling():
    with sql.connect('workshop.db') as con:
        name = request.args.get('name')
        cur = con.cursor()
        cur.execute("INSERT INTO recycling (name) VALUES (?)", (name))
        con.commit()
        return ('row added')

@app.route('/recycling/get/<id>', methods=['GET'])
def get_recycling_by_id(id):
    with sql.connect('workshop.db') as con:
        cur = con.cursor()
        row = cur.execute("SELECT * FROM recycling WHERE Id=%s;", id).fetchone()
        return json.dumps(row)

@app.route('/material/get/<barCode>', methods=['GET'])
def get_material_by_barCode(barCode):
    with sql.connect('workshop.db') as con:
        cur = con.cursor()
        row = cur.execute("SELECT * FROM material WHERE barCode=%s;", [barCode]).fetchone()
        return json.dumps(row)

# health check
@app.route('/status')
def health_check():
    return 'Running!'


# Performing image Recognition on Image, sent as bytes via POST payload
@app.route('/detect', methods=["POST"])
def detect():
    gc.collect()
    print(request.data)
    imgBytes = request.data

    imgdata = base64.b64decode(imgBytes)
    # with open("temp.png", 'wb') as f:
    #     f.write(imgdata)
    # f.close()
    # print("successfully receieved image")

    # Pass image bytes to classifier
    result = classify.analyse(imgdata)

    # Return results as neat JSON object, using
    result = jsonify(result)
    print(result.json)

    response_data = result.json

    return response_data

if __name__ == '__main__':
    init()
    app.run()
