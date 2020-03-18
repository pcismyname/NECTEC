from flask import *
app = Flask(__name__, template_folder='static')

@app.route('/')
def host():
    return render_template('host.html')

@app.route('/success',methods = ['POST'])
def name():
    return render_template("name.html")

@app.route('/back',methods = ['POST'])
def bname():
    return render_template('host.html')

@app.route('/success2',methods = ['POST'])
def nec():
    return render_template('nectec.html')
@app.route('/success3',methods = ['POST'])
def hello():
    return render_template('hello world.html')

if __name__ == "__main__":
    app.run(debug=True,port=50)