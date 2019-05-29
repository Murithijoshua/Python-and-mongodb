
import pymongo
#this can be used for checking wether the database is communicating using pycharm

""" for start ensure your db is working by using the following keyword $sudo service mongod status"""
url="mongodb://hostcode,port"
client=pymongo.MongoClient(url)
Database=client['fullstack']
collection=Database['student']
student=collection.find({})
for student in student:
    print(student)
