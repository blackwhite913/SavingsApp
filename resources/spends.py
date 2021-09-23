from flask_restful import Resource, reqparse
from models.spends import SpendModel
import datetime
from db import db



class Spend(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('spend_price',
                        type=float,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('icon_number',
                        type=int,
                        required=True,
                        help="This field cannot be left blank!"
                        )
   
    def get(self, title):
        spend= SpendModel.find_by_name(title)
        if spend:
            return spend.json()
        return {'message': 'Item not found'}, 404

    def post(self,title):
        if SpendModel.find_by_name(title):
            return {'message': "An spending with name '{}' already exists.".format(title)}, 400

        data = Spend.parser.parse_args()

        spend = SpendModel(title,**data)
        try:
            spend.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}, 500

        return spend.json(), 201

    def delete(self, title):
        spend = SpendModel.find_by_name(title)
        if spend:
            spend.delete_from_db()
            return {'message': 'Item deleted.'}
        return {'message': 'Item not found.'}, 404

    def put(self, title):
        data = Spend.parser.parse_args()

        spend = SpendModel.find_by_name(title)

        if spend:
            spend.spend_price = data['spend_price']
            spend.icon_number = data['icon_number']
            spend.date = datetime.datetime.now()

        else:
            spend = SpendModel(title, **data)

        spend.save_to_db()

        return spend.json()


class SpendingList(Resource):
    def get(self):
        return {'spendings': list(map(lambda x: x.json(), SpendModel.query.all()))}
        #ItemModel.query.all=SELECT * FROM items

    def delete(self):
        db.session.query(SpendModel).delete()
        db.session.commit()
        return {"message":"all the spendings have been deleted"}

    