
import json
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client.Hospital_BookingDB
collection = db.clientBookings
hospital_client = [
    {"_id": 1, "name": "John", "time": "9am - 10am",
        "symptoms": "Clumsiness or weakness", "DOB": "12/6/2000"},
    {"_id": 2, "name": "Peter", "time": "10am - 11am",
        "symptoms": "Difficulty walking or maintaining balance.", "DOB": "30/7/1980"},
    {"_id": 3, "name": "Amy", "time": "11am - 12pm",
        "symptoms": "Dizziness or vertigo.", "DOB": "27/05/1970"},
    {"_id": 4, "name": "Hannah", "time": "12pm - 1pm", "symptoms": "Fatigue.", "DOB": "22/08/1990"},
    {"_id": 5, "name": "Michael", "time": "1pm - 2pm",
        "symptoms": "stomack disturbance", "DOB": "15/06/2001"}
]
# collection.insert_many(hospital_client)
print('***************************************', '\n')
# Printing the number of documents in the collections

print("The number of documents in my collection: ", collection.count_documents({}))
print('***************************************', '\n')
# query entries in the collection using regex
myquery = {"symptoms": {"$regex": "^Di"}}

mydoc = collection.find(myquery)
print("All entries with 'Di' in field 'symptoms': ", collection.count_documents(myquery))
# Print all entries
print('***************************************', '\n')
print('Printing all entries:')
# iterate through the collection and read the entries
for x in collection.find():
    print(json.dumps(x, indent=2))
