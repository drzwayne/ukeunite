from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session,g
from Forms import CreateUserForm, CreateCustomerForm, CreateLoginForm
import shelve, User, Customer, log
import jyserver.Flask as jsf
app = Flask(__name__)
app.secret_key = 'yippee'
@app.route('/')

def home():
     if 'user' in session:
        return App.render(render_template("home.html", username=session['user']))
     else:
         return App.render(render_template('home.html'))
@app.route('/json')
def get_json():
    return jsonify('cart.html')
@app.route('/loginUser', methods=['GET', 'POST'])
def login():
    error_message = ""

    if request.method == 'POST':
        db = shelve.open('user.db')
        user_data = db['user']
        db.close()
        email = request.form['email']
        password = request.form['password']
        if email in user_data:

            if password == user_data[email][password]:

                session['user'] = email

                return render_template(url_for('home'))
            else:
                error_message = "Incorrect password"
        else:
            error_message = "Invalid email"
    return render_template('loginuser.html', error_message=error_message)



@app.route('/retrieveGuest', methods=['GET','POST'])
def logged():
    if g.user:
        return render_template('retrieveGuest.html', user=session['user'])
    return redirect(url_for('home'))

@app.before_request
def bfr_rq():
    g.user = None
    if 'user' in session:
        g.user = session['user']

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
        self.cart = 0
        self.total = 0
        self.total2 = 0
        self.total3 = 0
        self.total4 = 0
        self.c1 = self.escount
        self.cart = self.total
        escounts_dict = {}
        db = shelve.open('escount.db','c')
        try:
            escounts_dict = db['Escounts']
        except:
            print("Error in retrieving number of items from escount.db.")
        db['Escounts'] = escounts_dict
        db.close()
        escounts_dict = {}
        db = shelve.open('escount.db', 'r')
        escounts_dict = db['Escounts']
        db.close()
        escounts_list = []
        for key in escounts_dict:
            escount = escounts_dict.get(key)
            escounts_list.append(escount)
        self.b1 = []
        self.m1 = {'fn':'ES','price':18.50, 'qty':0}
    def esadd(self):
        self.escount += 1
        self.js.document.querySelector('.es').value = self.escount
        self.m1['qty'] = self.escount
        if self.escount >= 0:
            self.b1.pop(self.m1)
        self.b1.push(self.m1)
        self.js.document.querySelector('.cartQty').value= self.js.document.querySelector('.cartQty').value + 1
        ts_dict = {}
        db = shelve.open('t.db','c')
        try:
            ts_dict = db['Ts']
        except:
            print("Error in retrieving number of items from t.db.")
        ts_dict = self.total[self.m1]
        db['Ts'] = ts_dict
        db.close()
        self.js.document.querySelector('.tp1').value = (self.cart['qty']*18.5).toFixed(2)
        self.js.document.querySelector('.mtp').value = (self.js.document.querySelector('.mtp').value+18.5).toFixed(2)
    def get(self):
        self.cart = self.total
        ts_dict = {}
        db = shelve.open('t.db', 'r')
        ts_dict = db['Ts']
        db.close()
        ts_list = []
        for key in ts_dict:
            t = ts_dict.get(key)
            ts_list.append(t)
        self.js.document.querySelector('.tp1').value= (self.cart['qty']*18.5).toFixed(2)
        self.js.document.querySelector('.mtp').value= (self.js.document.querySelector('.mtp').value+self.cart['qty']*18.5).toFixed(2)

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
        db = shelve.open('qty.db', 'c')
        qtys_list = []
        for key in qtys_dict:
            qty = qtys_dict.get(key)
            qtys_list.append(qty)
        qtys_dict ={}
        db = shelve.open('qty.db','c')
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
        user = User.User(create_user_form.first_name.data, create_user_form.last_name.data, create_user_form.gender.data, create_user_form.email.data,create_user_form.password.data, create_user_form.birthday.data, create_user_form.address.data, create_user_form.payment_method.data, create_user_form.credit_number.data, create_user_form.exp_number.data, create_user_form.remarks.data,   create_user_form.cvc.data)
        users_dict[user.get_user_id()] = user
        db['Users'] = users_dict
        db.close()
        return redirect(url_for('retrieve_users'))
    return render_template('createUser.html', form=create_user_form)
@app.route('/createCustomer', methods=['GET', 'POST'])
def create_customer():
    create_customer_form = CreateCustomerForm(request.form)
    if request.method == 'POST' and create_customer_form.validate():
        customers_dict = {}
        db = shelve.open('customer.db', 'c')
        try:
            customers_dict = db['Customers']
        except:
            print("Error in retrieving Customers from customer.db.")
        customer = Customer.Customer(create_customer_form.first_name.data,create_customer_form.last_name.data, create_customer_form.gender.data, create_customer_form.membership.data, create_customer_form.remarks.data, create_customer_form.email.data, create_customer_form.date_joined.data, create_customer_form.address.data, create_customer_form.password.data)
        customers_dict[customer.get_user_id()] = customer
        db['Customers'] = customers_dict
        db.close()
        return redirect(url_for('retrieve_customers'))
    return render_template('createCustomer.html', form=create_customer_form)
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
@app.route('/retrieveCustomers')
def retrieve_customers():
    customers_dict = {}
    db = shelve.open('customer.db', 'r')
    customers_dict = db['Customers']
    db.close()
    customers_list = []
    for key in customers_dict:
        customer = customers_dict.get(key)
        customers_list.append(customer)
    return render_template('retrieveCustomers.html', count=len(customers_list), customers_list=customers_list)
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
if __name__ == '__main__':
    app.run()
