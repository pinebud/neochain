#!/usr/bin/python3
import pymongo
import time
import pprint

from configuration import Config


class MongoClient(object):

    def __init__(self):
        config = Config()
        self.myclient = pymongo.MongoClient(config.get('database', 'host'), int(config.get('database', 'port')))
        self.mydb = self.myclient[config.get('database', 'db_name')]
        self.mydb.authenticate(config.get('database', 'user'), config.get('database', 'password'))

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
