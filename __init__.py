from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session, g
from Forms import CreateUserForm, CreateCustomerForm, CreateLaylaForm, CreateAyatoForm, CreateBeidouForm
import shelve, User, Customer, log, Cart
import jyserver.Flask as jsf
import ctypes

app = Flask(__name__)
app.secret_key = 'yippee'
@app.route('/home')
def home():
    welcome_mes = "Guest Login"
    try:
        user_dict = {}
        db = shelve.open('user.db', 'r')
        user_dict = db['Users']

        for key in user_dict:
            curr_user = user_dict[key]
            if curr_user.get_curr() == 1:
                welcome_mes = "Welcome Back, " + curr_user.get_first_name()
                break

        db.close()
        return render_template('home.html', welcome_mes=welcome_mes)

    except FileNotFoundError:
        welcome_mes = 'File not found'

    except PermissionError:
        welcome_mes = 'Permisson error'

    except KeyError:
        welcome_mes = 'Key Error'

    except AttributeError:
        welcome_mes = 'Attribute Error'

    except TypeError:
        welcome_mes = 'Type Error'

    except EOFError:
        welcome_mes = 'End of File error'

    except:
        welcome_mes = "Other error"

    return render_template('home.html', welcome_mes=welcome_mes)

@app.route('/')
def fhome():
    welcome_mes = "Guest Login"
    try:
        user_dict = {}
        db = shelve.open('user.db', 'r')
        user_dict = db['Users']

        for key in user_dict:
            curr_user = user_dict[key]
            if curr_user.get_curr() == 1:
                welcome_mes = "Welcome Back, " + curr_user.get_first_name()
                break

        db.close()
        return render_template('home.html', welcome_mes=welcome_mes)

    except FileNotFoundError:
        welcome_mes = 'File not found'

    except PermissionError:
        welcome_mes = 'Permisson error'

    except KeyError:
        welcome_mes = 'Key Error'

    except AttributeError:
        welcome_mes = 'Attribute Error'

    except TypeError:
        welcome_mes = 'Type Error'

    except EOFError:
        welcome_mes = 'End of File error'

    except:
        welcome_mes = "Other error"

    return render_template('home.html', welcome_mes=welcome_mes)

@app.route('/loginUser', methods=['GET', 'POST'])
def login():
    error_message = ""

    if request.method == 'POST':
        users_dict = {}
        db = shelve.open('user.db', 'w')
        users_dict = db['Users']


        email = request.form['email']
        password = request.form['password']
        for key in users_dict:
            user = users_dict[key]
            if email == user.get_email():

                if password == user.get_password():

                    flash("Password accepted")

                    user.set_curr(1)
                    users_dict[key] = user
                    db['Users'] = users_dict
                    db.close()

                    return redirect('/home')
                else:
                    error_message = "Incorrect password"
            else:
                error_message = "Invalid email"
    return render_template('loginuser.html', error_message=error_message)


@app.route('/retrieveGuest', methods=['GET', 'POST'])
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
    return render_template('cart.html')





@app.route('/extraSlum', methods=['GET', 'POST'])
def layla():
    create_l_form = CreateLaylaForm(request.form)
    if request.method == 'POST':
        carts_dict = {}
        db = shelve.open('cart.db', 'c')
        try:
            carts_dict = db['Carts']
        except:
            print("Error in retrieving Carts from cart.db.")
        cart = Customer.Cart(create_l_form.esp, create_l_form.esq)
        carts_dict[cart.get_cart_id()] = cart
        db['Carts'] = carts_dict
        db.close()
        if request.form.get('act1') == 'Add ES':
            carts_dict = {}
            db = shelve.open('cart.db', 'r')
            carts_dict = db['Carts']
            db.close()
            carts_list = []
            for key in carts_dict:
                cart = carts_dict.get(key)
                if len(carts_list) > 0:
                    carts_list.pop(0)
                carts_list.insert(0, cart)
            print('layla')
            return render_template('cart.html', carts_list=carts_list)
        elif request.form.get('clr1') == 'Remove ES':
            carts_dict = {}
            db = shelve.open('cart.db', 'w')
            carts_dict = db['Carts']
            carts_dict[cart.decrease()] = cart
            db['Carts'] = carts_dict
            carts_list = []
            for key in carts_dict:
                cart = carts_dict.get(key)
                if len(carts_list) > 0:
                    carts_list.remove(cart[0])
            db.close()
            print('clear layla')
            return render_template('cart.html', carts_list=carts_list)
    return render_template('createCustomer.html', form=create_l_form)


