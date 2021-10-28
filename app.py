from flask import Flask
app = Flask(__name__)
@app.route('/')
@app.route("/api/v1.0/precipitation")
def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)

#def hello_world():
    #return 'Hello world'

## 9.5.1 SETUP THE DATABASE AND FLASK

import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)



print("example __name__ = %s", __name__)

if __name__ == "__main__":
    app.run(debug=True)
    print("example is being run directly.")
else:
    print("example is being imported")




## 9.5.2 CREATE THE WELCOME ROUTE

# def welcome():
#     return(
#     '''
#     Welcome to the Climate Analysis API!
#     Available Routes:
#     /api/v1.0/precipitation
#     /api/v1.0/stations
#     /api/v1.0/tobs
#     /api/v1.0/temp/start/end
#     ''')


## 9.5.3 PRECIPITATION ROUTE
#@app.route("/api/v1.0/precipitation")
# def precipitation():
#    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
#    precipitation = session.query(Measurement.date, Measurement.prcp).\
#     filter(Measurement.date >= prev_year).all()
#    precip = {date: prcp for date, prcp in precipitation}
#    return jsonify(precip)

## 9.5.4 STATIONS ROUTE


# python app.py