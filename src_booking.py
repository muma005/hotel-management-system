import db.db_helper as db_helper

def check_availability(room_type, start_date, end_date):
    return db_helper.is_room_available(room_type, start_date, end_date)

def book_room(user_id, room_type, start_date, end_date):
    if check_availability(room_type, start_date, end_date):
        db_helper.create_booking(user_id, room_type, start_date, end_date)
        print("Booking successful!")
    else:
        print("Room not available.")