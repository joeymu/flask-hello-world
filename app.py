from flask import Flask
import psycopg

app = Flask(__name__)

db_url = 'postgresql://jm_db_2c3z_user:byXbToPGSweTUlwrlbE9BL5zS4U12AuM@dpg-d241lgfdiees73a91fjg-a/jm_db_2c3z'

@app.route('/')
def hello_world():
    return 'Hello World from Joey Musholt in 3308'

@app.route('/db_test')
def test_db():
    conn = psycopg.connect(db_url)
    conn.close()
    return 'Database Connection Successful'

@app.route('/db_create')
def create_db():
    conn = psycopg.connect(db_url)
    cur = conn.cursor()
    sql_text = '''
        CREATE TABLE IF NOT EXISTS Basketball(
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
        '''
    cur.execute(sql_text)
    conn.commit()
    conn.close()
    return 'Basketball table creation successful'

@app.route('/db_insert')
def insert():
    conn = psycopg.connect(db_url)
    cur = conn.cursor()
    sql_text = '''
        INSERT INTO Basketball (First, Last, City, Name, Number)
        Values
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
        '''
    cur.execute(sql_text)
    conn.commit()
    conn.close()
    return 'Basketball Table Successfully Populated'

@app.route('/db_select')
def select():
    conn = psycopg.connect(db_url)
    cur = conn.cursor()
    sql_text = 'SELECT * FROM Basketball'
    cur.execute(sql_text)
    records = cur.fetchall()
    conn.close()
    
    response_string = ''
    response_string += '<table>'
    for player in records:
        response_string += '<tr>'
        for info in player:
            response_string += f'<td>{info}</td>'
        response_string += '</tr>'
    response_string += '</table>'

    return response_string

@app.route('/db_drop')
def drop():
    conn = psycopg.connect(db_url)
    cur = conn.cursor()
    sql_text = 'DROP TABLE Basketball'
    cur.execute(sql_text)
    conn.commit()
    conn.close()
    return 'Basketball Table Successfully Dropped'