######## ยังไม่เสร็จนะครับ ##########

import pymongo
import time
from datetime import datetime

#--------------------------------------------------------#
client = MongoClient('mongodb://exceed_group16:7vyf5srq@158.108.182.0:2255/exceed_group16')
admin_db =  client['admin_user']
people_db = client['people']
room_info_db = client['room_info']

def insert_people(time):
    my_insert = {
                    "type" : people by time,
                    "total_people" : 0,
                    "total_used_time" : 0,
                    "date" : date_time.now(),
                    "time" : time,
                    "avg_people" : 0
                }
    people_db.insert_one(my_insert)

def update_people(time):
    filt = {"time": time}
    query = room_info.aggregate([
        { "$match": { "$or": [ 
                                { "time_out": None }, 
                                { "time_out": {"$gte": start_time, "$lt": stop_time } } 
                             ] 
                    } 
        },
        { "$count": "total_people"}
        ],allowDiskUse=True)
    total_people = query["total_people"]
    updated_content = {"$set": {
                                    "total_people" : total_people,
                                    "total_used_time" : date_time.now() - start_time,
                                    "date" : date_time.now(),
                                    "avg_people" : total_people / (date_time.now() - start_time).min
                                }
                      }
    people_db.update_one(filt, updated_content)
    return {'result': 'light off'}

while(True):
    if datetime.now().hour = 6 and datetime.now().min = 0:
        time = "morning"
        star_ttime = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 6, 0, 0) 
        end_time = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 12, 0, 0)
        insert_people(time)
    if datetime.now().hour = 12 and datetime.now().min = 0:
        time = "afternoon"
        star_ttime = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 12, 0, 0) 
        end_time = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 16, 0, 0)
        insert_people(time)
    if datetime.now().hour = 16 and datetime.now().min = 0:
        time = "evening"
        star_ttime = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 16, 0, 0) 
        end_time = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 20, 0, 0)
        insert_people(time)
    if datetime.now().hour = 20 and datetime.now().min = 0:
        time = "night"
        star_ttime = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 20, 0, 0) 
        end_time = datetime(datetime.now().year, datetime.now().month, datetime.now().day+1, 6, 0, 0)
        insert_people(time)
    time.sleep(1)
