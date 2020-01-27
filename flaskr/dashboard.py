from flask import Blueprint, request, render_template
from werkzeug.exceptions import abort

from flaskr.db import get_db

bp = Blueprint('dashboard', __name__)