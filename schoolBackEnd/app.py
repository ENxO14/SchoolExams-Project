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
    if request.method == 'POST':
        name = request.form['name']
        lname = request.form['surname']
        email = request.form['email']
        password = request.form['password']
        
        conn = connection()
        # Create a cursor
        cursor = conn.cursor()

        # Execute a SELECT query
        cursor.execute('SELECT * FROM docente WHERE email=%s', (email))

        # Fetch the data
        account = cursor.fetchone()

        if account:
            return jsonify({"message": "Account already exists"}), 400
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            return jsonify({"message": "Invalid email address"}), 400
        elif not name or not password or not email:
            return jsonify({"message": "Please fill out the form"}), 400
        else:
            # Execute an INSERT query
            cursor.execute(
                'INSERT INTO users (name, surname, email, password) VALUES (%s, %s, %s, %s)', (name,lname, email, password))
            conn.commit()
            session['loggedin'] = True
            session['name'] = name
            session['email'] = email
            return jsonify({"message": "You have successfully registered"}), 201

    return jsonify({"message": "Invalid request method"}), 400


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
