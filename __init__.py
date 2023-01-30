from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session,g
from Forms import CreateUserForm, CreateCustomerForm
import shelve, User, Customer, log, Cart
import jyserver.Flask as jsf
import ctypes
app = Flask(__name__)
app.secret_key = 'yippee'


@app.route('/')
def home():
    try:
        current_user_db = shelve.open("currentuser.db", "r")
        current_user = current_user_db["user"]
        current_user_db.close()
        return render_template('home.html', current_user=current_user)
    except:
        current_user_db = shelve.open("currentuser.db", "c")
        current_user_db.close()

    return render_template('home.html')


@app.route('/loginUser', methods=['GET', 'POST'])
def login():
    error_message = ""

    if request.method == 'POST':
        users_dict = {}
        db = shelve.open('user.db', 'r')
        users_dict = db['Users']
        db.close()

        email = request.form['email']
        password = request.form['password']
        for key in users_dict:
            user = users_dict[key]
            if email == user.get_email():

                if password == user.get_password():


                    flash("Password accepted")

                    session['user'] = email
                    current_user_db = shelve.open("currentuser.db", "c")
                    current_user_db["user"] = user
                    current_user_db.close()



                    return render_template('home.html')
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
    carts_dict = {}
    db = shelve.open('cart.db', 'r')
    carts_dict = db['Carts']
    db.close()
    carts_list = []
    for key in carts_dict:
        cart = carts_dict.get(key)
        carts_list.append(cart)
    return render_template('cart.html', count=len(carts_list), carts_list=carts_list)
@jsf.use(app)
class App:
    def __init__(self):
        self.count = 0
    def increment(self):
        self.count += 1
        self.js.document.querySelector(".esc").innerHTML = self.count

@app.route('/createCustomer',methods=['GET','POST'])
def menu():
    create_customer_form = CreateCustomerForm(request.form)
    if request.method == 'POST':
        carts_dict = {}
        db = shelve.open('cart.db', 'c')
        try:
            carts_dict = db['Carts']
        except:
            print("Error in retrieving Carts from cart.db.")
        cart = Customer.Cart(create_customer_form.fi, create_customer_form.fn, create_customer_form.fp, create_customer_form.fq, create_customer_form.esp, create_customer_form.esq, create_customer_form.sdp, create_customer_form.sdq,create_customer_form.qep, create_customer_form.qeq, create_customer_form.bdp, create_customer_form.bdq)
        carts_dict[cart.get_cart_id()] = cart
        db['Carts'] = carts_dict
        db.close()
        return redirect(url_for('cart'))
    return render_template('createCustomer.html', form=create_customer_form)
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
if __name__ == '__main__':
    app.run()
