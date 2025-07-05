# Importing
from flask import Flask, render_template
import os

# Integration
app = Flask(__name__)

picfolder = os.path.join('static')

app.config["UPLOAD_FOLDER"] = picfolder
# Mapping
@app.route('/')

# Inputs
def first():
    pic = os.path.join(app.config["UPLOAD_FOLDER"], "Waterfall.jpg")
    newpic = os.path.join(app.config["UPLOAD_FOLDER"], "nature.jpg")
    return render_template('home.html',user_image = pic,nature = newpic)

# Mapping
@app.route('/second')

# Inputs
def second():
    return render_template('second.html')

# Main
if __name__ == '__main__':
    app.run(debug=True)