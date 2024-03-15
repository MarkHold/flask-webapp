from flask import Blueprint

# The Blueprint class is used to create a blueprint. 
#The first argument is the name of the blueprint, 
#and the second argument is the name of the module or package where the blueprint is located.
views = Blueprint('views', __name__)

# The views.route decorator is used to register the route for the home page.
@views.route('/')
def home():
    return "<h1>Hello, World!</h1>"