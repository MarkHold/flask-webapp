from flask import Blueprint

auth = Blueprint('auth', __name__)

# The auth.route decorator is used to register the route for the login page.
@auth.route('/login')
def login():
    return "<p>Login</p>"

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"