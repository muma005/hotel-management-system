import db.db_helper as db_helper

def add_room(room_type, price):
    db_helper.add_room(room_type, price)

def view_users():
    users = db_helper.get_all_users()
    for user in users:
        print(user)

def view_bookings():
    bookings = db_helper.get_all_bookings()
    for booking in bookings:
        print(booking)