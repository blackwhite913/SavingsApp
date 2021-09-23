from db import db
import datetime


class SpendModel(db.Model):
    __tablename__ = 'spends'

    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(80))
    spend_price=db.Column(db.Float(precision=2))
    icon_number=db.Column(db.Integer)
    date=db.Column(db.DateTime(timezone=True),server_default=db.func.now())
    

    def __init__(self, title,spend_price,icon_number):
        self.title=title
        self.spend_price=spend_price
        self.icon_number=icon_number
        self.date=datetime.datetime.now()

        

    def json(self):
        return {'title':self.title,'spend_price':self.spend_price,'icon_number':self.icon_number,'date':str(self.date)}

    @classmethod
    def find_by_name(cls,title):
        return cls.query.filter_by(title=title).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

       

    
        


    

