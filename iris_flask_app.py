#iris flask app
#Jay mataji
from flask import Flask, request, flash, url_for, redirect, render_template
import gunicorn
app=Flask(__name__)

from sklearn.externals import joblib
mod=joblib.load("iris_model")

def model_op(sl,sw,pw):    
    x=mod.predict([[sl,sw,pw]])
    for i in x:
        a=i 
        
    if a==0:
        flower="setosa"
        
    elif a==1:
        flower= "versicolor"
        
    elif a==2:
        flower="virginica"
            
    return flower


from datetime import datetime,date

today=(datetime.now().ctime())
#/ home / about app
@app.route("/")
def home():
    return render_template("home.html",today=today)

#/ get_data /gethering data from user
@app.route("/get_data",methods=["GET","POST"])
def get_data():
    global data_dict
    
    if request.method=="POST":
        if not request.form['sl'] or not request.form['sw'] or not request.form['pw']:
            return "plzz fill all the data"
        else:
            sl=(request.form["sl"])
            sw=(request.form["sw"])
            pw=(request.form["pw"])
            
            result=model_op(sl,sw,pw)
            
            data_dict={"sl":sl,"sw":sw,"pw":pw,"result":result}
            
            return redirect(url_for("show_pred_result"))
            
           
        
    return render_template("get_data_from_user.html")

     

@app.route("/show_result")
def show_pred_result():
    return render_template("show_result_of_prediction.html",ip_data=data_dict)

@app.route("/about_us")
def about_us():
    return f"<h1>this simple flask app,deploy on heroku. made by Kunal Padhiyar.God_Father<h1>"

if __name__=="__main__":
    app.run()
    
    
    
    
    
    
    
    
    
    
    
