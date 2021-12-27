from flask import Flask
from flask import render_template

app = Flask(__name__, template_folder='template')

@app.route("/")
# define the view using a function, which returns a string
def hello_world(name =None):
    return render_template('index.html', name = name)

@app.route('/reg')
def register():
    return render_template('registration.html')
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)