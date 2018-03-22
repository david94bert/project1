from . import db

class UserProfile(db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    gender=db.Column(db.String(6))
    email = db.Column(db.String(80))
    location = db.Column(db.String(80))
    bio=db.Column(db.String(255))
    image=db.Column(db.LargeBinary)
    created_on=db.Column(db.DateTime)
    
    def __init__(self, uid, firstname, lastname, gender, email, location, bio, image, created_on):
        self.uid=uid
        self.firstname=firstname
        self.lastname=lastname
        self.gender=gender
        self.email=email
        self.location=location
        self.bio=bio
        self.image=image
        self.created_on=created_on
        
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.uid)  # python 2 support
        except NameError:
            return str(self.uid)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)
