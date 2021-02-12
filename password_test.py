import unittest
from password import User, Credentials

class TestUser(unittest.TestCase):

    def setUp(self):
        """
        Runs before each individual test method
        """
        self.new_user = User('Dorothy', 'Dorothy2')

    def test_init(self):
        """
        Checks if the object has been initialized correctly
        """
        self.assertEqual(self.new_user.username,'Dorothy')
        self.assertEqual(self.new_user.password,'Dorothy2')

    def test_save_user(self):
        """
        Test to see if user has been saved
        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)

    










if __name__ == '__main__':
    unittest.main()