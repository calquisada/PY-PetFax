from flask import Flask

def create_app():
    # config
    app = Flask(__name__)

    # index route
    @app.route('/')
    def hello():
        return 'Hello, this is PetFax!'
    
    # register pet blueprint
    from . import pet
    app.register_blueprint(pet.bp)
    
    return app