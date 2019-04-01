import mongoengine

class User(mongoengine.Document):
    fullname = mongoengine.StringField()
    birthdate = mongoengine.StringField()
    gender = mongoengine.StringField()
    timestamp = mongoengine.DateTimeField()