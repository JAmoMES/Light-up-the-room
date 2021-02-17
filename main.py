from flask import Flask, request
from flask_pymongo import PyMongo
improt time

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://exceed_group16:7vyf5srq@158.108.182.0:2255/exceed_group16'
mongo = PyMongo(app)

admin = mongo.db.admin_user
people = mongo.db.people
room_info = mongo.db.room_info

@app.route('/create', methods=['POST'])
def insert_one():
    car_number = request.args.get('car_number')
    data = request.json
    myInsert = {
            "car_number": car_number,
            "time_in": data["time_in"],
            "time_out": data["time_out"]
            }
    myCollection.insert_one(myInsert)
    return {'result': 'Created successfully'}


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='50005', debug=True)
    