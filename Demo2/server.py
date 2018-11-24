from flask import Flask, request
import pymysql


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Docker Fans !"

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    age = int(request.form.get("age"))

    db = pymysql.connect("mysql","root","123123","test" )
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    # Prepare SQL query to INSERT a record into the database.
    sql = "INSERT INTO Person(NAME,AGE) VALUES ('%s',%d)" %(name,age)
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()
        return "sucess",200
    except Exception as e:
        print(e)
        # Rollback in case there is any error
        db.rollback()
        return "failed",500

@app.route("/list")
def list():
    db = pymysql.connect("mysql","root","123123","test" )
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # execute SQL query using execute() method.
    cursor.execute("SELECT * FROM Person")
    
    # Fetch a single row using fetchone() method.
    data = cursor.fetchall()
    return str(data),200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)