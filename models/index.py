from datetime import datetime
from mongoengine import Document
from mongoengine.fields import (
    DateTimeField, ReferenceField, StringField,IntField
)

# class Department(Document):
#     meta = {'collection': 'department'}
#     name = StringField()


# class Role(Document):
#     meta = {'collection': 'role'}
#     name = StringField()


# class Employee(Document):
#     meta = {'collection': 'employee'}
#     name = StringField()
#     hired_on = DateTimeField(default=datetime.now)
#     department = ReferenceField(Department)
#     role = ReferenceField(Role)

class ObjectInformation(Document):
    meta = {'collection': 'object_information'}
    id_ = IntField(required=True,unique=True)
    name = StringField()
    content = StringField()
    url_video = StringField()
    url_icon = StringField()
    sub_description = StringField()
