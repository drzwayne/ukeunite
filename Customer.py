class Total:
    es = {}
    sd = {'price':11.5, 'qty':1}
    def __init__(self):
        Total.es = {'price':18.5, 'qty':1}
        self.__totales = Total.es
    def increase(self):
        Total.es['qty'] += 1
        if Total.es['qty'] >1:
            Total.es['price'] *= Total.es['qty']
    def decrease(self):
        Total.es['qty'] -= 1
        if Total.es['qty'] >0:
            Total.es['price'] *= Total.es['qty']
    def totales(self):
        return self.__totales
class Cart:
    esp = 18.50
    esq = 1
    count_id = 0
    def __init__(self, esp, esq):
        self.__cart_id = Cart.count_id
        self.__esp = esp
        self.__esq = esq
    def get_cart_id(self):
        return self.__cart_id
    def get_esp(self):
        return self.__esp
    def get_esq(self):
        return self.__esq
    def set_cart_id(self, cart_id):
        self.__cart_id = cart_id
    def update_cart_id(self):
        self.__cart_id = Cart.count_id
    def set_esp(self,esp):
        self.__esp = esp
    def set_esq(self,esq):
        self.__esq = esq
    def decqty(self):
        Cart.count_id = 0
        self.__cart_id = Cart.count_id
    def incqty(self):
        Cart.count_id += 1
        self.__cart_id = Cart.count_id


class Cbrt:
    sdp = 11.50
    sdq = 1
    cunt_id = 0
    def __init__(self, sdp, sdq):
        self.__cbrt_id = Cbrt.cunt_id
        self.__sdp = sdp
        self.__sdq = sdq
    def get_cbrt_id(self):
        return self.__cbrt_id
    def get_sdp(self):
        return self.__sdp
    def get_sdq(self):
        return self.__sdq
    def set_cbrt_id(self, cbrt_id):
        self.__cbrt_id = cbrt_id
    def set_sdp(self,sdp):
        self.__sdp = sdp
    def set_sdq(self,sdq):
        self.__sdq = sdq
    def decqtyb(self):
        Cbrt.cunt_id = 0
        self.__cbrt_id = Cbrt.cunt_id
    def incqtyb(self):
        Cbrt.cunt_id += 1
        self.__cbrt_id = Cbrt.cunt_id

class Ccrt:
    qep = 37
    qeq = 1
    csnt_id = 0
    def __init__(self, qep, qeq):
        self.__ccrt_id = Ccrt.csnt_id
        self.__qep = qep
        self.__qeq = qeq
    def get_ccrt_id(self):
        return self.__ccrt_id
    def get_qep(self):
        return self.__qep
    def get_qeq(self):
        return self.__qeq
    def set_ccrt_id(self, ccrt_id):
        self.__ccrt_id = ccrt_id
    def set_qep(self,qep):
        self.__qep = qep
    def set_qeq(self,qeq):
        self.__qeq = qeq
    def decqtyc(self):
        Ccrt.csnt_id = 0
        self.__ccrt_id = Ccrt.csnt_id
    def incqtyc(self):
        Ccrt.csnt_id += 1
        self.__ccrt_id = Ccrt.csnt_id
class Cdrt:
    bdp = 7.4
    bdq = 1
    cznt_id = 0
    def __init__(self, bdp, bdq):
        self.__cdrt_id = Cdrt.cznt_id
        self.__bdp = bdp
        self.__bdq = bdq
    def get_cdrt_id(self):
        return self.__cdrt_id
    def get_bdp(self):
        return self.__bdp
    def get_bdq(self):
        return self.__bdq
    def set_cdrt_id(self, cdrt_id):
        self.__cdrt_id = cdrt_id
    def set_bdp(self,bdp):
        self.__bdp = bdp
    def set_bdq(self,bdq):
        self.__bdq = bdq
    def decqtyd(self):
        Cdrt.cznt_id = 0
        self.__cdrt_id = Cdrt.cznt_id
    def incqtyd(self):
        Cdrt.cznt_id += 1
        self.__cdrt_id = Cdrt.cznt_id

class Roytut:
    p1 = {'code':1, 'name': 'Extravagant Slumber', 'image':'/static/ess.png', 'price':18.50}
    p2 = {'code':2, 'name': 'Sweet Dreams', 'image':'/static/sd.png', 'price':11.50}
    p3 = {'code':3, 'name': 'Quiet Elegance', 'image':'/static/qe.png', 'price':37.00}
    p4 = {'code':4, 'name': 'Flash-Fried-Fillet', 'image':'/static/fff.png', 'price':7.40}

class Subtotalprice:
    subtotal_count = 0
    def __init__(self):
        Subtotalprice.subtotal_count += 1
        self.__subtotalcount = Subtotalprice.subtotal_count
    def get_subtotalcount(self):
        return self.__subtotalcount
    def set_subtotalcount(self, subtotalcount):
        self.__subtotalcount = subtotalcount
    def get_tproduct1(self):
        return self.__tproduct1
    def set_tproduct1(self):
        self.__tproduct1 = 18.5 * self.__subtotalcount
    def get_tproduct2(self):
        return self.__tproduct2
    def set_tproduct2(self):
        self.__tproduct2 = 11.5 * self.__subtotalcount
    def get_tproduct3(self):
        return self.__tproduct3
    def set_tproduct3(self):
        self.__tproduct3 = 37 * self.__subtotalcount
    def get_tproduct4(self):
        return self.__tproduct4
    def set_tproduct4(self):
        self.__tproduct4 = 7.4 * self.__subtotalcount

