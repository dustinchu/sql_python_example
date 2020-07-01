import sys
sys.path.append("C:/Users/dustinchu/Desktop/mysql/")
from model.user import Note

Note.create_db()
data = {'username':'123','password':'321'}
print(type(data))
user=Note(**data)
user.save_to_db()