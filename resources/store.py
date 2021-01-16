from flask_restful import Resource
from models.store import StoreModel


class Store(Resource):

    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': 'Store not found'}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': "store name '{}' already exist".format(name)}, 400
        store = StoreModel(name)

        try:
            store.save_to_db()
        except:
            return {'message': 'problems with creating store'}, 500
        return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.update()
            return {'message': 'Store {} deleted'.format(name)}
        return {'message': 'Ther is no Store {} '.format(name)}


class StoreList(Resource):
    def get(self):
        return {'stores': [x.json() for x in StoreModel.query.all()]}
