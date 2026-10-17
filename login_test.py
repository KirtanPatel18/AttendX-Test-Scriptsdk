
import unittest

def login(username, password):
    if not username or not password:
        return "Username and password required"
    if username == "student" and password == "pass123":
        return "Login successful"
    return "Invalid username or password"


class LoginTest(unittest.TestCase):

    def test_valid_login(self):
        self.assertEqual(
            login("student", "pass123"),
            "Login successful"
        )

    def test_empty_username(self):
        self.assertEqual(
            login("", "pass123"),
            "Username and password required"
        )

    def test_wrong_password(self):
        self.assertEqual(
            login("student", "wrong"),
            "Invalid username or password"
        )

    def test_empty_fields(self):
        self.assertEqual(
            login("", ""),
            "Username and password required"
        )


if __name__ == "__main__":
    unittest.main()

