from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
import os

app = Flask(__name__)

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
		cur.execute("SELECT type FROM recycling JOIN materials ON recycling.id = materials.id_recycling JOIN waste ON materials.id = waste.id_material WHERE waste.barcode=%s",[barcode])
		res = cur.fetchone()
		cur.close()
		if res != None:
			return jsonify(res),200
		else:
			return 'Erreur'
	except Exception as e:
		return 'Erreur'
	finally:
		cur.close()

@app.route('/idMaterial/<id>', methods=["GET"])
def getRecyclingTypeByIdMaterial(id):
	try:
		cur = mysql.connection.cursor()
		cur.execute("SELECT type FROM recycling JOIN materials ON recycling.id = materials.id_recycling JOIN waste ON materials.id = waste.id_material WHERE id_material=%s",id)
		res = cur.fetchone()
		if res != None:
			return jsonify(res),200
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

if __name__ == "__main__":
	app.run(debug=True)
