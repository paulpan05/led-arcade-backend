from flask import Blueprint, request, render_template
from werkzeug.exceptions import abort

from flaskr.db import get_db

bp = Blueprint('dashboard', __name__)

@bp.route('/')
def main_page():
    return ''