@app.route('/sweetDreams', methods=['GET', 'POST'])
def xiao():
    create_customer_form = CreateCustomerForm(request.form)
    if request.method == 'POST':
        cbrts_dict = {}
        db = shelve.open('cbrt.db', 'c')
        try:
            cbrts_dict = db['Cbrts']
        except:
            print("Error in retrieving Cbrts from cbrt.db.")
        cbrt = Customer.Cbrt(create_customer_form.sdp, create_customer_form.sdq)
        cbrts_dict[cbrt.get_cbrt_id()] = cbrt
        db['Cbrts'] = cbrts_dict
        db.close()
        if request.form.get('sd') == 'Add SD':
            cbrts_dict = {}
            db = shelve.open('cbrt.db', 'r')
            cbrts_dict = db['Cbrts']
            db.close()
            cbrts_list = []
            for key in cbrts_dict:
                cbrt = cbrts_dict.get(key)
                if len(cbrts_list) > 0:
                    cbrts_list.pop(0)
                cbrts_list.insert(0, cbrt)
            print('xiao')
            return render_template('cart.html', cbrts_list=cbrts_list)
    return render_template('createCustomer.html', form=create_customer_form)


@app.route('/kamisatoClan', methods=['GET', 'POST'])
def ayato():
    create_a_form = CreateAyatoForm(request.form)
    if request.method == 'POST':
        ccrts_dict = {}
        db = shelve.open('ccrt.db', 'c')
        try:
            ccrts_dict = db['Ccrts']
        except:
            print("Error in retrieving Ccrts from ccrt.db.")
        ccrt = Customer.Ccrt(create_a_form.qep, create_a_form.qeq)
        ccrts_dict[ccrt.get_ccrt_id()] = ccrt
        db['Ccrts'] = ccrts_dict
        db.close()
        if request.form.get('qe') == 'Add QE':
            ccrts_dict = {}
            db = shelve.open('ccrt.db', 'r')
            ccrts_dict = db['Ccrts']
            db.close()
            ccrts_list = []
            for key in ccrts_dict:
                ccrt = ccrts_dict.get(key)
                if len(ccrts_list) > 0:
                    ccrts_list.pop(0)
                ccrts_list.insert(0, ccrt)
            print('ayato')
            return render_template('cart.html', ccrts_list=ccrts_list)
    return render_template('createCustomer.html', form=create_a_form)


@app.route('/ningGuang', methods=['GET', 'POST'])
def beidou():
    create_b_form = CreateBeidouForm(request.form)
    if request.method == 'POST':
        cdrts_dict = {}
        db = shelve.open('cdrt.db', 'c')
        try:
            cdrts_dict = db['Cdrts']
        except:
            print("Error in retrieving Cdrts from cdrt.db.")
        cdrt = Customer.Cdrt(create_b_form.bdp, create_b_form.bdq)
        cdrts_dict[cdrt.get_cdrt_id()] = cdrt
        db['Cdrts'] = cdrts_dict
        db.close()
        if request.form.get('bd') == 'Add BD':
            cdrts_dict = {}
            db = shelve.open('cdrt.db', 'r')
            cdrts_dict = db['Cdrts']
            db.close()
            cdrts_list = []
            for key in cdrts_dict:
                cdrt = cdrts_dict.get(key)
                if len(cdrts_list) > 0:
                    cdrts_list.pop(0)
                cdrts_list.insert(0, cdrt)
            print('i love beidou :>')
            return render_template('cart.html', cdrts_list=cdrts_list)
    return render_template('createCustomer.html', form=create_b_form)


@app.route('/createCustomer', methods=['GET', 'POST'])
def menu():
    return render_template('createCustomer.html')


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
        user = User.User(create_user_form.first_name.data, create_user_form.last_name.data,
                         create_user_form.gender.data, create_user_form.email.data, create_user_form.password.data,
                         create_user_form.birthday.data, create_user_form.address.data,
                         create_user_form.payment_method.data, create_user_form.credit_number.data,
                         create_user_form.exp_number.data, create_user_form.remarks.data, create_user_form.cvc.data)
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


if __name__ == '__main__':
    app.run()
