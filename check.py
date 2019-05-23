
import pymongo

url="mongodb://127.0.0.1:27017"
client=pymongo.MongoClient(url)
Database=client['fullstack']
collection=Database['student']
student=collection.find({})
for student in student:
    print(student)