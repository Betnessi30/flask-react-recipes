from decouple import config   #allows to read configuration values frrom the .env file
import os  #os provides fxns for interacting with Os, dirname gets directory name of path, real path gets absolute path of file
from os.path import dirname, realpath, join   #join combines path components intelligently
BASE_DIR = dirname(realpath(__file__))   #set the base directory of the project

class Config:
    SECRET_KEY=config('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS=config('SQLALCHEMY_TRACK_MODIFICATIONS',cast=bool)
    
    
class DevConfig(Config):
     SQLALCHEMY_DATABASE_URI="sqlite:///"+os.path.join(BASE_DIR,'dev.db')
     DEBUG=True           #enables flak debug mode
     SQLALCHEMY_ECHO=True  #show SQL queries in console
     
class ProdConfig(Config):
         pass
     
class TestConfig(Config):           
    SQLALCHEMY_DATABASE_URI='sqlite:///test.db'
    SQLALCHEMY_ECHO=False      #turns off SQL query logging during tests
    TESTING=True
    