from mongoengine import *
import datetime
from mongoengine.queryset import QuerySet
from mongoengine.errors import DoesNotExist

class Registration(Document):
    firstname = StringField(max_length=100)
    lastname = StringField(max_length=100)
    contactno = StringField(max_length=12)
    username = StringField(max_length=50,unique=True)
    email = StringField(max_length=50)
    password = StringField(max_length=20)
    created_date = DateTimeField()
    modified_date = DateTimeField()
    user_id = IntField()

    def save(self, *args, **kwargs):
        if not self.created_date:
           self.created_date = datetime.datetime.now()
           self.modified_date = datetime.datetime.now()
        self.modified_date = datetime.datetime.now()
        return super(Registration, self).save(*args,**kwargs)

    def __str__(self):
        return self.username

class BlogDetails(Document):
    author = ReferenceField('Registration')
    title = StringField(SSrequired=True)
    shortdescription = StringField()
    longdescription = StringField()
    image = StringField()
    created_date = DateTimeField()
    modified_date = DateTimeField()
    published_date = DateTimeField()

    def save(self, *args, **kwargs):
        if not self.created_date:
           self.created_date = datetime.datetime.now()
           self.modified_date = datetime.datetime.now()
        self.modified_date = datetime.datetime.now()
        return super(BlogDetails, self).save(*args,**kwargs)
    
    def __str__(self):
        return self.title


