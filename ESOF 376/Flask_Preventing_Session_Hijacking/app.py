from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import hashlib

import time # need the time import

# Flask app setup
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # under is my key
#-------------------------------------------------------------
SESSION_TIMEOUT = 900   # 15 minutes
REGENERATE_TIME = 300   # 5 minutes


@app.before_request
def manage_session():
    if 'user_id' in session:

        now = time.time()

        # Destroy session after 15 minutes
        if 'last_activity' in session:
            if now - session['last_activity'] > SESSION_TIMEOUT:
                session.clear()
                return redirect(url_for('login'))

        session['last_activity'] = now

        # Regenerate session every 5 minutes
        if 'created' not in session:
            session['created'] = now
        elif now - session['created'] > REGENERATE_TIME:
            session.clear()
            session['created'] = now
#----------------------------------------------------------------

def init_db():
    """Initialize the database only if the users table is empty."""
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    # Check if the `users` table has any data
    cursor.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name='users';")
    table_exists = cursor.fetchone()[0]

    if table_exists:
        cursor.execute("SELECT COUNT(*) FROM users;")
        row_count = cursor.fetchone()[0]
        if row_count == 0:
            # If the table exists but is empty, initialize it
            with open('test_user.sql', 'r') as f:
                connection.executescript(f.read())
            print("Database initialized successfully.")
        else:
            print("Database already contains data. Skipping initialization.")
    else:
        # If the table does not exist, initialize it
        with open('test_user.sql', 'r') as f:
            connection.executescript(f.read())
        print("Database initialized successfully.")

    connection.close()


@app.route('/')
def home():
    """Redirect to the login page."""
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login route to handle user authentication."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Hash the entered password with SHA-1
        hashed_password = hashlib.sha1(password.encode()).hexdigest()

        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        # Check the username and hashed password
        cursor.execute("SELECT * FROM users WHERE user = ? AND password = ?", (username, hashed_password))
        user = cursor.fetchone()
        connection.close()

        if user:
            session['user_id'] = user[0]
            session['username'] = user[1]
            # here i edited it a bit-------------
            session['last_activity'] = time.time()
            session['created'] = time.time()
            #--------------------------------
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error="Invalid username or password.")

    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    """Dashboard route accessible only after login."""
    if 'user_id' in session:
        return render_template('dashboard.html', username=session['username'])
    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    """Logout route to clear the session."""
    session.pop('user_id', None)
    session.pop('username', None)
    return render_template('logout.html')


@app.route('/create_login', methods=['GET', 'POST'])
def create_login():
    """Route to create a new user."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Hash the password with SHA-1
        hashed_password = hashlib.sha1(password.encode()).hexdigest()

        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        # Check if the username already exists
        cursor.execute("SELECT * FROM users WHERE user = ?", (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            connection.close()
            return render_template('create_login.html', error="Username already exists!")

        # Insert the username and hashed password
        cursor.execute("INSERT INTO users (user, password) VALUES (?, ?)", (username, hashed_password))
        connection.commit()
        connection.close()

        return render_template('success.html', message="User created successfully! Redirecting to login page...")

    return render_template('create_login.html')


if __name__ == '__main__':
    # Initialize the database only if needed
    init_db()
    app.run(debug=True)
