from flask import Flask, request
from mongoengine import  connect
import sys
from pymongo.errors import ConnectionFailure

def initialize_db():
    try:
        connect('fastapi', host='mongodb://localhost:27017/') 
        print("Connected successfully!!!")
    except ConnectionFailure as e:
        print("Could not connect to MongoDB: %s" % e)
        sys.stderr.write("Could not connect to MongoDB: %s" % e)
        sys.exit(1)
