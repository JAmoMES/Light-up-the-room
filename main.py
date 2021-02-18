from flask import Flask, request
from flask_pymongo import PyMongo
from datetime import datetime

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://exceed_group16:7vyf5srq@158.108.182.0:2255/exceed_group16'
mongo = PyMongo(app)

admin_db = mongo.db.admin_user
people_db = mongo.db.people
room_info_db = mongo.db.room_info

#---------------------------- HARDWARE --------------------------------------
@app.route('/hardware', methods=['POST'])
def hardware_insert_one():
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
def hardware_update_one():
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
def hardware_find():
    query = room_info_db.find().sort("_id", -1).limit(2)
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

#--------------------------------- FRONT END ----------------------------------
@app.route('/switch', methods=['POST'])
def switch_insert_one():
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


@app.route('/switch', methods=['PATCH'])
def switch_update_one():
    data = request.json
    filt = {"ID": data["ID"], "Status": 1}
    if data['r'] == 0 and data['g'] == 0 and data['b'] == 0 and data['w'] == 0:
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
    else:
        updated_content = {"$set": {
                                    'r': data['r'],
                                    'g': data['g'],
                                    'b': data['b'],
                                    'w': data['w'],
                                }
                        }
        room_info_db.update_one(filt, updated_content)
        return {'result': 'light changed'}

# @app.route('/switch', methods=['GET'])
# def switch_find():
#     query = room_info_db.find().sort("_id", -1).limit(2)
#     res = []
#     for data in query:
#         tmp = {
#             "ID" : data["ID"],
#             "r": data["r"],
#             "g": data["g"],
#             "b": data["b"],
#             "w": data["w"]
#         }
#         res.append(tmp)
#     return {"result": res}

@app.route('/switch', methods=['GET'])
def switch_find():
    id = request.args.get("ID")
    filt = {"Status": 1 , "ID": int(id)}
    data = room_info_db.find_one(filt)
    res = {
            "ID" : int(id),
            "Status" : 0,
            "r": 0,
            "g": 0,
            "b": 0,
            "w": 0
        }
    if (data == None):
        return {"result" : res}
    res["Status"] = data["Status"]
    res["r"] = data['r']
    res["g"] = data['g']
    res["b"] = data['b']
    res["w"] = data['w']
    return {"result": res}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='50005', debug=True)
