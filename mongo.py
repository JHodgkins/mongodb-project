import os
import pymongo

if os.path.exists("env.py"):
    import env

MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "myFirstDB"
COLLECTION = "celebrities"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("connection successful")
        return conn
    except pymongo.errorsConnectionFailure as e:
        print("could not connect to MongoDB: %s") % e


conn = mongo_connect(MONGO_URI)
coll = conn[DATABASE][COLLECTION]

# Insert one new record
# new_doc = {
#     "first": "douglas",
#     "last": "adams",
#     "dob": "11/03/1952",
#     "hair_color": "grey",
#     "occupation": "writer",
#     "nationality": "british"
#     }
# coll.insert_one(new_doc)


# Insert multiple records
# send an array of objects
# new_docs = [{
#     "first": "terry",
#     "last": "pratchett",
#     "dob": "28/04/1948",
#     "gender": "m",
#     "hair_color": "not much",
#     "occupation": "writer",
#     "nationality": "british"
# }, {
#     "first": "george",
#     "last": "rr martin",
#     "dob": "20/09/1948",
#     "gender": "m",
#     "hair_color": "white",
#     "occupation": "writer",
#     "nationality": "american"
# }]
# coll.insert_many(new_docs)

# search and return a record with the criteria
# documents = coll.find({"first": "douglas"})

# delete an entry with criteria
# coll.delete_one({"first": "douglas"})

# update one record
# coll.update_one({"nationality": "american"}, {"$set": {"hair_color": "maroon"}})

# update multiple records
# coll.update_many({"nationality": "american"}, {"$set": {"hair_color": "maroon"}})

documents = coll.find({"nationality": "american"})

for doc in documents:
    print(doc)
