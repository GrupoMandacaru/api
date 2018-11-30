from database.settings import db
import datetime

cupulas = db.cupulas

def set_cupula_info(cupula_info):
    cupula_id = cupulas.insert_one(cupula_info).inserted_id
    return cupula_id

def get_cupula_info(cupula_id):
    for cupula in cupulas.find({ "cupula_id": cupula_id }, { "_id": 0 }):
        return cupula

def get_all_cupulas():
    all_cupulas = []
    for cupula in cupulas.find({}, { "_id": 0 }):
        all_cupulas.append(cupula)
    return all_cupulas

def set_cupula_attribute(cupula_id, args):
    cupula = db[cupula_id]
    args['date'] = datetime.datetime.now()
    cupula.insert_one(args)
    return 'ok'

def get_cupula_attributes(cupula_id, limit):
    cupula = db[cupula_id]
    attributes_docs = []
    query = cupula.find({}, { "_id": 0 }).sort([("date", -1)]).limit(limit)
    for attributes_doc in query:
        if limit == 1: return attributes_doc
        attributes_docs.append(attributes_doc)
    return attributes_docs