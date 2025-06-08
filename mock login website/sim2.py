from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Store credentials temporarily
registered_user = {}

@app.route('/register', methods=['GET', 'POST'])
def register():
    message = ''
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        registered_user['email'] = email
        registered_user['password'] = password
        message = 'Registered successfully. Go to login.'

    return render_template('register.html', message=message)

@app.route('/login', methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if registered_user.get('email') == email and registered_user.get('password') == password:
            message = 'Login successful!'
        else:
            message = 'Invalid credentials.'

    return render_template('login.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
