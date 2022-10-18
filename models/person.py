from .sqlalchemy_init import db

class Person(db.Model):

  __tablename__ = 'persons'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(), nullable=False)
  age = db.Column(db.Integer, nullable=False)

  def __repr__(self):
      return f'<Person {self.id}, {self.name}>'