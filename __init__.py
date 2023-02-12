from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session, g
from Forms import CreateUserForm, CreateCustomerForm, CreateLaylaForm, CreateAyatoForm, CreateBeidouForm, CreateXiaoForm
import shelve, User, Customer, log, Cart
import jyserver.Flask as jsf
import math
import os
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

@app.route('/payment')
def paymentpage():
    carts_dict = {}
    db = shelve.open('cart.db', 'r')
    carts_dict = db['Carts']
    db.close()
    carts_list = []
    for key in carts_dict:
        cart = carts_dict.get(key)
        if len(carts_list) >0 :
            carts_list.pop(0)
        carts_list.insert(0,cart)
    cbrts_dict = {}
    db = shelve.open('cbrt.db', 'r')
    cbrts_dict = db['Cbrts']
    db.close()
    cbrts_list = []
    for key in cbrts_dict:
        cbrt = cbrts_dict.get(key)
        if len(cbrts_list) >0 :
            cbrts_list.pop(0)
        cbrts_list.insert(0,cbrt)
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
    print('fail')
    total_dict = {}
    db = shelve.open('total.db','r')
    total_dict = db['Total']
    total_list = []
    for key in total_dict:
        total = total_dict.get(key)
        total_list.append(total)
    t2_dict = {}
    db = shelve.open('two.db','r')
    t2_dict = db['Two']
    t2_list = []
    for key in t2_dict:
        t2 = t2_dict.get(key)
        t2_list.append(t2)
    t3_dict = {}
    db = shelve.open('tree.db','r')
    t3_dict = db['Tree']
    t3_list = []
    for key in t3_dict:
        t3 = t3_dict.get(key)
        t3_list.append(t3)
    t4_dict = {}
    db = shelve.open('four.db','r')
    t4_dict = db['Four']
    t4_list = []
    for key in t4_dict:
        t4 = t4_dict.get(key)
        t4_list.append(t4)
    st = (math.fsum(total_list)+math.fsum(t2_list)+math.fsum(t3_list)+math.fsum(t4_list))
    subtotal_list = []
    subtotal_list.append(st)
    return render_template('payment.html', carts_list=carts_list, cbrts_list=cbrts_list, ccrts_list=ccrts_list, cdrts_list=cdrts_list, total_list=total_list, t2_list=t2_list, t3_list=t3_list, t4_list=t4_list, subtotal_list=subtotal_list)

@app.before_request
def bfr_rq():
    g.user = None
    if 'user' in session:
        g.user = session['user']

@jsf.use(app)
class App:
    def __init__(self):
        self.count1 = 0
    def increment(self):
        self.count1 += 1
        self.js.document.querySelector('.count1').value = self.count1


