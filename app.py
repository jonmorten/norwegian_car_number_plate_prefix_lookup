# coding: utf-8


from flask import Flask
from flask import Response
from flask import render_template
from classes.Db import Db


def json_response(result):
    return Response(result, mimetype='text/json')


def html_response(result):
    return Response(result, mimetype='text/html')


app = Flask(__name__)
db = Db('db/vehicle_reg_prefix.db')


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/prefix/<name>")
def prefix_by_area(name):
    result = ''
    if name is not None and len(name) == 2:
        sql = """
            SELECT area.name AS area_name, county.name AS county_name
            FROM area JOIN county
            ON area.county_id = county.id
            WHERE area.id IN (SELECT area_id FROM prefix WHERE name LIKE '%s')
        """
        result = db.fetchall(sql % (name))
    return json_response(result)


@app.route("/prefix/")
def prefixes():
    result = db.fetchall("SELECT name FROM prefix")
    return json_response(result)


"""
@app.route("/county/")
def county():
    result = db.fetchall("SELECT * FROM county")
    return json_response(result)
"""


"""
@app.route("/area/")
def area():
    result = db.fetchall("SELECT * FROM area")
    return json_response(result)
"""


if __name__ == "__main__":
    app.run()
