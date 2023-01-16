from flask import Flask, render_template, request, redirect, url_for, flash
from Forms import CreateUserForm, CreateGuestForm
import shelve, User, Guest, Order
import jyserver.Flask as jsf
app = Flask(__name__)
@app.route('/')
def home():
    return App.render(render_template('home.html'))

@app.route('/cart')
def cart():
    return App.render(render_template('cart.html'))
@jsf.use(app)
class App:
    def __init__(self):
        self.count = 0
        self.escount = 0
        self.sdcount = 0
        self.qecount = 0
        self.fffcount = 0
    def esadd(self):
        self.escount += 1
        self.js.document.querySelector('.es').value = self.escount
    def esminus(self):
        if self.escount > 0:
            self.escount -= 1
        else:
            pass
        self.js.document.querySelector('.es').value = self.escount
    def increment(self):
        self.count += 1
        self.js.document.querySelector('.cartQty').value = self.count
        orders_dict = {}
        db = shelve.open('order.db','c')
        try:
            orders_dict = db['Orders']
        except:
            print("Error in retrieving number of items from order.db.")
        order = {'fn':'Extravagant Slumber', 'price':18.50, 'qty':0}
        orders_dict = order
        db['Orders'] = orders_dict
        db.close()
        orders_dict = {}
        db = shelve.open('order.db', 'r')
        orders_dict = db['Orders']
        db.close()
        qtys_dict ={}
        db = shelve.open('qty.db','c')
        qtys_list = []
        for key in qtys_dict:
            qty = qtys_dict.get(key)
            qtys_list.append(qty)
        try:
            qtys_dict = db['Qtys']
        except:
            print('Error in retrieving count')
        qty = self.count
        qtys_dict = qty
        db['Qtys'] = qtys_dict
        self.js.document.querySelector('.cartQty').value = self.count
        db.close()
        qtys_dict = {}
        db = shelve.open('qty.db', 'r')
        qtys_dict = db['Qtys']
        db.close()
        qtys_list = []
        for key in qtys_dict:
            qty = qtys_dict.get(key)
            qtys_list.append(qty)
    def decrement(self):
        if self.count > 0:
            self.count -= 1
        else:
            pass
        self.js.document.querySelector('.cartQty').value = self.count
        orders_dict = {}
        db = shelve.open('order.db','w')
        try:
            orders_dict = db['Orders']
        except:
            print("Error in retrieving number of items from order.db.")
        order = {'fn':'Extravagant Slumber', 'price':18.50, 'qty':0}
        orders_dict = order
        db['Orders'] = orders_dict
        db.close()
        orders_dict = {}
        db = shelve.open('order.db', 'r')
        orders_dict = db['Orders']
        db.close()
        qtys_dict ={}
        db = shelve.open('qty.db','w')
        try:
            qtys_dict = db['Qtys']
        except:
            print('Error in retrieving count')
        qty = self.count
        qtys_dict = qty
        db['Qtys'] = qtys_dict
        self.js.document.querySelector('.cartQty').value = self.count
        db.close()
        qtys_dict = {}
        db = shelve.open('qty.db', 'r')
        qtys_dict = db['Qtys']
        db.close()
        qtys_list = []
        for key in qtys_dict:
            qty = qtys_dict.get(key)
            qtys_list.append(qty)
@app.route('/createUser', methods=['GET', 'POST'])
def create_user():
    create_user_form = CreateUserForm(request.form)
    if request.method == 'POST' and create_user_form.validate():
        users_dict = {}
        db = shelve.open('user.db', 'c')
        try:
            users_dict = db['Users']
        except:
            print("Error in retrieving Users from user.db.")
        user = User.User(create_user_form.first_name.data, create_user_form.last_name.data, create_user_form.gender.data, create_user_form.email.data, create_user_form.birthday.data, create_user_form.address.data, create_user_form.payment_method.data, create_user_form.credit_number.data, create_user_form.exp_number.data, create_user_form.remarks.data)
        users_dict[user.get_user_id()] = user
        db['Users'] = users_dict
        db.close()
        return redirect(url_for('retrieve_users'))
    return render_template('createUser.html', form=create_user_form)
