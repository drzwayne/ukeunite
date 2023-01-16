from wtforms import Form, StringField, RadioField, SelectField, TextAreaField, validators
from wtforms.fields import EmailField, DateField
class CreateUserForm(Form):
    first_name = StringField('First Name',[validators.Length(min=1, max=150),validators.DataRequired()])
    last_name = StringField('Last Name',[validators.Length(min=1, max=150),validators.DataRequired()])
    gender = SelectField('Gender',[validators.DataRequired()], choices=[('','Select'),('F','Female'),('M','Male')], default='')
    email = EmailField('Email',[validators.DataRequired()])
    birthday = DateField('Birthday',format='%Y-%m-%d')
    address = TextAreaField('Delivery Address',[validators.Length(max=200),validators.DataRequired()])
    payment_method = SelectField('Payment Method',[validators.DataRequired()], choices=[('','Select'),('V','Visa'),('MC','Mastercard')], default='')
    credit_number = StringField('Credit Card Number',[validators.Length(min=12, max=12),validators.DataRequired()])
    exp_number = StringField('Expiry',[validators.Length(min=4, max=4),validators.DataRequired()])
    remarks = TextAreaField('Remarks',[validators.Optional()])

class CreateGuestForm(Form):
    first_name = StringField('First Name',[validators.Length(min=1, max=150),validators.DataRequired()])
    address = TextAreaField('Delivery Address',[validators.Length(max=200),validators.DataRequired()])
    payment_method = SelectField('Payment Method',[validators.DataRequired()], choices=[('','Select'),('V','Visa'),('MC','Mastercard')], default='')
    credit_number = StringField('Credit Card Number',[validators.Length(min=12, max=12),validators.DataRequired()])
    exp_number = StringField('Expiry',[validators.Length(min=3, max=3),validators.DataRequired()])
    remarks = TextAreaField('Remarks',[validators.Optional()])
