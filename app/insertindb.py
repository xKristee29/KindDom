from tinydb import TinyDB, Query
import hashlib
import uuid

db = TinyDB('db.json')
User = Query()

pas = "user"

pashash = hashlib.sha256(pas.encode('utf-8')).hexdigest()

idu = str(uuid.uuid4())

db.insert({'username': 'test','password':pashash,'nickname':'human','id':idu})