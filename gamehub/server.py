from flask import Flask, request
from mysql.connector import MySQLConnection
from datetime import datetime
import mysql.connector


app = Flask(__name__)

@app.route("/submit-score", methods=['POST'])
def submi_score():
    conn = MySQLConnection(
        user='gamehub',
        password='gamehub',
        host='localhost',
        database='gamehub',
    )

    # Find the game
    game_id = int(request.form.get('game_id', 0))
    score = float(request.form.get('score', 0))
    print(score)
    
    cursor = conn.cursor()
    cursor.execute('select id from game where id = %s',
                   (game_id, )
                   )
    game, = cursor.fetchone()

    if game:
        # insert the score
        cursor = conn.cursor()
        params = (game, score, datetime.utcnow(), )
        query = ('insert into score '
                 '(`idGame`, `score`, `timestamp`) '
                 'values (%s, %s, %s);'
                 )
        cursor.execute(query, params)
        score_id = cursor.lastrowid
        conn.commit()

        return 'OK'

    else:
        return 'IvalidGame'


if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    server = make_server('', 9090, app)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('bye')