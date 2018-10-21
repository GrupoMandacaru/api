from database.settings import db

cupulas = db.cupulas

def set_cupula(cupula):
    cupula_id = cupulas.insert_one(cupula).inserted_id
    return cupula_id

def get_cupula(cupula_name):
    cupula = cupulas.find_one()
    return cupula

def get_all_cupulas():
    all_cupulas = []
    for cupula in cupulas.find({}, { "name": 1, "_id": 0 }):
        all_cupulas.append(cupula["name"])
    return all_cupulas

def set_cupula_attribute(cupula_name, attribute):
    cupula = db[cupula_name]
    cupula_id = cupula.insert_one(cupula).inserted_id
    return cupula_id

def get_cupula_attributes(cupula_name):
    cupula = db[cupula_name]
    query = cupula.find({}, { "_id": 0 })
    attributes = []
    for attribute in query:
        attributes.append(attribute)
    return attributes