from src import db


#Classes
class User(db.Model):
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(100),nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    active = db.Column(db.Boolean)

    def __init__(self, code, first_name, last_name, email, password, active):
        self.code = code
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.active = active

    # Create a String
    def __repr__(self):
        return '<User {}>'.format(self.email)


# Functions
# Insert record
def insert(_code, _first_name, _last_name, _email, _password, _active):
    try:      
        if _active == 'on':
            _active2 = 1
        else:
            _active2 = 0

        userNew = User(_code, _first_name, _last_name, _email, _password, _active2)
        db.session.add(userNew)
        db.session.commit()
    except:
        print("*** ERROR EXCEPT ***")
        db.session.rollback()
    finally:
        print("*** FINALLY ***")
        db.session.close()

# Get All records
def getAll():
    users = User.query.all()

    return users

# Get One record by Code
def getOne(code):
    user = User.query.filter_by(code = code)
    return user
        