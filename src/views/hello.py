from flask import (
    Blueprint,
    render_template)

bp = Blueprint('hello', __name__, url_prefix='/')

@bp.route('/')
def index():
    """
    Display an empty or welcome page
    """
    return render_template('business-card-list/index.html')