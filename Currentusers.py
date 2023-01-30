class CurrentUser:
    def __init__(self, user_id, first_name, last_name, gender, email, password, birthday, address, payment_method, credit_number, cvc, exp_number, remarks):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.email = email
        self.password = password
        self.birthday = birthday
        self.address =address
        self.payment_method = payment_method
        self.credit_number = credit_number
        self.cvc = cvc
        self.exp_number = exp_number
        self.remarks = remarks

    def get_user_id(self):
        return self.user_id
    def get_first_name(self):
        return self.first_name
    def get_last_name(self):
        return self.last_name
    def get_gender(self):
        return self.gender
    def get_email(self):
        return self.email
    def get_password(self):
        return self.password
    def get_birthday(self):
        return self.birthday
    def get_address(self):
        return self.address
    def get_payment_method(self):
        return self.payment_method
    def get_credit_number(self):
        return self.credit_number
    def get_cvc(self):
        return self.cvc
    def get_exp_number(self):
        return self.exp_number
    def get_remarks(self):
        return self.remarks

    def set_user_id(self, user_id):
        self.user_id = user_id
    def set_first_name(self, first_name):
        self.first_name = first_name
    def set_last_name(self, last_name):
        self.last_name = last_name
    def set_gender(self, gender):
        self.gender = gender
    def set_email(self, email):
        self.email = email
    def set_password(self, password):
        self.password = password
    def set_birthday(self, birthday):
        self.birthday = birthday
    def set_address(self, address):
        self.address = address
    def set_payment_method(self, payment_method):
        self.payment_method = payment_method
    def set_credit_number(self, credit_number):
        self.credit_number = credit_number
    def set_cvc(self, cvc):
        self.cvc = cvc
    def set_exp_number(self, exp_number):
        self.exp_number = exp_number
    def set_remarks(self, remarks):
        self.remarks = remarks
