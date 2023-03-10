from flask import Flask, render_template, request, redirect, url_for, session, jsonify, flash,  render_template, Response
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
import pymssql
import pandas as pd
from bson import json_util
import json


import psycopg2  # pip install psycopg2
import psycopg2.extras

app = Flask(__name__)

app.secret_key = 'xyzsdfg'


def connection():
    conn = pymssql.connect(server='213.140.22.237\SQLEXPRESS',
                           user='livera.sasmitha', password='xxx123##', database='livera.samsmitha')
    return conn


mysql = MySQL(app)
CORS(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/exams')
def exams():
    # Create a connection
    conn = connection()
    # Create a cursor
    cur = conn.cursor(as_dict=True)
    # Execute the SQL SELECT statement
    cur.execute("SELECT * FROM verificaTec")
    # Fetch all rows from the SELECT statement
    list_users = cur.fetchall()
    # Render the index.html template and pass the list of students
    # return render_template('hehe.html', list_users = list_users)

    return jsonify(list_users)
    resp = jsonify(list_users)
    # return json.dumps(list_users)
    resp = json_util.dumps(list_users)
    return Response(resp, mimetype='application/json')


@app.route('/teachers')
def teachers():
    # Create a connection
    conn = connection()
    # Create a cursor
    cur = conn.cursor(as_dict=True)
    # Execute the SQL SELECT statement
    cur.execute("SELECT * FROM docente")
    # Fetch all rows from the SELECT statement
    list_users = cur.fetchall()
    # Render the index.html template and pass the list of students
    # return render_template('hehe.html', list_users = list_users)

    return jsonify(list_users)
    resp = jsonify(list_users)
    # return json.dumps(list_users)
    resp = json_util.dumps(list_users)
    return Response(resp, mimetype='application/json')

@app.route('/login', methods=['GET', 'POST'])
def login():
    #return jsonify({"message": request.json['email']}), 200
    if request.method == 'POST':
        email = request.json['email']
        password = request.json['password']
        #return jsonify({"message": email, "m2":password}), 200
        #print("ciao")
        conn = connection()
        # Create a cursor
        cursor = conn.cursor()
        # Execute a SELECT query
        cursor.execute('SELECT * FROM docente WHERE email=%s AND password=%s', (email, password))
        # Fetch the data
        user = cursor.fetchone()
        if user:
            return jsonify({"message": "Logged in successfully", "email":email, "password":password}), 200
        else:
            return jsonify("Doesn't match"), 400

    return jsonify({"message": "Error"}), 400


@app.route('/logout')
def logout():
    if 'loggedin' in session:
        session.pop('loggedin', None)
        session.pop('name', None)
        session.pop('email', None)
        return jsonify({"message": "Logged out successfully"}), 200
    else:
        return jsonify({"message": "You are not logged in"}), 400
        

@app.route('/register', methods=['GET', 'POST'])
def register():
    print("1")
    if request.method == 'POST':
        print("2")
        name = request.json['name']
        surname = request.json['surname']
        email = request.json['email']
        password = request.json['password']
        print("3")

        conn = connection()
        # Create a cursor
        cursor = conn.cursor()
        print("4")
        # Execute a SELECT query
        cursor.execute('SELECT * FROM docente WHERE email=%s', (email))
        print("5")
        # Fetch the data
        account = cursor.fetchone()
        print("6")
        if account:
            print("7")
            return jsonify({"message": "Account already exists"}), 400
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            print("8")
            return jsonify({"message": "Invalid email address"}), 400
        elif not name or not password or not email:
            print("9")
            return jsonify({"message": "Please fill out the form"}), 400
        else:
            # Execute an INSERT query
            print("10")
            cursor.execute(
                'INSERT INTO docente (name, surname, email, password) VALUES (%s, %s, %s, %s)', (name,surname, email, password))
            conn.commit()
            return jsonify({"message": "You have successfully registered"}), 201

@app.route('/users', methods=['POST', 'GET'])
def data():
    conn = connection()
    # Create a cursor
    cur = conn.cursor(as_dict=True)
    # POST a data to database
    if request.method == 'POST':
        body = request.json
        title = body['title']
        course = body['course']
        tipo = body['tipo']
        difficulty = body['difficulty']
        duration = body['duration']
        classe = body['classe']
        subject = body['subject']
        link = body['link']
        
        cur.execute("INSERT INTO verificaTec (title,course,tipo,difficulty,duration, classe,subject,link) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", (title, course,tipo,difficulty,duration,classe,subject,link))
        conn.commit()
        return jsonify({
            'status': 'Data is posted to SQLite!',
            'title': title,
            'course': course,
            'tipo':tipo,
            'difficulty':difficulty,
            'duration':duration,
            'classe':classe,
            'subject':subject,
            'link':link
        })

    # GET all data from database
    if request.method == 'GET':
        conn = connection()
        # Create a cursor
        cur = conn.cursor(as_dict=True)
        cur.execute("SELECT * FROM verificaTec WHERE course = 'Tecnico Informatico'")
        data = cur.fetchall()
        dataJson = []
        print(data)
        for doc in data:
            id = doc['id']
            title = doc['title']
            course = doc['course']
            tipo = doc['tipo']
            difficulty = doc['difficulty']
            duration = doc['duration']
            classe = doc['classe']
            subject = doc['subject']
            link = doc['link']

            dataDict = {
                'id' :id,
                'title': title,
                'course': course,
                'tipo': tipo,
                'difficulty': difficulty,
                'duration': duration,
                'classe': classe,
                'subject': subject,
                'link':link
            }
            dataJson.append(dataDict)
        return jsonify(dataJson)

@app.route('/users/<int:id>', methods=['GET', 'DELETE', 'PUT'])
def onedata(id):

    # GET a specific data by id
    if request.method == 'GET':
        conn = connection()
        # Create a cursor
        cur = conn.cursor(as_dict=True)
        cur.execute("SELECT * FROM verificaTec WHERE id = %s", (id, ))
        ver = cur.fetchone()
        dataDict = {
            'id': ver['id'],
            'title': ver['title'],
            'course': ver['course'],
            'tipo': ver['tipo'],
            'difficulty': ver['difficulty'],
            'duration': ver['duration'],
            'classe': ver['classe'],
            'subject': ver['subject'],
            'link':ver['link']
        }
        cur.close()
        conn.close()
        return jsonify(dataDict)
        

    # DELETE a data
    if request.method == 'DELETE':
        conn = connection()
        cur = conn.cursor()

        cur.execute('SELECT * FROM verificaTec WHERE id = %s', (id,))
        ver = cur.fetchone()
        if ver:
            cur.execute('DELETE FROM verificaTec WHERE id = %s', (id,))
            conn.commit()
            cur.close()
            conn.close()
            return jsonify({'status': 'Data id: ' + str(id) + ' is deleted!'})
        else:
            return jsonify({"message": "Data not found"}), 404

    # UPDATE a data by id
    if request.method == 'PUT':
        body = request.json
        title = body['title']
        course = body['course']
        tipo = body['tipo']
        difficulty = body['difficulty']
        duration = body['duration']
        classe = body['classe']
        subject = body['subject']
        link = body['link']


        conn = connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM verificaTec WHERE id = %s", (id,))
        ver = cur.fetchone()
        if ver:
            cur.execute("UPDATE verificaTec SET title = %s, course = %s, tipo = %s, difficulty = %s, duration = %s, classe = %s, subject = %s,link = %s WHERE id = %s", (title, course, tipo, difficulty, duration, classe, subject,link, id))
            conn.commit()
            cur.close()
            conn.close()
            return jsonify({'status': 'Data id: ' + str(id) + ' is updated!'})
        else:
            return jsonify({"message": "Data not found"}), 404

@app.route('/verifSci', methods=['POST', 'GET'])
def data1():
    conn = connection()
    # Create a cursor
    cur = conn.cursor(as_dict=True)
    # POST a data to database
    if request.method == 'POST':
        body = request.json
        title = body['title']
        course = body['course']
        tipo = body['tipo']
        difficulty = body['difficulty']
        duration = body['duration']
        classe = body['classe']
        subject = body['subject']
        link = body['link']
        
        cur.execute("INSERT INTO verificaTec (title,course,tipo,difficulty,duration, classe,subject,link) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", (title, course,tipo,difficulty,duration,classe,subject,link))
        conn.commit()
        return jsonify({
            'status': 'Data is posted to SQLite!',
            'title': title,
            'course': course,
            'tipo':tipo,
            'difficulty':difficulty,
            'duration':duration,
            'classe':classe,
            'subject':subject,
            'link':link
        })

    # GET all data from database
    if request.method == 'GET':
        conn = connection()
        # Create a cursor
        cur = conn.cursor(as_dict=True)
        cur.execute("SELECT * FROM verificaTec WHERE course = 'Liceo Scienze Applicate'")
        data = cur.fetchall()
        dataJson = []
        print(data)
        for doc in data:
            id = doc['id']
            title = doc['title']
            course = doc['course']
            tipo = doc['tipo']
            difficulty = doc['difficulty']
            duration = doc['duration']
            classe = doc['classe']
            subject = doc['subject']
            link = doc['link']
            dataDict = {
                'id' :id,
                'title': title,
                'course': course,
                'tipo': tipo,
                'difficulty': difficulty,
                'duration': duration,
                'classe': classe,
                'subject': subject,
                'link':link
            }
            dataJson.append(dataDict)
        return jsonify(dataJson)

@app.route('/verifSci/<int:id>', methods=['GET', 'DELETE', 'PUT'])
def onedata1(id):

    # GET a specific data by id
    if request.method == 'GET':
        conn = connection()
        # Create a cursor
        cur = conn.cursor(as_dict=True)
        cur.execute("SELECT * FROM verificaTec WHERE id = %s", (id, ))
        ver = cur.fetchone()
        dataDict = {
            'id': ver['id'],
            'title': ver['title'],
            'course': ver['course'],
            'tipo': ver['tipo'],
            'difficulty': ver['difficulty'],
            'duration': ver['duration'],
            'classe': ver['classe'],
            'subject': ver['subject'],
            'link':ver['link']
        }
        cur.close()
        conn.close()
        return jsonify(dataDict)
        

    # DELETE a data
    if request.method == 'DELETE':
        conn = connection()
        cur = conn.cursor()

        cur.execute('SELECT * FROM verificaTec WHERE id = %s', (id,))
        ver = cur.fetchone()
        if ver:
            cur.execute('DELETE FROM verificaTec WHERE id = %s', (id,))
            conn.commit()
            cur.close()
            conn.close()
            return jsonify({'status': 'Data id: ' + str(id) + ' is deleted!'})
        else:
            return jsonify({"message": "Data not found"}), 404

    # UPDATE a data by id
    if request.method == 'PUT':
        body = request.json
        title = body['title']
        course = body['course']
        tipo = body['tipo']
        difficulty = body['difficulty']
        duration = body['duration']
        classe = body['classe']
        subject = body['subject']
        link = body['link']

        conn = connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM verificaTec WHERE id = %s", (id,))
        ver = cur.fetchone()
        if ver:
            cur.execute("UPDATE verificaTec SET title = %s, course = %s, tipo = %s, difficulty = %s, duration = %s, classe = %s, subject = %s, link = %s WHERE id = %s", (title, course, tipo, difficulty, duration, classe, subject,link, id))
            conn.commit()
            cur.close()
            conn.close()
            return jsonify({'status': 'Data id: ' + str(id) + ' is updated!'})
        else:
            return jsonify({"message": "Data not found"}), 404


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
    os.environ['SERVER_LINK'] = "http://0.0.0.0:5000"

