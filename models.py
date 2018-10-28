import pymodm
from pymodm import fields
from flask_login import UserMixin


class Compagnie(pymodm.MongoModel):
    description = fields.CharField()
    logo = fields.CharField()
    name = fields.CharField(primary_key=True)
    URL = fields.CharField()


class Houblonniere(Compagnie):
    pass


class Levurier(Compagnie):
    pass


class Malterie(Compagnie):
    pass


class User(pymodm.MongoModel, UserMixin):
    username = fields.CharField()
    password = fields.CharField()
