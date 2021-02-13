import unittest
from password import User, Credentials

class TestUser(unittest.TestCase):
    """
    Defines test cases for user class
    """

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


class TestCredentials(unittest.TestCase):
    """
    Defines test cases for Credentials class
    """

    def setUp(self):
        self.new_credentials = Credentials('Facebook', 'Dorothy', 'Dorothy2')

    def test_init(self):
        """
        Checks if a new credential instance has been initialized correctly
        """
        self.assertEqual(self.new_credentials.account_name, 'Facebook')
        self.assertEqual(self.new_credentials.username, 'Dorothy')
        self.assertEqual(self.new_credentials.password, 'Dorothy2')

    def tearDown(self):
        """
        Cleans up after each test case has run
        """
        Credentials.credential_list = []

    def test_save_multiple_accounts(self):
        """
        Check whether we can save multiple credentials in our list
        """
        self.new_credentials.save_credentials()
        test_credentials = Credentials('Twitter', 'Dorothy', 'Muhonja5')
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credential_list),2)

    def test_delete_credentials(self):
        """
        Test if we can remove credentials from our list
        """
        self.new_credentials.save_credentials()
        test_credentials = Credentials('Twitter', 'Dorothy', 'Muhonja5')
        test_credentials.save_credentials()
        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credential_list),1)

    def test_find_credentials(self):
        """
        Check if we can find a credential by account name
        """
        self.new_credentials.save_credentials()
        test_credentials = Credentials('Twitter', 'Dorothy', 'Muhonja5')
        test_credentials.save_credentials()
        find_credentials = Credentials.find_account_name('Twitter')
        self.assertEqual(find_credentials.account_name,test_credentials.account_name)
    
    def test_credentials_exist(self):
        """
        test to check if we can return True or False in regards to finding the credentials
        """
        self.new_credentials.save_credentials()
        test_credentials = Credentials('Twitter','Dorothy','Muhonja5')
        test_credentials.save_credentials()
        credentials_exist = Credentials.credentials_exist('Twitter')
        self.assertTrue(credentials_exist)

    def display_credentials(self):
        """
        Displays all credentials saved by the user
        """
        self.assertEqual(Credentials.display_credentials(), Credentials.credential_list)
    
    def test_generate_password(self):
        generated_password = self.new_credentials.generate_password()
        self.assertEqual(len(generated_password), 8)


if __name__ == '__main__':
    unittest.main()
