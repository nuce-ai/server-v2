# flask_graphene_mongo/database.py
from mongoengine import connect

# You can connect to a real mongo server instance by your own.
connect(
        db = 'alook',
        host = 'mongodb+srv://alook:alook12345678@object-information.i7udl.mongodb.net/alook?retryWrites=true&w=majority'
)




    