from flask import Flask, redirect, url_for, session, request, render_template
import sqlite3
import requests
from flask_session import Session
import base64

# Initialize Flask app
app = Flask(__name__)

# Secret key and session configuration
app.secret_key = 'mysecretkey'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# GitHub OAuth credentials
CLIENT_ID = 'Ov23liZXf21wqzwWyv2Z'
CLIENT_SECRET = '04af23472a11f7db6273ed006ef91b49765b282f'
REDIRECT_URI = 'http://localhost:3000/auth/github/callback'

# Database setup
DB_NAME = 'users.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            github_id TEXT UNIQUE,
            email TEXT,
            access_token TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Route: Home page
@app.route('/')
def home():
    if 'github_id' in session:
        return redirect(url_for('welcome'))
    return render_template('home.html')

# Route: Start GitHub login
@app.route('/login')
def login():
    github_auth_url = (
        f"https://github.com/login/oauth/authorize"
        f"?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&scope=user"
    )
    return redirect(github_auth_url)

# Route: GitHub callback
@app.route('/auth/github/callback')
def github_callback():
    code = request.args.get('code')
    if not code:
        return render_template('error.html', message="Authorization code missing.")

    # Exchange authorization code for access token
    token_url = 'https://github.com/login/oauth/access_token'
    token_data = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'code': code
    }
    headers = {'Accept': 'application/json'}
    response = requests.post(token_url, data=token_data, headers=headers)
    token_json = response.json()

    access_token = token_json.get('access_token')
    if not access_token:
        return render_template('error.html', message="Failed to get access token.")

    # Fetch user information
    user_url = 'https://api.github.com/user'
    user_headers = {'Authorization': f'token {access_token}'}
    user_response = requests.get(user_url, headers=user_headers)
    user_data = user_response.json()

    username = user_data.get('login')
    github_id = user_data.get('id')
    email = user_data.get('email', 'No public email')

    # Save user information in the database
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('INSERT OR IGNORE INTO user (username, github_id, email, access_token) VALUES (?, ?, ?, ?)',
              (username, github_id, email, access_token))
    conn.commit()
    conn.close()

    # Store user in session
    session['github_id'] = github_id
    session['access_token'] = access_token

    return redirect(url_for('welcome'))

# Route: Welcome page
@app.route('/welcome')
def welcome():
    if 'github_id' not in session:
        return redirect(url_for('home'))

    github_id = session['github_id']
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('SELECT username, email, github_id FROM user WHERE github_id = ?', (github_id,))
    user = c.fetchone()
    conn.close()

    return render_template('welcome.html', username=user[0], email=user[1], github_id=user[2])

# Route: Logout
@app.route('/logout')
def logout():
    session.clear()  # Clear all session data
    return redirect(url_for('home'))

# Route: Delete Account

@app.route('/delete_account')
def delete_account():
    if 'github_id' in session and 'access_token' in session:
        github_id = session['github_id']
        access_token = session['access_token']

        # Step 1: Revoke the token on GitHub
        revoke_url = f'https://api.github.com/applications/{CLIENT_ID}/token'
        auth_value = base64.b64encode(f'{CLIENT_ID}:{CLIENT_SECRET}'.encode()).decode()
        revoke_headers = {
            'Authorization': f'Basic {auth_value}',
            'Accept': 'application/json'
        }
        revoke_data = {'access_token': access_token}
        revoke_response = requests.delete(revoke_url, headers=revoke_headers, json=revoke_data)

        if revoke_response.status_code not in [200, 204]:
            return render_template('error.html', message="Failed to revoke access on GitHub.")

        # Step 2: Delete the user from the database
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute('DELETE FROM user WHERE github_id = ?', (github_id,))
        conn.commit()
        conn.close()

        # Step 3: Clear the session
        session.clear()

    return redirect(url_for('home'))


# Initialize the database
init_db()

# Run the app
if __name__ == '__main__':
    app.run(host='localhost', port=3000, debug=True)

