from flask import Flask
from flask_restx import Api
from models import Recipe,User
from exts import db
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from recipes import recipe_ns
from auth import auth_ns
from flask_cors import CORS

def create_app(config):       #allows creating app instances with different configurations(dev,test,prod)
    
    app=Flask(__name__)       #create a new flask appliction instance
    app.config.from_object(config)    #loads configuration from the config class you pass in
    
    
    CORS(app)                   #allows react frontend communicate with flask backend
    
    db.init_app(app)           #connects SQLAlchemy database to flask app
    
    migrate=Migrate(app,db)    #Tracks database schema changes and generates migration scripts
    JWTManager(app)            #enables token-based authentication for the API
    
    api=Api(app,doc='/docs')
    
    api.add_namespace(recipe_ns)
    api.add_namespace(auth_ns)
    #model (serializer)
 

    
    @app.shell_context_processor
    def make_shell_context():
        return{
            "db":db,
            "Recipe":Recipe,
            "User":User
        }

    return app