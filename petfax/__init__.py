from flask import Flask
from flask_migrate import Migrate

def create_app():
    # config
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Dilla702$@localhost:5432/petfax'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

    from . import models
    models.db.init_app(app)
    migrate = Migrate(app, models.db)

    # index route
    @app.route('/')
    def hello():
        return 'Hello, this is PetFax!'
    
    # register pet blueprint
    from . import pet
    app.register_blueprint(pet.bp)

    # register fact blueprint
    from . import fact
    app.register_blueprint(fact.bp)           

    
    return app