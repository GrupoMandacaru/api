from pymongo import MongoClient

client = MongoClient('mongodb://admin:Admin123@ecodomo-shard-00-00-3mokt.mongodb.net:27017,ecodomo-shard-00-01-3mokt.mongodb.net:27017,ecodomo-shard-00-02-3mokt.mongodb.net:27017/test?ssl=true&replicaSet=Ecodomo-shard-0&authSource=admin&retryWrites=true')

db = client.ecodomo