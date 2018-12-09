#!/usr/bin/python3

import pymongo
import time


class MongoClient(object):

    def __init__(self):
        self.myclient = pymongo.MongoClient("mongodb://sense:123456@47.92.3.134:27017/")
        self.mydb = self.myclient["neochain"]

    def insert(self, value):
        self.mydb.get_collection('neochain').insert_one({'value': value, 'created_time': time.time()})

    def find_latest(self, name):
        return self.mydb[name].find().sort('created_time', direction=pymongo.DESCENDING).limit(1)


client = MongoClient()
client.insert({'test': '001'})
# client.insert({'test': '002'})
print(client.find_latest())
