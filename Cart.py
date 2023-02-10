class Cart:
    count_id = 0
    def __init__(self, es, sd, qe, fff, amt):
        Cart.count_id += 1
        self.__cart_id = Cart.count_id
        self.__es = es
        self.__sd = sd
        self.__qe = qe
        self.__fff = fff
        self.__amt = amt
    def get_cart_id(self):
        return self.__cart_id
    def get_es(self):
        return self.__es
    def get_sd(self):
        return self.__sd
    def get_qe(self):
        return self.__qe
    def get_fff(self):
        return self.__fff
    def get_amt(self):
        return self.__amt
    def set_cart_id(self, cart_id):
        self.__cart_id = cart_id
    def set_es(self,es):
        self.__es = es
    def set_sd(self,sd):
        self.__sd = sd
    def set_qe(self,qe):
        self.__qe = qe
    def set_fff(self,fff):
        self.__fff = fff
    def set_amt(self,amt):
        self.__amt = amt



