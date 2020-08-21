from flask import Flask
import sys
from flask_restful import Api
from api.routes import initialize_routes
from flask_cors import CORS
import config.configDB
from flask_graphql import GraphQLView
from schema.index import schema

app = Flask(__name__)


cors = CORS(app)
api  = Api(app)
initialize_routes(api)


app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')