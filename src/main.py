from pymongo import MongoClient

host, port = ('localhost', 27017)
client = MongoClient(host, port)


db = client.test_database
collection = db.test_collection

test_id = collection.insert_one({"test": 123}).inserted_id

print(test_id)

test = collection.find_one()

print(test)
