from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    name = request.args.get('name', '')
    message = f"Welcome, {name}!" if name else "Welcome to the Flask Web App!"
    return render_template('home.html', message=message)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/thank_you', methods=['POST'])
def thank_you():
    name = request.form['name']
    email = request.form['email']
    return render_template('thank_you.html', name=name, email=email)

if __name__ == '__main__':
    app.run(debug=True)
