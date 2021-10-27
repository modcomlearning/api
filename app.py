from flask import *
# create a Flask app
app = Flask(__name__)
# Password  empty
import pymysql
con = pymysql.connect(host='localhost', user='root', password='',
                      database='api')

# CRUD Operation - CREATE
@app.route('/post', methods=['POST'])
def add_post():
    from flask import request
    json = request.json
    firstname = json['firstname']
    lastname = json['lastname']
    residence = json['residence']
    phone = json['phone']
    request = json['request']

    SQL_Query = "INSERT INTO posts(firstname, lastname, residence, phone, request) VALUES(%s, %s, %s, %s, %s)"
    data = (firstname, lastname, residence, phone, request)
    Pointer = con.cursor()
    Pointer.execute(SQL_Query, data)
    con.commit()
    response = jsonify({"msg": 'Post  Received!'})
    response.status_code = 200
    return response




if __name__ == '__main__':
    app.run(debug=True)