@app.route('/cart')
def cartpage():
    if request.form.get('act1') == 'Add ES':
        carts_dict = {}
        db = shelve.open('cart.db', 'r')
        carts_dict = db['Carts']
        db.close()
        carts_list = []
        for key in carts_dict:
            cart = carts_dict.get(key)
            if len(carts_list) >0 :
                carts_list.pop(0)
            carts_list.insert(0,cart)
        print('1')
        return render_template('cart.html', carts_list=carts_list)
    elif request.form.get('clr1') == 'Remove ES':
        carts_dict = {}
        db = shelve.open('cart.db', 'r')
        carts_dict = db['Carts']
        db.close()
        carts_list = []
        for key in carts_dict:
            cart = carts_dict.get(key)
            if len(carts_list) >0:
                carts_list.pop(0)
            carts_list.insert(0,cart)
        print('cartd1')
        return render_template('cart.html', carts_list=carts_list)
    elif request.form.get('sd') == 'Add SD':
        cbrts_dict = {}
        db = shelve.open('cbrt.db', 'r')
        cbrts_dict = db['Cbrts']
        db.close()
        cbrts_list = []
        for key in cbrts_dict:
            cbrt = cbrts_dict.get(key)
            if len(cbrts_list) >0 :
                cbrts_list.pop(0)
            cbrts_list.insert(0,cbrt)
        print('2')
        return render_template('cart.html',cbrts_list=cbrts_list)
    elif request.form.get('qe') == 'Add QE':
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
        print('3')
        return render_template('cart.html',ccrts_list=ccrts_list)
    elif request.form.get('bd') == 'Add BD':
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
    else:
        carts_dict = {}
        db = shelve.open('cart.db', 'r')
        carts_dict = db['Carts']
        db.close()
        carts_list = []
        for key in carts_dict:
            cart = carts_dict.get(key)
            if len(carts_list) >0 :
                carts_list.pop(0)
            carts_list.insert(0,cart)
        cbrts_dict = {}
        db = shelve.open('cbrt.db', 'r')
        cbrts_dict = db['Cbrts']
        db.close()
        cbrts_list = []
        for key in cbrts_dict:
            cbrt = cbrts_dict.get(key)
            if len(cbrts_list) >0 :
                cbrts_list.pop(0)
            cbrts_list.insert(0,cbrt)
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
        print('fail')
        users_dict = {}
        db = shelve.open('user.db', 'r')
        users_dict = db['Users']
        db.close()
        users_list = []
        for key in users_dict:
            user = users_dict.get(key)
            users_list.append(user)
        print('user success')
        total_dict = {}
        db = shelve.open('total.db','r')
        total_dict = db['Total']
        total_list = []
        for key in total_dict:
            total = total_dict.get(key)
            total_list.append(total)
        t2_dict = {}
        db = shelve.open('two.db','r')
        t2_dict = db['Two']
        t2_list = []
        for key in t2_dict:
            t2 = t2_dict.get(key)
            t2_list.append(t2)
        t3_dict = {}
        db = shelve.open('tree.db','r')
        t3_dict = db['Tree']
        t3_list = []
        for key in t3_dict:
            t3 = t3_dict.get(key)
            t3_list.append(t3)
        t4_dict = {}
        db = shelve.open('four.db','r')
        t4_dict = db['Four']
        t4_list = []
        for key in t4_dict:
            t4 = t4_dict.get(key)
            t4_list.append(t4)
        st = (math.fsum(total_list)+math.fsum(t2_list)+math.fsum(t3_list)+math.fsum(t4_list))
        subtotal_list = []
        subtotal_list.append(st)
        return render_template('cart.html', carts_list=carts_list, cbrts_list=cbrts_list, ccrts_list=ccrts_list, cdrts_list=cdrts_list, users_list=users_list, total_list=total_list, t2_list=t2_list, t3_list=t3_list, t4_list=t4_list, subtotal_list=subtotal_list)

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
        cart.incqty()
        carts_dict[cart.get_cart_id()] = cart
        db['Carts'] = carts_dict
        db.close()
        total_dict = {}
        db = shelve.open('total.db', 'c')
        try:
            total_dict = db['Total']
        except:
            print("Error in retrieving Total from total.db.")
        total_dict = {'p1': 18.5 * cart.get_cart_id()}
        db['Total'] = total_dict
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
            total_dict = {}
            db = shelve.open('total.db','r')
            total_dict = db['Total']
            total_list = []
            for key in total_dict:
                total = total_dict.get(key)
                total_list.append(total)
                print('es:',total)
            print('es:',math.fsum(total_list))
            return render_template('menu.html', carts_list=carts_list, total_list=total_list)
        elif request.form.get('clr1') == 'Clear ES':
            os.remove('cart.db.bak')
            os.remove('cart.db.dat')
            os.remove('cart.db.dir')
            carts_dict = {}
            db = shelve.open('cart.db', 'c')
            try:
                carts_dict = db['Carts']
            except:
                print("Error in retrieving Carts from cart.db.")
            cart = Customer.Cart(create_l_form.esp, create_l_form.esq)
            cart.decqty()
            carts_dict[cart.get_cart_id()] = cart
            db['Carts'] = carts_dict
            db.close()
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
            print('clear layla')
            os.remove('total.db.bak')
            os.remove('total.db.dat')
            os.remove('total.db.dir')
            total_dict = {}
            db = shelve.open('total.db', 'c')
            try:
                total_dict = db['Total']
            except:
                print("Error in retrieving Total from total.db.")
            total_dict = {'p1': 18.5 * cart.get_cart_id()}
            db['Total'] = total_dict
            db.close()
            total_dict = {}
            db = shelve.open('total.db','r')
            total_dict = db['Total']
            total_list = []
            for key in total_dict:
                total = total_dict.get(key)
                total_list.append(total)
                print('removees:',total)
            print('res:',math.fsum(total_list))
            return render_template('menu.html', carts_list=carts_list, total_list=total_list)
    return render_template('menu.html', form=create_l_form)


