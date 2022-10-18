from .sqlalchemy_init import db


class Book(db.Model):

    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    author = db.Column(db.String)
    rating = db.Column(db.Integer)

    def __init__(self, title, author, rating):
        self.title = title
        self.author = author
        self.rating = rating

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "rating": self.rating,
        }