# Importing
from flask import render_template, Flask

# Integration
app = Flask(__name__)


# Mapping
@app.route('/')

# Inputs
def home():
    return render_template('index.html')

# Main

if __name__ == '__main__':
    app.run(debug=True)