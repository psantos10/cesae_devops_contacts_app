from app import db

class Contact(db.Model):
    __tablename__ = 'contacts'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False)
    phone = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'Contact<name:{self.name}, email:{self.email}, phone:{self.phone}>'

