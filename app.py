from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def init_db():
    """Initialize the SQLite database and create the contacts table."""
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS contacts
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT, message TEXT)''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    """Render the contact form."""
    return render_template('contact.html')

@app.route('/submit', methods=['POST'])
def submit():
    """Handle form submission and store data in SQLite."""
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)", (name, email, message))
    conn.commit()
    conn.close()
    
    return redirect('/')

if __name__ == '__main__':
    init_db()  # Ensure the database is set up before running
    app.run(debug=True)
