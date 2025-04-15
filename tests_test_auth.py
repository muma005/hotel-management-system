import unittest
from auth import register_user, login_user
from db.db_helper import get_user

class TestAuth(unittest.TestCase):
    def test_register_and_login_user(self):
        username = "test_user"
        password = "password123"
        role = "customer"

        # Register user
        register_user(username, password, role)
        user = get_user(username)
        self.assertIsNotNone(user)
        self.assertEqual(user['username'], username)

        # Login user
        logged_in_user = login_user(username, password)
        self.assertIsNotNone(logged_in_user)
        self.assertEqual(logged_in_user['username'], username)

if __name__ == "__main__":
    unittest.main()