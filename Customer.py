class Cart:
    esp = 18.50
    esq = 1
    sdp = 11.50
    sdq = 1
    qep = 37.00
    qeq = 7.4
    bdp = 7.40
    bdq = 1
    count_id = 0
    sdc_id = 0
    qec_id = 0
    fffc_id = 0
    def __init__(self, esp, esq, sdp,sdq, qep, qeq, bdp,bdq):
        Cart.count_id += 1
        Cart.sdc_id += 1
        Cart.qec_id += 1
        Cart.fffc_id += 1
        self.__cart_id = Cart.count_id
        self.__cart2_id = Cart.sdc_id
        self.__cart3_id = Cart.qec_id
        self.__cart4_id = Cart.fffc_id
        self.__esp = esp
        self.__esq = esq
        self.__sdp = sdp
        self.__sdq = sdq
        self.__qep = qep
        self.__qeq = qeq
        self.__bdp = bdp
        self.__bdq = bdq
    def get_cart_id(self):
        return self.__cart_id
    def get_cart2_id(self):
        return self.__cart2_id
    def get_cart3_id(self):
        return self.__cart3_id
    def get_cart4_id(self):
        return self.__cart4_id
    def get_esp(self):
        return self.__esp
    def get_esq(self):
        return self.__esq
    def get_sdp(self):
        return self.__sdp
    def get_sdq(self):
        return self.__sdq
    def get_qep(self):
        return self.__qep
    def get_qeq(self):
        return self.__qeq
    def get_bdp(self):
        return self.__bdp
    def get_bdq(self):
        return self.__bdq
    def set_cart_id(self, cart_id):
        self.__cart_id = cart_id
    def set_cart2_id(self, cart2_id):
        self.__cart2_id = cart2_id
    def set_cart3_id(self, cart3_id):
        self.__cart3_id = cart3_id
    def set_cart4_id(self, cart4_id):
        self.__cart4_id = cart4_id
    def set_esp(self,esp):
        self.__esp = esp
    def set_esq(self,esq):
        self.__esq = esq
    def set_sdp(self,sdp):
        self.__sdp = sdp
    def set_sdq(self,sdq):
        self.__sdq = sdq
    def set_qep(self,qep):
        self.__qep = qep
    def set_qeq(self,qeq):
        self.__qeq = qeq
    def set_bdp(self,bdp):
        self.__bdp = bdp
    def set_bdq(self,bdq):
        self.__bdq = bdq

class Minus(Cart):
    def __init__(self, esp, esq, sdp,sdq, qep, qeq, bdp,bdq):
        super().__init__(esp, esq, sdp,sdq, qep, qeq, bdp,bdq)
        Cart.count_id -= 1
        self.__cart_id = Cart.count_id
    def get_cart_id(self):
        return self.__cart_id
    def set_cart_id(self, cart_id):
        self.__cart_id = cart_id
