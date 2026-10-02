from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'finguard_secret_key'

# 1. Home Route -> Redirects to Login
@app.route('/')
def home():
    return redirect(url_for('login'))

# 2. Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        session['user'] = email
        return redirect(url_for('fingerprint'))
    return render_template('login.html')

# 3. Fingerprint Verification Page
@app.route('/fingerprint')
def fingerprint():
    return render_template('fingerprint.html')

# 4. Link Account Page
@app.route('/link-account')
@app.route('/link_account')
@app.route('/link_account.html')
def link_account():
    return render_template('link_account.html')

# 5. Main Categorization & Dashboard Page (Firebase Integrated)
@app.route('/categorization')
@app.route('/categorization.html')
@app.route('/dashboard')
def categorization():
    return render_template('categorization.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)