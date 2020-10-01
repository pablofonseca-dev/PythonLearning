class User():

    def __init__(self, first_name, last_name, personal_mail, password, nickname):
        """
        Initialize a User object with the given values. 
        """
        self.first_name = first_name
        self.last_name = last_name
        self.personal_mail = personal_mail
        self.password = password
        self.nickname = nickname
        self.login_attempts = 0

    def describe_user(self): 
        """
        Returns all the details about the user created. 
        """
        stringFormatter =  "-------------------------------------------------------------------\n" 
        stringFormatter += "First Name: " + str(self.first_name.title()) + "\n"
        stringFormatter += "Last Name: " + str(self.last_name.title()) + "\n"
        stringFormatter += "Personal Mail: " + str(self.personal_mail) + "\n"
        stringFormatter += "Password: " + str(self.encrypt_user_key(self.password)) + "\n"
        stringFormatter += "Nickname: " + str(self.nickname) + "\n"
        stringFormatter += "Loggin Attempts: " + str(self.get_login_attempts()) + "\n"
        stringFormatter +=  "-------------------------------------------------------------------\n"
        return stringFormatter

    def greet_user(self):
        """
        Returns a message greeting the user created. 
        """
        return "Hello, " + str(self.first_name.title()) + '!'

    def encrypt_user_key(self, password):
        """
        Simulates a password encryption 
        """
        encryptedPassword = ""
        for x in range(len(password)):
            if(x <= 3):
                encryptedPassword += password[x]
            else:
                encryptedPassword += "*"
        return encryptedPassword

    def increment_login_attempts(self):
        """Increments the value of login attempts by one"""
        self.login_attempts += 1
    
    def get_login_attempts(self):
        """Returns the value of login attempts"""
        return self.login_attempts

    def reset_login_attempts(self):
        """Reset the value of login attempts"""
        self.login_attempts = 0    


        
my_profile = User("Pablo", "Fonseca", "pablo.fonsecam@outlook.com", "articdynamite3000", "ArticDynamite")

my_profile.increment_login_attempts()

my_profile.reset_login_attempts()
print(my_profile.describe_user())
