from flask import Blueprint, request
from werkzeug.exceptions import abort

from flaskr.db import get_db

bp = Blueprint('remote', __name__)