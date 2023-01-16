class loginuser:
    def __init__(self, loginemail, loginpassword):
        self.__loginemail = loginemail
        self.__loginpassword = loginpassword

    def get_loginemail(self):
        return self.__loginemail

    def get_loginpassword(self):
        return self.__loginpassword

    def set_loginemail(self, loginemail):
        self.__loginemail = loginemail

    def set_password(self, loginpassword):
        self.__loginpassword = loginpassword

