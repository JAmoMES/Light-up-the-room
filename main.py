from flask import Flask, request
from flask_pymongo import PyMongo
improt datetime

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://exceed_group16:7vyf5srq@158.108.182.0:2255/exceed_group16'
mongo = PyMongo(app)

admin_db = mongo.db.admin_user
people_db = mongo.db.people
room_info_db = mongo.db.room_info

@app.route('/hardware', methods=['POST'])
def insert_one():
    data = request.json
    myInsert = {
            'Type' : {Room_info},
            'ID' : data["ID"],
            'r': data["r"],
            'g': data["g"],
            'b': data["b"],
            'w': data["w"],
            'Status' : 1,
            'Time_in' : datetime.datetime(), 
            'Time_out' : None,
            'Discord' : - 
            }
    room_info.insert_one(myInsert)
    return {'result': 'room_info insert successfully'}


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='50005', debug=True)
    