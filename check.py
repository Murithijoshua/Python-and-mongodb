
import pymongo
#this can be used for checking wether the database is communicating
url="mongodb://hostcode,port"
client=pymongo.MongoClient(url)
Database=client['fullstack']
collection=Database['student']
student=collection.find({})
for student in student:
    print(student)
