from flask import Flask, request
from flask_cors import CORS, cross_origin
from flask_pymongo import PyMongo
from datetime import datetime

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://exceed_group16:7vyf5srq@158.108.182.0:2255/exceed_group16'
mongo = PyMongo(app)
cors = CORS(app, resource={r"/": {"origins": "*"}})

admin_db = mongo.db.admin_user
people_db = mongo.db.people
room_info_db = mongo.db.room_info
bill_db = mongo.db.electric_bill
graph_db = mongo.db.graph_peoole
#---------------------------- HARDWARE --------------------------------------#
@app.route('/hardware', methods=['POST'])
@cross_origin()
def hardware_insert_one():
    data = request.json
    myInsert = {
            'Type' : 'Room_info',
            'ID' : data["ID"],
            'r': int(data["r"]),
            'g': int(data["g"]),
            'b': int(data["b"]),
            'w': int(data["w"]),
            'Status' : int(1),
            'Time_in' : datetime.now(),
            'Time_out' : None,
            'Discord' : None
            }
    room_info_db.insert_one(myInsert)
    return {'result': 'light on'}


@app.route('/hardware', methods=['PATCH'])
@cross_origin()
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
@cross_origin()
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

#--------------------------------- FRONT END ----------------------------------#

############## SWITCH ##################

@app.route('/switch', methods=['POST'])
@cross_origin()
def switch_insert_one():
    data = request.json
    myInsert = {
            'Type' : 'Room_info',
            'ID' : int(data["ID"]),
            'r': int(data["r"]),
            'g': int(data["g"]),
            'b': int(data["b"]),
            'w': int(data["w"]),
            'Status' : int(1),
            'Time_in' : datetime.now(),
            'Time_out' : None,
            'Discord' : None
            }
    room_info_db.insert_one(myInsert)
    return {'result': 'light on'}


@app.route('/switch', methods=['PATCH'])
@cross_origin()
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
@cross_origin()
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

############## GRAPH ##################

@app.route('/cost_graph',methods=['GET'])
@cross_origin()
def cost_graph_cal():
    data = room_info_db.find().sort("_id", -1)
    res = {
            "ID" : 0,
            "Time_in" : 0
          }
    return {"result": res}

@app.route('/people_graph',methods=['GET'])
@cross_origin()
def people_graph_cal():
    res= {}
    return {"result" : res}

@app.route('/people', methods=['POST'])
@cross_origin()
def switch_insert_one():
    data = request.json
    myInsert = {
            'Type' : 'Room_info',
            'ID' : data["ID"],
            'r': data["r"],
            'g': data["g"],
            'b': data["b"],
            'w': data["w"],
            'Status' : int(1),
            'Time_in' : datetime.now(),
            'Time_out' : None,
            'Discord' : None
            }
    room_info_db.insert_one(myInsert)
    return {'result': 'light on'}
 
 #calculate elec bill (ฮอนหาสูตรคิดค่าไฟมาใส่ให้หน่อย) time in sec
def cal_bill(time):
    cost = time
    #cost = ...
    return cost

 #James
@app.route('/elecbill', methods=['GET'])
@cross_origin()
def bill():
    frequency = request.args
    time = str(datetime.now()).split(':')
    bill_min = bill_db.find_one({"frequency": 0})
    bill_hour = bill_db.find_one({"frequency": 1})
    bill_day = bill_db.find_one({"frequency": 2})
    active_room = room_info_db.find({"status":1})
    sum =0
    for ele in active_room:
        sum+=1
    bill_min["time"].append(bill_min["time"][-1]+1)
    bill_min["cost"].append(bill_min["cost"][-1] + cal_bill(sum))
    bill_db.update_one({"frequency": 0},{"$set":{"time":bill_min["time"]}})
    bill_db.update_one({"frequency": 0},{"$set":{"cost":bill_min["cost"]}})
    if len(bill_min["cost"]) > 60:
        bill_min["cost"] = bill_min["cost"] [1:]
    if time[1] == '00':
        bill_hour["time"].append(bill_hour["time"][-1]+1)
        bill_hour["cost"].append(bill_min["cost"][-1])
        if len(bill_hour["cost"]) > 60:
            bill_hour["cost"] = bill_hour["cost"] [1:]
        bill_db.update_one({"frequency": 1},{"$set":{"time":bill_hour["time"]}})
        bill_db.update_one({"frequency": 1},{"$set":{"cost":bill_hour["cost"]}})
    if time[0][-2:] == '00':
        bill_day["time"].append(bill_day["time"][-1]+1)
        bill_day["cost"].append(bill_hour["cost"][-1])
        if len(bill_day["cost"]) > 24:
            bill_day["cost"] = bill_day["cost"] [1:]
        bill_db.update_one({"frequency": 2},{"$set":{"time":bill_day["time"]}})
        bill_db.update_one({"frequency": 2},{"$set":{"cost":bill_day["cost"]}})
    l = 60
    if frequency == 2:
        l = 24
    cost = [bill_min["time"],bill_hour["time"],bill_day["time"]]
    size = list(range(l))
    my_get = {
        "time" : l,
        "cost" : cost[frequency]
    }
    return {'result': my_get}

@app.route('/people_graph', methods=['GET'])
@cross_origin()
def bill():
    frequency = request.args
    time = str(datetime.now()).split(':')
    graph_min = graph_db.find_one({"frequency": 0})
    graph_hour = graph_db.find_one({"frequency": 1})
    graph_day = graph_db.find_one({"frequency": 2})
    active_room = room_info_db.find({"status":1})
    sum =0
    for ele in active_room:
        sum+=1
    graph_min["time"].append(graph_min["time"][-1]+1)
    graph_min["people"].append(sum)
    graph_db.update_one({"frequency": 0},{"$set":{"people":graph_min["people"]}})
    if len(graph_min["people"]) > 60:
        graph_min["people"] = graph_min["people"] [1:]
    if time[1] == '00':
        graph_hour["time"].append(graph_hour["time"][-1]+1)
        graph_hour["people"].append(sum(graph_min["people"])/len(graph_min["people"]))
        if len(graph_hour["people"]) > 60:
            graph_hour["people"] = graph_hour["people"] [1:]
        graph_db.update_one({"frequency": 1},{"$set":{"people":graph_hour["people"]}})
    if time[0][-2:] == '00':
        graph_day["time"].append(graph_day["time"][-1]+1)
        graph_day["people"].append(sum(graph_hour["people"])/len(graph_hour["people"]))
        if len(graph_day["people"]) > 24:
            graph_day["people"] = graph_day["people"] [1:]
        graph_db.update_one({"frequency": 2},{"$set":{"people":graph_day["people"]}})
    l = 60
    if frequency == 2:
        l = 24
    people = [graph_min["people"],graph_hour["people"],graph_day["people"]]
    size = list(range(l))
    my_get = {
        "time" : l,
        "people" : people[frequency]
    }
    return {'result': my_get}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='3000', debug=True)

