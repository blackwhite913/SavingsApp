from flask import Flask
from flask_restful import Api
from resources.spends import Spend,SpendingList


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key = 'jose'
api=Api(app)


api.add_resource(Spend,'/spend/<string:title>')
api.add_resource(SpendingList,'/spendingList')

if __name__=='__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000,debug=True)
