from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Joey Musholt in 3308'

@app.route('/db_test')
def test_db():
    db_url = 'postgresql://jm_db_2c3z_user:byXbToPGSweTUlwrlbE9BL5zS4U12AuM@dpg-d241lgfdiees73a91fjg-a/jm_db_2c3z'
    conn = psycopg2.connect(db_url)
    conn.close()
    return 'Database Connection Successful'