@app.route('/guestPayment', methods=['GET', 'POST'])
def create_guest():
    create_guest_form = CreateGuestForm(request.form)
    if request.method == 'POST' and create_guest_form.validate():
        guests_dict = {}
        db = shelve.open('guest.db', 'c')
        try:
            guests_dict = db['Guests']
        except:
            print("Error in retrieving Guests from guest.db.")
        guest = Guest.Guest(create_guest_form.first_name.data, create_guest_form.address.data, create_guest_form.payment_method.data, create_guest_form.credit_number.data, create_guest_form.exp_number.data, create_guest_form.remarks.data)
        guests_dict[guest.get_guest_id()] = guest
        db['Guests'] = guests_dict
        db.close()
        return redirect(url_for(''))
    return render_template('guestPayment.html', form=create_guest_form)
@app.route('/retrieveUsers')
def retrieve_users():
    users_dict = {}
    db = shelve.open('user.db', 'r')
    users_dict = db['Users']
    db.close()
    users_list = []
    for key in users_dict:
        user = users_dict.get(key)
        users_list.append(user)
    return render_template('retrieveUsers.html', count=len(users_list), users_list=users_list)
@app.route('/updateUser/<int:id>/', methods=['GET', 'POST'])
def update_user(id):
    update_user_form = CreateUserForm(request.form)
    if request.method == 'POST' and update_user_form.validate():
        users_dict = {}
        db = shelve.open('user.db', 'w')
        users_dict = db['Users']
        user = users_dict.get(id)
        user.set_first_name(update_user_form.first_name.data)
        user.set_last_name(update_user_form.last_name.data)
        user.set_gender(update_user_form.gender.data)
        user.set_email(update_user_form.email.data)
        user.set_birthday(update_user_form.birthday.data)
        user.set_address(update_user_form.address.data)
        user.set_payment_method(update_user_form.payment_method.data)
        user.set_credit_number(update_user_form.credit_number.data)
        user.set_exp_number(update_user_form.exp_number.data)
        user.set_remarks(update_user_form.remarks.data)
        db['Users'] = users_dict
        db.close()
        return redirect(url_for('retrieve_users'))
    else:
        users_dict = {}
        db = shelve.open('user.db', 'r')
        users_dict = db['Users']
        db.close()
        user = users_dict.get(id)
        update_user_form.first_name.data = user.get_first_name()
        update_user_form.last_name.data = user.get_last_name()
        update_user_form.gender.data = user.get_gender()
        update_user_form.email.data = user.get_email()
        update_user_form.birthday.data = user.get_birthday()
        update_user_form.address.data = user.get_address()
        update_user_form.payment_method.data = user.get_payment_method()
        update_user_form.credit_number.data = user.get_credit_number()
        update_user_form.exp_number.data = user.get_exp_number()
        update_user_form.remarks.data = user.get_remarks()
        return render_template('updateUser.html', form=update_user_form)
@app.route('/deleteUser/<int:id>', methods=['POST'])
def delete_user(id):
    users_dict = {}
    db = shelve.open('user.db', 'w')
    users_dict = db['Users']
    users_dict.pop(id)
    db['Users'] = users_dict
    db.close()
    return redirect(url_for('retrieve_users'))

@app.route('/deleteOrder/<int:id>', methods=['POST'])
def delete_order(id):
    orders_dict = {}
    db = shelve.open('order.db', 'w')
    orders_dict = db['Orders']
    orders_dict.pop(id)
    db['Orders'] = orders_dict
    db.close()
@app.route('/payment')
def payment():
    return App.render(render_template('Payment.html'))
if __name__ == '__main__':
    app.run(debug=True)
