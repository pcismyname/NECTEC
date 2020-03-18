import pymongo
from flask import *
from pymongo import MongoClient

client = MongoClient()
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
app = Flask(__name__,template_folder='html00')

db = client.information
col = db.info
print(myclient.list_database_names())

@app.route('/')
def host():
    return render_template('form.html')

@app.route('/',methods =['POST'])
def submit():
     name = request.form['name']
     surename = request.form['surename']
     email = request.form['email']
     contact = request.form['contact']
     gender = request.form['gender']
     col.insert_one({'name': name,'surenane':surename,'email':email,'contact':contact,'gender':gender})
     return render_template('back.html')

@app.route('/back',methods=['POST'])
def back():
    return render_template('form.html')

if __name__ == "__main__":
    app.run(debug=True,port=50)