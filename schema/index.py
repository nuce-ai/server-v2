import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from models.index import ObjectInformation as ObjectInformationModel


class ObjectInformation(MongoengineObjectType):
    class Meta:
        model = ObjectInformationModel
        interfaces = (Node,)

class Query(graphene.ObjectType):
    all_object_information = MongoengineConnectionField(ObjectInformation)

    

schema = graphene.Schema(query=Query, types=[ObjectInformation])