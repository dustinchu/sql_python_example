from db import db
import pandas as pd
import json as js
class Note(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))


    def __init__(self, username, password):
        self.username = username
        self.password = password

    def json(self):
        return {'username': self.username, 'password': self.password}

    def create_db():
        db.create_all()
        return Note

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        db.session.close

    def find_by_name(self, name):
        return  list(map(lambda x: x.json(), db.session.query(Note).filter_by(username=name)))


    def get_all_notes(self):
        return {'items': list(map(lambda x: x.json(), db.session.query(Note).all()))}

    def update_to_db(self, name):
        try:
            db.session.query(Note).filter_by(username=name).update({'password':'55'})
            db.session.commit()
            db.session.close
            return {'status':'ok'}
        except :
            return {'status':'error'}

    def find_by_count(self, name):
        try:
            return db.session.query(Note).filter_by(username=name).count()
        except :
            return 0
    def sqlcode_to_db(self, name):

        result = db.session.execute(
            "SELECT * from users where username={name}".format(name=name))

        # If no rows were returned (e.g., an UPDATE or DELETE), return an empty list
        if result.returns_rows == False:
            response = []

        # Convert the response to a plain list of dicts
        else:
            response = [dict(row.items()) for row in result]

        # Output the query result as JSON
        rdata = js.dumps(response, ensure_ascii=False)
        return js.loads(rdata)

# Note.create_db()
data = {}
data ['username']='1323'
data ['password']= None
# print(type(data))
user=Note(**data)

# print(type(user.find_by_name()))
# user.find_name().username
# user.save_to_db()

# da = user.find_by_name('123')
# df = pd.DataFrame(da).to_excel("excel.xlsx", index=False)

print(user.sqlcode_to_db('123'))