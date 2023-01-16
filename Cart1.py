from User import User
class Order:
    def __init__(self, sd, es, qe, fff ):

        self.__sd = sd
        self.__es = es
        self.__qe = qe
        self.__fff = fff


    def get_food_img(self):
        return self.__sd

    def get_food_name(self):
        return self.__es

    def get_quanity(self):
        return self.__qe

    def get_price(self):
        return self.__fff



    def set_food_img(self, sd):
        self.__sd = sd

    def set_food_name(self, es):
        self.__es = es

    def set_quantity(self, qe):
        self.__qe = qe

    def set_price(self, fff):
        self.__fff = fff
