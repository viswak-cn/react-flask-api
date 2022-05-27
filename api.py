import time
import mysql.connector
from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
  return 'Hello, Docker!'


@app.route('/val')
def get_val():
    mydb = mysql.connector.connect(
    host="mysqldb",
    user="root",
    password="p@ssw0rd1",
    database="db"
    )
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM count")
    return count['counter']



@app.route('/initdb')
def initdb():
    mydb = mysql.connector.connect(
    host="black-hummingbird-8ggfj1hv.ws.trilogy.devspaces.com",
    user="root",
    password="p@ssw0rd1"
    )
    cursor = mydb.cursor()

    cursor.execute("DROP DATABASE IF EXISTS db")
    cursor.execute("CREATE DATABASE db")
    cursor.close()

    mydb = mysql.connector.connect(
    host="mysqldb",
    user="root",
    password="p@ssw0rd1",
    database="db"
    )
    cursor = mydb.cursor()

    cursor.execute("DROP TABLE IF EXISTS count")
    cursor.execute("CREATE TABLE count (counter int)")
    cursor.close()
    return "db Initialized"

if __name__ == "__main__":
  app.run(host ='0.0.0.0')