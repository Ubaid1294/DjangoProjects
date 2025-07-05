# Importing

from flask import Flask
from flask import render_template, request


# Interaction
web = Flask(__name__)


# Mapping
@web.route('/')
@web.route('/register')


# Inputs
def homepage():
    return render_template('register.html')

@web.route('/confirmation', methods=['GET', 'POST'])

def register():
    if request.method == 'POST':
        n = request.form['name']
        c = request.form['city']
        p = request.form['phonenumber']

        return render_template('confirm.html', name=n, city=c, phonenumber=p)


# Main
if __name__ == '__main__':
    web.run(debug=True)

