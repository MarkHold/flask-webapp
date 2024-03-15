from flask import Flask

# The create_app function is used to create the Flask application.
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '123123'
 
    # Importing the blueprints
    from .views import views
    from .auth import auth

    # Registering the blueprints
    # What are blueprints?
    # Blueprints are a way to organize related routes in a Flask application.
    # They are used to define a collection of routes and associated views.
    # The Blueprint class is used to create a blueprint.
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/auth/')
    
    return app