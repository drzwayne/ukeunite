class Cart:
    fi = []
    fn = ['Extravagant Slumber', 'Sweet Dreams', 'Quiet Elegance', 'Flash-Fried-Fillet']
    fp = [18.5, 11.5, 37, 7.4]
    fq = [1, 1, 1, 1]
    esp = 18.50
    esq = 1
    sdp = 11.50
    sdq = 1
    qep = 37.00
    qeq = 7.4
    bdp = 7.40
    bdq = 1
    count_id = 0
    def __init__(self, fi, fn,fp,fq, esp, esq, sdp,sdq, qep, qeq, bdp,bdq):
        Cart.count_id += 1
        self.__cart_id = Cart.count_id
        self.__fi = fi
        self.__fn = fn
        self.__fp = fp
        self.__fq = fq
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
    def get_fi(self):
        return self.__fi
    def get_fn(self):
        return self.__fn
    def get_fp(self):
        return self.__fp
    def get_fq(self):
        return self.__fq
    def get_amt(self):
        return self.__amt
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
    def set_fi(self,fi):
        self.__fi = fi
    def set_fn(self,fn):
        self.__fn = fn
    def set_fp(self,fp):
        self.__fp = fp
    def set_fq(self,fq):
        self.__fq = fq
    def set_amt(self):
        self.__amt = self.__fq * self.__fp
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


