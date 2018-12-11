#!/usr/bin/python3
import pymongo
import time
import pprint


class MongoClient(object):

    def __init__(self):
        self.myclient = pymongo.MongoClient('47.92.3.134', 27017)
        self.mydb = self.myclient["neochain"]
        self.mydb.authenticate('sense', '123456')

    def insert_chain(self, value):
        return self.mydb.get_collection('neochain').insert_one({'value': value, 'created_time': time.time()})

    def find_latest_chain(self):
        return self.mydb.get_collection('neochain').find({'value.chain': {'$exists': True}}).sort('created_time',
                    direction=pymongo.DESCENDING).limit(1)

    def insert_nodes(self, value):
        return self.mydb.get_collection('neonodes').insert_one({'value': value, 'created_time': time.time()})

    def find_latest_nodes(self):
        return self.mydb.get_collection('neonodes').find({'value.node': {'$exists': True}}).sort('created_time',
                                                                direction=pymongo.DESCENDING).limit(1)


# client = MongoClient()
# client.insert({'test': '001'})
# client.insert({'test': '002'})
# result = client.find_latest_chain()
# for item in result:
#     pprint.pprint(item)
