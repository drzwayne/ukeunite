import shelve

db = shelve.open('currentuser.db', 'r')
currentusers_dict = db['Users']
db.close()

for key in currentusers_dict:
    user = currentusers_dict[key]
    print("Email:", user.get_email())
    print("Password:", user.get_password())
