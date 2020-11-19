from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
import os
import json
import sqlite3 as sql
import classify
import base64
import os
import gc

from flask_cors import CORS, cross_origin
import json
import env
from classify import init

app = Flask(__name__)
CORS(app)

#Conf db
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "Workshop"

mysql = MySQL(app)

@app.route('/barcode/<barcode>', methods=["GET"])
def getRecyclingTypeByBarcode(barcode):
	try:
		cur = mysql.connection.cursor()
		cur.execute("SELECT type,materials.name,waste.name FROM recycling JOIN materials ON recycling.id = materials.id_recycling JOIN waste ON materials.id = waste.id_material WHERE waste.barcode=%s",[barcode])
		res = cur.fetchone()
		final=json.dumps({"name": res[2], "material": res[1], "trash": res[0]}, sort_keys=True)
		cur.close()
		if res != None:
			return final,200
		else:
			return 'Erreur'
	except Exception as e:
		return 'Erreur'
	finally:
		cur.close()
		
@app.route('/add/Waste/', methods=["POST"])
def addWaste():
	name = request.form.get('name')
	id_material = request.form.get('id_material')
	barcode = request.form.get('barcode')
	try:
		cur = mysql.connection.cursor()
		cur.execute("INSERT INTO waste(name,id_material,barcode) VALUES (%s,%s,%s)",[name,id_material,barcode])
		mysql.connection.commit()
		return 'Added'
	except Exception as e:
		return e.__str__()
	finally:
		cur.close()
		
@app.route('/idMaterial/<id>', methods=["GET"])
def getRecyclingTypeByIdMaterial(id):
	try:
		cur = mysql.connection.cursor()
		cur.execute("SELECT type,materials.name,waste.name FROM recycling JOIN materials ON recycling.id = materials.id_recycling JOIN waste ON materials.id = waste.id_material WHERE id_material=%s",id)
		res = cur.fetchone()
		final=json.dumps({"name": res[2], "material": res[1], "trash": res[0]}, sort_keys=True)
		if res != None:
			return final,200
		else:
			return 'Erreur'
	except Exception as e:
		return 'Erreur'
	finally:
		cur.close()

@app.route('/wastes', methods=["GET"])
def getWastes():
	try:
		cur = mysql.connection.cursor()
		result = cur.execute("SELECT * FROM waste")
		if result > 0 :
			wasteDetails = cur.fetchall()
			return jsonify(wasteDetails),200
		else:
			return 'Erreur'
	except Exception as e:
		return 'Erreur'
	finally:
		cur.close()

@app.route('/materials', methods=["GET"])
def getMaterials():
	try:
		cur = mysql.connection.cursor()
		result = cur.execute("SELECT id,name FROM materials")
		if result > 0 :
			materialsDetails = cur.fetchall()
			return jsonify(materialsDetails),200
		else:
			return 'Erreur'
	except Exception as e:
		return 'Erreur'
	finally:
		cur.close()
		
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

if __name__ == "__main__":
	init()
	app.run(debug=True)
