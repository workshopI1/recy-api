from flask import Flask
import json
import sqlite3 as sql

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/waste/get')
def get_wastes():
    with sql.connect('workshop.db') as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        rows = cur.execute("SELECT w.Id, w.name, m.Id as id_mat, m.name as mat FROM waste w CROSS JOIN material m on w.id_material = m.Id").fetchall()
        return json.dumps( [dict(row) for row in rows])

@app.route('/recycling/get')
def get_recycling():
    with sql.connect('workshop.db') as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        rows = cur.execute("SELECT * FROM recycling").fetchall()
        return json.dumps([dict(row) for row in rows])

@app.route('/material/get')
def get_materials():
    with sql.connect('workshop.db') as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        rows = cur.execute("SELECT m.Id, m.name, m.barCode, r.Id as id_recycling, r.name as recycling FROM material m  CROSS JOIN recycling r on m.id_recycling = r.Id").fetchall()
        return json.dumps([dict(row) for row in rows])

@app.route('/material/add')
def add_material(name, barCode, id_recycling):
    with sql.connect('workshop.db') as con:
        cur = con.cursor()
        cur.execute("INSERT INTO material (name, barCode, id_recycling) VALUES(?,?,?)", (name, barCode, id_recycling))
        con.commit()
        con.close()

@app.route('/waste/add')
def add_waste(name, id_material):
    with sql.connect('workshop.db') as con:
        cur = con.cursor()
        cur.execute("INSERT INTO waste (name, id_material) VALUES(?,?)", (name,id_material))
        con.commit()
        con.close()
        
if __name__ == '__main__':
    app.run()
