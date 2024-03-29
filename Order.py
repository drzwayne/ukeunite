class Qty:
    count1_id = 0
    def __init__(self):
        self.__sum += Qty.count1_id
        self.__add = Qty.count1_id + 1
        self.__minus = Qty.count1_id - 1
    def get_sum(self):
        return self.__sum
    def get_add(self):
        return self.__add
    def get_minus(self):
        return self.__minus
    def set_sum(self, sum):
        self.__sum = sum
    def set_add(self, add):
        self.__add = add
    def set_minus(self, minus):
        self.__minus = minus

class Order:
    count_id = 0
    def __init__(self, food_img, food_name, quantity, price):
        Order.count_id += 1
        self.order_id = Order.count_id
        self.food_img = food_img
        self.food_name = food_name
        self.quantity = quantity
        self.price = price
    def get_order_id(self):
        return self.order_id

    def get_food_img(self):
        return self.food_img

    def get_food_name(self):
        return self.food_name

    def get_quanity(self):
        return self.quantity

    def get_price(self):
        return self.price

    def set_order_id(self, order_id):
        self.order_id = order_id

    def set_food_img(self, food_img):
        self.food_img = food_img

    def set_food_name(self, food_name):
        self.food_name = food_name

    def set_quantity(self, quantity):
        self.quantity = quantity

    def set_price(self, price):
        self.price = price
