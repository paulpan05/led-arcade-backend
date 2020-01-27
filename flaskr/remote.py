from flask import Blueprint, request
from werkzeug.exceptions import abort

from flaskr.db import get_db

bp = Blueprint('remote', __name__)

@bp.route('/add-game', methods=['POST'])
def add_game():
    username = request.form['username']
    round_number = request.form['round_number']
    millis = request.form['millis']
    score = request.form['score']
    db = get_db()
    db.execute('INSERT INTO user_play(username, round_number, millis, score) ' +
        'VALUES(?, ?, ?, ?)', [username, round_number, millis, score])
    db.commit()
    return 'Success'
    