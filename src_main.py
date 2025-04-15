from auth import register_user, login_user
from booking import book_room
from admin import add_room, view_users, view_bookings

def main():
    print("Welcome to the Hotel Management System!")
    while True:
        print("1. Register\n2. Login\n3. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            username = input("Enter username: ")
            password = input("Enter password: ")
            role = input("Enter role (admin/customer): ")
            register_user(username, password, role)
        elif choice == 2:
            username = input("Enter username: ")
            password = input("Enter password: ")
            user = login_user(username, password)
            if user:
                print(f"Welcome, {user['username']}!")
                if user['role'] == 'admin':
                    print("Admin Dashboard")
                    admin_menu()
                else:
                    print("Customer Dashboard")
                    customer_menu(user['id'])
        elif choice == 3:
            break

def admin_menu():
    while True:
        print("1. Add Room\n2. View Users\n3. View Bookings\n4. Logout")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            room_type = input("Enter room type: ")
            price = float(input("Enter price: "))
            add_room(room_type, price)
        elif choice == 2:
            view_users()
        elif choice == 3:
            view_bookings()
        elif choice == 4:
            break

def customer_menu(user_id):
    while True:
        print("1. Book Room\n2. Logout")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            room_type = input("Enter room type: ")
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            book_room(user_id, room_type, start_date, end_date)
        elif choice == 2:
            break

if __name__ == "__main__":
    main()