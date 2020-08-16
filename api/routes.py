from controllers.ClassifierController import *

def initialize_routes(api):
    api.add_resource(ClassifierController,'/api/classifier/image')