@app.route('/sweetDreams', methods=['GET', 'POST'])
def xiao():
    create_x_form = CreateXiaoForm(request.form)
    if request.method == 'POST':
        cbrts_dict = {}
        db = shelve.open('cbrt.db', 'c')
        try:
            cbrts_dict = db['Cbrts']
        except:
            print("Error in retrieving Cbrts from cbrt.db.")
        cbrt = Customer.Cbrt(create_x_form.sdp, create_x_form.sdq)
        cbrt.incqtyb()
        cbrts_dict[cbrt.get_cbrt_id()] = cbrt
        db['Cbrts'] = cbrts_dict
        db.close()
        t2_dict = {}
        db = shelve.open('two.db', 'c')
        try:
            t2_dict = db['Two']
        except:
            print("Error in retrieving T2 from two.db.")
        t2_dict = {'p2':11.5 * cbrt.get_cbrt_id()}
        db['Two'] = t2_dict
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
            t2_dict = {}
            db = shelve.open('two.db','r')
            t2_dict = db['Two']
            t2_list = []
            for key in t2_dict:
                t2 = t2_dict.get(key)
                t2_list.append(t2)
            return render_template('menu.html', cbrts_list=cbrts_list, t2_list=t2_list)
        elif request.form.get('clr2') == 'Clear SD':
            os.remove('cbrt.db.bak')
            os.remove('cbrt.db.dat')
            os.remove('cbrt.db.dir')
            cbrts_dict = {}
            db = shelve.open('cbrt.db', 'c')
            try:
                cbrts_dict = db['Cbrts']
            except:
                print("Error in retrieving Cbrts from cbrt.db.")
            cbrt = Customer.Cbrt(create_x_form.sdp, create_x_form.sdq)
            cbrt.decqtyb()
            cbrts_dict[cbrt.get_cbrt_id()] = cbrt
            db['Cbrts'] = cbrts_dict
            db.close()
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
            os.remove('two.db.bak')
            os.remove('two.db.dat')
            os.remove('two.db.dir')
            t2_dict = {}
            db = shelve.open('two.db', 'c')
            try:
                t2_dict = db['Two']
            except:
                print("Error in retrieving T2 from two.db.")
            t2_dict = {'p2':11.5 * cbrt.get_cbrt_id()}
            db['Two'] = t2_dict
            db.close()
            t2_dict = {}
            db = shelve.open('two.db','r')
            t2_dict = db['Two']
            t2_list = []
            for key in t2_dict:
                t2 = t2_dict.get(key)
                t2_list.append(t2)
            return render_template('menu.html', cbrts_list=cbrts_list, t2_list=t2_list)
    return render_template('menu.html', form=create_x_form)

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
        ccrt.incqtyc()
        ccrts_dict[ccrt.get_ccrt_id()] = ccrt
        db['Ccrts'] = ccrts_dict
        db.close()
        t3_dict = {}
        db = shelve.open('tree.db', 'c')
        try:
            t3_dict = db['Tree']
        except:
            print("Error in retrieving T3 from tree.db.")
        t3_dict = {'p3':37 * ccrt.get_ccrt_id()}
        db['Tree'] = t3_dict
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
            t3_dict = {}
            db = shelve.open('tree.db','r')
            t3_dict = db['Tree']
            t3_list = []
            for key in t3_dict:
                t3 = t3_dict.get(key)
                t3_list.append(t3)
            return render_template('menu.html', ccrts_list=ccrts_list, t3_list=t3_list)
        elif request.form.get('clr3') == 'Clear QE':
            os.remove('ccrt.db.bak')
            os.remove('ccrt.db.dat')
            os.remove('ccrt.db.dir')
            ccrts_dict = {}
            db = shelve.open('ccrt.db', 'c')
            try:
                ccrts_dict = db['Ccrts']
            except:
                print("Error in retrieving Ccrts from ccrt.db.")
            ccrt = Customer.Ccrt(create_a_form.qep, create_a_form.qeq)
            ccrt.decqtyc()
            ccrts_dict[ccrt.get_ccrt_id()] = ccrt
            db['Ccrts'] = ccrts_dict
            db.close()
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
            os.remove('tree.db.bak')
            os.remove('tree.db.dat')
            os.remove('tree.db.dir')
            t3_dict = {}
            db = shelve.open('tree.db', 'c')
            try:
                t3_dict = db['Tree']
            except:
                print("Error in retrieving T3 from tree.db.")
            t3_dict = {'p3':37 * ccrt.get_ccrt_id()}
            db['Tree'] = t3_dict
            db.close()
            t3_dict = {}
            db = shelve.open('tree.db','r')
            t3_dict = db['Tree']
            t3_list = []
            for key in t3_dict:
                t3 = t3_dict.get(key)
                t3_list.append(t3)
            return render_template('menu.html', ccrts_list=ccrts_list, t3_list=t3_list)
    return render_template('menu.html', form=create_a_form)


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
        cdrt.incqtyd()
        cdrts_dict[cdrt.get_cdrt_id()] = cdrt
        db['Cdrts'] = cdrts_dict
        db.close()
        t4_dict = {}
        db = shelve.open('four.db', 'c')
        try:
            t4_dict = db['Four']
        except:
            print("Error in retrieving T4 from four.db.")
        t4_dict = {'p4':7.4 * cdrt.get_cdrt_id()}
        db['Four'] = t4_dict
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
            t4_dict = {}
            db = shelve.open('four.db','r')
            t4_dict = db['Four']
            t4_list = []
            for key in t4_dict:
                t4 = t4_dict.get(key)
                t4_list.append(t4)
            return render_template('menu.html', cdrts_list=cdrts_list, t4_list=t4_list)
        elif request.form.get('clr4') == 'Clear BD':
            os.remove('cdrt.db.bak')
            os.remove('cdrt.db.dat')
            os.remove('cdrt.db.dir')
            cdrts_dict = {}
            db = shelve.open('cdrt.db', 'c')
            try:
                cdrts_dict = db['Cdrts']
            except:
                print("Error in retrieving Cdrts from cdrt.db.")
            cdrt = Customer.Cdrt(create_b_form.bdp, create_b_form.bdq)
            cdrt.decqtyd()
            cdrts_dict[cdrt.get_cdrt_id()] = cdrt
            db['Cdrts'] = cdrts_dict
            db.close()
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
            os.remove('four.db.bak')
            os.remove('four.db.dat')
            os.remove('four.db.dir')
            t4_dict = {}
            db = shelve.open('four.db', 'c')
            try:
                t4_dict = db['Four']
            except:
                print("Error in retrieving T4 from four.db.")
            t4_dict = {'p4':7.4 * cdrt.get_cdrt_id()}
            db['Four'] = t4_dict
            db.close()
            t4_dict = {}
            db = shelve.open('four.db','r')
            t4_dict = db['Four']
            t4_list = []
            for key in t4_dict:
                t4 = t4_dict.get(key)
                t4_list.append(t4)
            return render_template('menu.html', cdrts_list=cdrts_list, t4_list=t4_list)
    return render_template('menu.html', form=create_b_form)
