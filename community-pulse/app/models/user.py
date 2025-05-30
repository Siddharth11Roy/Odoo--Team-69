from .. import db

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(80),unique=True,nullable=False)
    email=db.Column(db.String(120),unique=True,nullable=False)
    phone=db.Column(db.String(20),unique=True,nullable=False)
    password=db.Column(db.String(120),nullable=False)
    is_verified=db.Column(db.Boolean,default=False)
    is_admin=db.Column(db.Boolean,default=False)
    
    
    events=db.relationship("Event",backref="user")
    interests = db.relationship("Interest", backref="user", lazy=True)
    
    def __repr__(self):
        return f"<User {self.username}>"

