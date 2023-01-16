class Guest:
    count_id = 0
    def __init__(self, first_name, address, payment_method, credit_number, exp_number, remarks):
        Guest.count_id += 1
        self.__guest_id = Guest.count_id
        self.__first_name = first_name
        self.__address =address
        self.__payment_method = payment_method
        self.__credit_number = credit_number
        self.__exp_number = exp_number
        self.__remarks = remarks
    def get_guest_id(self):
        return self.__guest_id
    def get_first_name(self):
        return self.__first_name
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

    def set_guest_id(self, guest_id):
        self.__guest_id = guest_id
    def set_first_name(self, first_name):
        self.__first_name = first_name
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
