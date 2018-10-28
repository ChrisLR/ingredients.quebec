import pymodm
from pymodm import fields
from flask_user import UserMixin


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
    active = fields.BooleanField(default=True)
    username = fields.LineStringField()
    password = fields.LineStringField()
    first_name = fields.LineStringField(default='')
    last_name = fields.LineStringField(default='')
    # TODO Need to decide on a few usable roles and their permissions.
    # roles = db.ListField(db.StringField(), default=[])
