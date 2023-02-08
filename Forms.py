from wtforms import Form, StringField, RadioField, SelectField, TextAreaField, validators
from wtforms.fields import EmailField, DateField,TelField, IntegerField
class CreateUserForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    gender = SelectField('Gender', [validators.DataRequired()],choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')], default='')
    email = EmailField('Email', [validators.DataRequired()])
    birthday = DateField('Birthday', format='%Y-%m-%d')
    address = TextAreaField('Delivery Address', [validators.Length(max=200), validators.DataRequired()])
    payment_method = SelectField('Payment Method', [validators.DataRequired()],choices=[('', 'Select'), ('V', 'Visa'), ('MC', 'Mastercard')], default='')
    credit_number = StringField('Credit Card Number', [validators.Regexp('^[0-9]*$', message='only numbers are allowed'), validators.Length(min=12, max=12), validators.DataRequired()])
    cvc = TelField('CVC', [validators.Length(min=3, max=3), validators.DataRequired()])
    exp_number = TelField('Expiry', [validators.Length(min=4, max=4), validators.DataRequired()])
    remarks = TextAreaField('Remarks', [validators.Optional()])
    password = StringField('Password', [validators.Length(min=5, max=10), validators.DataRequired()])
class CreateCustomerForm(Form):
    fi = ['es','sd','qe','fff']
    fn = ['Extravagant Slumber', 'Sweet Dreams', 'Quiet Elegance', 'Flash-Fried-Fillet']
    fp = [18.5, 11.5, 37, 7.4]
    fq = [1, 1, 1, 1]
    esp = 18.50
    esq = 0
    sdp = 11.50
    sdq = 1
    qep = 37.00
    qeq = 1
    bdp = 7.40
    bdq = 1
class CreateMemberForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    gender = SelectField('Gender', [validators.DataRequired()],
                         choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')], default='')
    email = EmailField('Email', [validators.DataRequired()])
    birthday = DateField('Birthday', format='%Y-%m-%d')
    address = TextAreaField('Delivery Address', [validators.Length(max=200), validators.DataRequired()])
    payment_method = SelectField('Payment Method', [validators.DataRequired()],
                                 choices=[('', 'Select'), ('V', 'Visa'), ('MC', 'Mastercard')], default='')
    credit_number = StringField('Credit Card Number', [validators.Length(min=12, max=12), validators.DataRequired()])
    exp_number = StringField('Expiry', [validators.Length(min=4, max=4), validators.DataRequired()])
    remarks = TextAreaField('Remarks', [validators.Optional()])


class CreateGuestForm(Form):
    address = TextAreaField('Delivery Address', [validators.Length(max=200), validators.DataRequired()])
    payment_method = SelectField('Payment Method', [validators.DataRequired()],
                                 choices=[('', 'Select'), ('V', 'Visa'), ('MC', 'Mastercard')], default='')
    credit_number = StringField('Credit Card Number', [validators.Length(min=12, max=12), validators.DataRequired()])
    exp_number = StringField('Expiry', [validators.Length(min=3, max=3), validators.DataRequired()])
    remarks = TextAreaField('Remarks', [validators.Optional()])

class CreateLoginForm(Form):
    loginemail = EmailField('Email Address', [validators.DataRequired()])
    loginpassword = StringField('Password', [validators.Length(min=5, max=10), validators.DataRequired()])

