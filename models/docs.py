from extensions import db

class Doc(db.Model):
    __tablename__ = 'local_docs'

    slug = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)
    path = db.Column(db.String, nullable=False)
