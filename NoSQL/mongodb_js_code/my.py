import pprint
import pymongo
from pymongo import MongoClient
client = MongoClient()
db = client['test']
for i in db.webs.find():
    pprint.pprint(i)