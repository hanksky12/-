# import
from pymongo import MongoClient
#from bson.objectid import ObjectId #這東西再透過ObjectID去尋找的時候會用到

# connection
conn = MongoClient("mongodb://127.0.0.1") # 如果你只想連本機端的server你可以忽略，遠端的url填入: mongodb://<user_name>:<user_password>@ds<xxxxxx>.mlab.com:<xxxxx>/<database_name>，請務必既的把腳括號的內容代換成自己的資料。
db = conn["db104"]
#collection = db.inventory
collection = db.employee
for doc in collection.find():
	print(doc)

# test if connection success
#collection.stats  # 如果沒有error，你就連線成功了。
# for doc in collection.find({"$and":[{"quantity":{"$in":[50,30]}},{"price":10}]}):
# 	print(doc)