from tinydb import TinyDB, Query
import hashlib
import uuid

db = TinyDB('db.json')
User = Query()

pas = "parola"

pashash = hashlib.sha256(pas.encode('utf-8')).hexdigest()

idu = str(uuid.uuid4())

db.insert({'username': 'kristee','password':pashash,'nickname':'shoymu','id':idu})