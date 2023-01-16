class User:
    count_id = 0
    def __init__(self, first_name, last_name, gender, email, birthday, address, payment_method, credit_number, exp_number, remarks):
        User.count_id += 1
        self.__user_id = User.count_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__gender = gender
        self.__email = email
        self.__birthday = birthday
        self.__address =address
        self.__payment_method = payment_method
        self.__credit_number = credit_number
        self.__exp_number = exp_number
        self.__remarks = remarks
    def get_user_id(self):
        return self.__user_id
    def get_first_name(self):
        return self.__first_name
    def get_last_name(self):
        return self.__last_name
    def get_gender(self):
        return self.__gender
    def get_email(self):
        return self.__email
    def get_birthday(self):
        return self.__birthday
    def get_address(self):
        return self.__address
    def get_payment_method(self):
        return self.__payment_method
    def get_credit_number(self):
        return self.__credit_number
    def get_exp_number(self):
        return self.__exp_number
    def get_remarks(self):
        return self.__remarks

    def set_user_id(self, user_id):
        self.__user_id = user_id
    def set_first_name(self, first_name):
        self.__first_name = first_name
    def set_last_name(self, last_name):
        self.__last_name = last_name
    def set_gender(self, gender):
        self.__gender = gender
    def set_email(self, email):
        self.__email = email
    def set_birthday(self, birthday):
        self.__birthday = birthday
    def set_address(self, address):
        self.__address = address
    def set_payment_method(self, payment_method):
        self.__payment_method = payment_method
    def set_credit_number(self, credit_number):
        self.__credit_number = credit_number
    def set_exp_number(self, exp_number):
        self.__exp_number = exp_number
    def set_remarks(self, remarks):
        self.__remarks = remarks
