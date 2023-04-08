from nicegui import app, ui
from tinydb import TinyDB, Query
import hashlib

db = TinyDB('db.json')
User = Query()

nickname = ""

@app.get("/login/{uspas}")
def login_checker(uspas: str):
    parsed = uspas.split('^')
    user = parsed[0]
    password = parsed[1]
    pashash = hashlib.sha256(password.encode('utf-8')).hexdigest()
    result = db.search(User.username == user)
    if result is None:
        return False
    return result[0]

ui.run()