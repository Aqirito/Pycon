from flask import (
    Blueprint,
    render_template)

bp = Blueprint('hello', __name__, url_prefix='/')

@bp.route('/')
def index():
    """
    Display an empty or welcome page
    """
    return render_template('hello/index.html')

@bp.route('/a')
def l():
    """
    Display an empty or welcome page
    """
    return "SDSDSD"