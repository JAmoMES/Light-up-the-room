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
    query = room_info.find({})
    updated_content = {"$set": {
                                'r': 0,
                                'g': 0,
                                'b': 0,
                                'w': 0,
                                'Status' : 0,
                                'Time_out' : datetime.now(),
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
