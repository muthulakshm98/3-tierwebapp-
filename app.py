from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_data():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
    cursor.execute("INSERT INTO users (name) VALUES ('Hello from Web DB')")
    conn.commit()
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()
    conn.close()
    return data

@app.route('/')
def home():
    data = get_data()
    return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
