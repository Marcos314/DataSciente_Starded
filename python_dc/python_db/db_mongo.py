from pymongo import MongoClient
import datetime

conn = MongoClient('localhost', 27017)

db = conn.cadastrodb


collection = db.cadastrodb
print(type(collection))


post1 = {"codigo": "ID-9987725",
        "prod_name": "Geladeira",
        "marcas": ["brastemp","consul","eletrolux"],
        "data-cadastro": datetime.datetime.utcnow()}

collection = db.posts

#post_id = collection.insert_one(post1)


# for post in collection.find():
#     print(post)

print(db.collection_names())
