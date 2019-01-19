from pymongo import MongoClient
client = MongoClient()

db = client['goodboy_db']
collection = db['users']


import datetime

def create_boy(name):
    post = {"boy": "name",
            "created": datetime.datetime.utcnow()}


