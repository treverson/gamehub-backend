from mysql.connector import MySQLConnection
from binascii import hexlify
import sys
import os


if sys.argv[1] == 'game' \
and sys.argv[2] == 'add':
    conn = MySQLConnection(
        user='gamehub',
        password='gamehub',
        host='localhost',
        database='gamehub',
    )
    pubkey = hexlify(os.urandom(32)).decode('utf8')
    cursor = conn.cursor()
    cursor.execute(('insert into game (description, `publicKey`) '
                    'values (%s, %s)'),
                    (sys.argv[3], pubkey, )
                    )
    game_id = cursor.lastrowid
    conn.commit()
    print('inserted id: {}'.format(game_id))
