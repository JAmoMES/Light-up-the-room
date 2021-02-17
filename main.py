from flask import Flask, request
from flask_pymongo import PyMongo
from datetime import datetime

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
            'Type' : 'Room_info',
            'ID' : data["ID"],
            'r': data["r"],
            'g': data["g"],
            'b': data["b"],
            'w': data["w"],
            'Status' : 1,
            'Time_in' : datetime.now(), 
            'Time_out' : None,
            'Discord' : None
            }
    room_info_db.insert_one(myInsert)
    return {'result': 'light on'}


@app.route('/hardware', methods=['PATCH'])
def update_one():
    data = request.json
    filt = {"ID": data["ID"], "Status": 1}
    updated_content = {"$set": {
                                'r': 0,
                                'g': 0,
                                'b': 0,
                                'w': 0,
                                'Status' : 0,
                                'Time_out' : datetime.now(),
                               }
                      }
    room_info_db.update_one(filt, updated_content)
    return {'result': 'light off'}

@app.route('/hardware', methods=['GET'])
def find():
    flit = {"Status": 1}
    query = room_info_db.find(flit)
    res = []
    for data in query:
        tmp = {
            "ID" : data["ID"],
            "r": data["r"],
            "g": data["g"],
            "b": data["b"],
            "w": data["w"]
        }
        res.append(tmp)
    return {"result": res}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='50005', debug=True)
    