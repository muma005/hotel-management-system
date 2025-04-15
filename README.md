# hotel-management-system
# 🏨 Hotel Management System

This is a comprehensive **Hotel Management System** built with **Python** and **MySQL**, designed to simulate real-world hotel operations such as user authentication, room booking, and administrative management. It’s perfect for showcasing software development skills, database integration, and real-world problem-solving.

---

## 🚀 Features

- ✅ User Registration & Login (with Admin and Customer roles)
- ✅ Role-based Access (Customers can book; Admins can manage)
- ✅ Real-time Room Availability
- ✅ Room Booking and Cancellation
- ✅ Admin Dashboard for Managing Rooms & Users
- ✅ MySQL Database Integration
- ✅ CLI Interface (GUI optional)
- ✅ Clean and Scalable Code Structure
- ✅ Walkthrough Video Demo

---

## 🧰 Tech Stack

- **Python 3.8+**
- **MySQL**
- **MySQL Connector (mysql-connector-python)**  
- (Optional) **Tkinter** or **PyQt5** for GUI

---

## 🧠 Database Schema

### `users`
| Field     | Type         | Description                     |
|-----------|--------------|---------------------------------|
| id        | INT (PK)     | Auto-incremented ID             |
| username  | VARCHAR(50)  | Unique                          |
| password  | VARCHAR(255) | Hashed password                 |
| role      | ENUM         | 'admin' or 'customer'           |

### `
