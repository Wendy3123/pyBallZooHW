from flask import (Blueprint, render_template)


bp = Blueprint('reptile',__name__, url_prefix='/reptiles')

@bp.route('/')
def index():
    return 'reptiles data placeholder'