@app.route('/menu',methods=['GET','POST'])
def menupage():
    return render_template('menu.html')

@app.route('/add', methods=['POST'])
def addcart():
    try:
        _quantity = int(request.form['quantity'])
        _code = request.form['code']
        # validate the received values
        if _quantity and _code and request.method == 'POST':

            itemArray = { Customer.Roytut['code'] : {'name' : Customer.Roytut['name'], 'quantity' : _quantity, 'price' : Customer.Roytut['price'], 'image' : Customer.Roytut['image'], 'total_price': _quantity * Customer.Roytut['price']}}

            all_total_price = 0
            all_total_quantity = 0

            session.modified = True
            if 'cart_item' in session:
                if Customer.Roytut['code'] in session['cart_item']:
                    for key, value in session['cart_item'].items():
                        if Customer.Roytut['code'] == key:
                            old_quantity = session['cart_item'][key]['quantity']
                            total_quantity = old_quantity + _quantity
                            session['cart_item'][key]['quantity'] = total_quantity
                            session['cart_item'][key]['total_price'] = total_quantity * Customer.Roytut['price']
                else:
                    session['cart_item'] = array_merge(session['cart_item'], itemArray)
                for key, value in session['cart_item'].items():
                    individual_quantity = int(session['cart_item'][key]['quantity'])
                    individual_price = float(session['cart_item'][key]['total_price'])
                    all_total_quantity = all_total_quantity + individual_quantity
                    all_total_price = all_total_price + individual_price
            else:
                session['cart_item'] = itemArray
                all_total_quantity = all_total_quantity + _quantity
                all_total_price = all_total_price + _quantity * Customer.Roytut['price']
            session['all_total_quantity'] = all_total_quantity
            session['all_total_price'] = all_total_price
            return redirect(url_for('cart'))
        else:
            print('Error while adding item to cart')
    except Exception as e:
        print(e)
    return render_template('menu.html')

@app.route('/empty')
def empty_cart():
    try:
        session.clear()
        return redirect(url_for('menu'))
    except Exception as e:
        print(e)

@app.route('/delete/<string:code>')
def delete_product(code):
    try:
        all_total_price = 0
        all_total_quantity = 0
        session.modified = True
        for item in session['cart_item'].items():
            if item[0] == code:
                session['cart_item'].pop(item[0], None)
                if 'cart_item' in session:
                    for key, value in session['cart_item'].items():
                        individual_quantity = int(session['cart_item'][key]['quantity'])
                        individual_price = float(session['cart_item'][key]['total_price'])
                        all_total_quantity = all_total_quantity + individual_quantity
                        all_total_price = all_total_price + individual_price
                        break
        if all_total_quantity == 0:
            session.clear()
        else:
            session['all_total_quantity'] = all_total_quantity
            session['all_total_price'] = all_total_price
        return redirect(url_for('menu'))
    except Exception as e:
        print(e)
def array_merge( first_array , second_array ):
    if isinstance( first_array , list ) and isinstance( second_array , list ):
        return first_array + second_array
    elif isinstance( first_array , dict ) and isinstance( second_array , dict ):
        return dict( list( first_array.items() ) + list( second_array.items() ) )
    elif isinstance( first_array , set ) and isinstance( second_array , set ):
        return first_array.union( second_array )
    return False

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
