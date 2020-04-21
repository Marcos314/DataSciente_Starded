import pymongo

conn = pymongo.MongoClient()

#print(conn.database_names())

db = conn.cadastrodb

#print(db.collection_names())

#db.create_collection("minhaColecao")
#print(db.collection_names())


# db.minhaColecao.insert_one({
#     'titulo':'MongoDB com Python',
#     'descricao': 'mongo db noSql',
#     'likes': 100,
#     'tags': ['mongodb','database','NoSql']
# })

print(db.minhaColecao.find_one())