import random
import string

class User:
    """
    Create User class that generates new user instance
    """

    user_list = []

    def __init__(self,username,password):
        """
        Defines the properties of a user
        """

        self.username = username
        self.password = password

    def save_user(self):
        """
        Saves a new user instance to the user list
        """
        User.user_list.append(self)

    @classmethod

    def user_exist(cls,username,password):
        """
        Verifies whether the user is in the user_list or not
        """

        current_user = ''
        for user in User.user_list:
            if(user.username == username and user.password == password):
                current_user = user.name
            return current_user

class Credentials:
    """
    Create credentials class to help create new objects of credentials
    """

    credential_list = []

    def __init__(self,account_name, username, password):
        """
        Defines user credentials to be stored
        """

        self.account_name = account_name
        self.username = username
        self.password = password

    def save_credentials(self):
        """
        Store new credentials in the credentials list
        """
        Credentials.credential_list.append(self)

    def delete_credentials(self):
        """
        Deletes a saved credential from the list
        """
        Credentials.credential_list.remove(self)  


    @classmethod

    def credentials_exist(cls, account_name):
        """
        Verify whether credentials are in the user list or not
        """

        for credentials in cls.credential_list:
            if credentials.account_name == account_name:
                return True 

            return False

    @classmethod

    def display_credentials(cls):
        """
        Display all credentials in the credentials list
        """
        return cls.credential_list
        

    def generate_password(self, stringLength = 8):
        """
        Generate random passwords 8 characters long
        """
        password = string.ascii_uppercase + string.ascii_lowercase + string.digits + "(|/~!.@,)#{?$[%]^}&*"
        return ''.join(random.choice(password) for i in range(stringLength))
        
        
