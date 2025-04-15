import hashlib
import db.db_helper as db_helper

def register_user(username, password, role):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    db_helper.add_user(username, hashed_password, role)

def login_user(username, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    user = db_helper.get_user(username)
    if user and user['password'] == hashed_password:
        return user
    return None