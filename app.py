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
        rows = cur.execute("SELECT * FROM waste").fetchall()
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
        rows = cur.execute("SELECT * FROM material m  CROSS JOIN recycling r on m.id_recycling = r.Id").fetchall()
        return json.dumps([dict(row) for row in rows])

if __name__ == '__main__':
    app.run()
