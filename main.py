from flask import Flask, render_template, url_for,request
import numpy as np
from sklearn.externals import joblib
import pandas as pd


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("demo1.html")
	
@app.route('/home')
def h1():
    return render_template("h1.html")
	
@app.route('/home/base')
def base():
    return render_template("base.html")

@app.route('/h1/rice')
def rice():
    return render_template("homerice.html")
	
@app.route('/h1/groundnut')
def gnd():
    return render_template("homegroundnut.html")
	
@app.route('/h1/wheat')
def wh():
    return render_template("homewheat.html")
	
@app.route('/h1/sugercane')
def sug():
    return render_template("homesugarcane.html")

@app.route('/h1/jowar')
def jow():
    return render_template("homejowar.html")

@app.route('/h1/district')
def district():
    return render_template("district.html")

@app.route('/h1/district/nashik')
def nas():
    return render_template("nas.html")

@app.route('/h1/district/kolhapur')
def kol():
    return render_template("kol.html")    

@app.route('/h1/district/satara')
def sat():
    return render_template("sat.html")

@app.route('/h1/district/solapur')
def sol():
    return render_template("sol.html") 

@app.route('/h1/district/sangli')
def san():
    return render_template("san.html")          

@app.route('/h1/crop')
def crop():
    return render_template("cropinfo.html") 

@app.route('/h1/cropdist')
def cropdist():
    return render_template("cropinfo_dist.html") 

@app.route('/h1/cropwater')
def water():
    return render_template("water.html") 

@app.route('/contactus')
def contact():
    return render_template("contact.html") 




@app.route("/predictrice", methods=['GET','POST'])

def predictrice():
    global pred_args,District
    if request.method == 'POST':
        try:
            District = ["kolhapur","Nashik","Satara","Sangli","Solapur"]
            District = request.form['District']
            if District == 'kolhapur':
                kolhapur = 1
                Nashik = 0
                Satara = 0
                Sangli = 0
                Solapur = 0
            if District == 'Nashik':
                kolhapur = 0
                Nashik = 1
                Satara = 0
                Sangli = 0
                Solapur = 0
            if District == 'Satara':
                kolhapur = 0
                Nashik = 0
                Satara = 1
                Sangli = 0
                Solapur = 0
            if District == 'Sangli':
                kolhapur = 0
                Nashik = 0
                Satara = 0
                Sangli = 1
                Solapur = 0
            if District == 'Solapur':
                kolhapur = 0
                Nashik = 0
                Satara = 0
                Sangli = 0
                Solapur = 1
            Year = float(request.form['Year'])
            Area = float(request.form['Area'])
            Production = float(request.form['Production'])
            Annual_rainfall = float(request.form['Annual_rainfall'])
            Temperature = float(request.form['Temperature'])
            pred_args = [kolhapur, Nashik, Satara, Sangli, Solapur, Year, Area, Production, Annual_rainfall, Temperature]
            pred_args_arr = np.array(pred_args)
            pred_args_arr = pred_args_arr.reshape(1,-1)
            mul_reg = open("multiple_regression_rice_model.pkl","rb")
            ml_model = joblib.load(mul_reg)
            model_prediction = ml_model.predict(pred_args_arr)
            model_prediction = round(float(model_prediction), 2)
        except ValueError:
                return "Please check the entered values"
        return render_template('predict.html', prediction = model_prediction )
               

@app.route("/predictwheat", methods=['GET','POST'])

def predictwheat():
    global pred_args,District
    if request.method == 'POST':
        try:
            District = ["kolhapur","Nashik","Satara","Sangli","Solapur"]
            District = request.form['District']
            if District == 'kolhapur':
                kolhapur = 1
                Nashik = 0
                Satara = 0
                Sangli = 0
                Solapur = 0
            if District == 'Nashik':
                kolhapur = 0
                Nashik = 1
                Satara = 0
                Sangli = 0
                Solapur = 0
            if District == 'Satara':
                kolhapur = 0
                Nashik = 0
                Satara = 1
                Sangli = 0
                Solapur = 0
            if District == 'Sangli':
                kolhapur = 0
                Nashik = 0
                Satara = 0
                Sangli = 1
                Solapur = 0
            if District == 'Solapur':
                kolhapur = 0
                Nashik = 0
                Satara = 0
                Sangli = 0
                Solapur = 1
            Year = float(request.form['Year'])
            Area = float(request.form['Area'])
            Production = float(request.form['Production'])
            Annual_rainfall = float(request.form['Annual_rainfall'])
            Temperature = float(request.form['Temperature'])
            pred_args = [kolhapur, Nashik, Satara, Sangli, Solapur, Year, Area, Production, Annual_rainfall, Temperature]
            pred_args_arr = np.array(pred_args)
            pred_args_arr = pred_args_arr.reshape(1,-1)
            mul_reg = open("multiple_regression_wheat_model.pkl","rb")
            ml_model = joblib.load(mul_reg)
            model_prediction = ml_model.predict(pred_args_arr)
            model_prediction = round(float(model_prediction), 2)
        except ValueError:
                return "Please check the entered values"
        return render_template('predict.html', prediction = model_prediction )


@app.route("/predictsugarcane", methods=['GET','POST'])

def predictsugarcane():
    global pred_args,District
    if request.method == 'POST':
        try:
            District = ["kolhapur","Nashik","Satara","Sangli","Solapur"]
            District = request.form['District']
            if District == 'kolhapur':
                kolhapur = 1
                Nashik = 0
                Satara = 0
                Sangli = 0
                Solapur = 0
            if District == 'Nashik':
                kolhapur = 0
                Nashik = 1
                Satara = 0
                Sangli = 0
                Solapur = 0
            if District == 'Satara':
                kolhapur = 0
                Nashik = 0
                Satara = 1
                Sangli = 0
                Solapur = 0
            if District == 'Sangli':
                kolhapur = 0
                Nashik = 0
                Satara = 0
                Sangli = 1
                Solapur = 0
            if District == 'Solapur':
                kolhapur = 0
                Nashik = 0
                Satara = 0
                Sangli = 0
                Solapur = 1
            Year = float(request.form['Year'])
            Area = float(request.form['Area'])
            Production = float(request.form['Production'])
            Annual_rainfall = float(request.form['Annual_rainfall'])
            Temperature = float(request.form['Temperature'])
            pred_args = [kolhapur, Nashik, Satara, Sangli, Solapur, Year, Area, Production, Annual_rainfall, Temperature]
            pred_args_arr = np.array(pred_args)
            pred_args_arr = pred_args_arr.reshape(1,-1)
            mul_reg = open("multiple_regression_sugarcane_model.pkl","rb")
            ml_model = joblib.load(mul_reg)
            model_prediction = ml_model.predict(pred_args_arr)
            model_prediction = round(float(model_prediction), 2)
        except ValueError:
                return "Please check the entered values"
        return render_template('predict.html', prediction = model_prediction )

@app.route("/predictgroundnut", methods=['GET','POST'])

def predictgroundnut():
    global pred_args,District
    if request.method == 'POST':
        try:
            District = ["kolhapur","Nashik","Satara","Sangli","Solapur"]
            District = request.form['District']
            if District == 'kolhapur':
                kolhapur = 1
                Nashik = 0
                Satara = 0
                Sangli = 0
                Solapur = 0
            if District == 'Nashik':
                kolhapur = 0
                Nashik = 1
                Satara = 0
                Sangli = 0
                Solapur = 0
            if District == 'Satara':
                kolhapur = 0
                Nashik = 0
                Satara = 1
                Sangli = 0
                Solapur = 0
            if District == 'Sangli':
                kolhapur = 0
                Nashik = 0
                Satara = 0
                Sangli = 1
                Solapur = 0
            if District == 'Solapur':
                kolhapur = 0
                Nashik = 0
                Satara = 0
                Sangli = 0
                Solapur = 1
            Year = float(request.form['Year'])
            Area = float(request.form['Area'])
            Production = float(request.form['Production'])
            Annual_rainfall = float(request.form['Annual_rainfall'])
            Temperature = float(request.form['Temperature'])
            pred_args = [kolhapur, Nashik, Satara, Sangli, Solapur, Year, Area, Production, Annual_rainfall, Temperature]
            pred_args_arr = np.array(pred_args)
            pred_args_arr = pred_args_arr.reshape(1,-1)
            mul_reg = open("multiple_regression_groundnut_model.pkl","rb")
            ml_model = joblib.load(mul_reg)
            model_prediction = ml_model.predict(pred_args_arr)
            model_prediction = round(float(model_prediction), 2)
        except ValueError:
                return "Please check the entered values"
        return render_template('predict.html', prediction = model_prediction )

@app.route("/predictjowar", methods=['GET','POST'])

def predictjowar():
    global pred_args,District
    if request.method == 'POST':
        try:
            District = ["kolhapur","Nashik","Satara","Sangli","Solapur"]
            District = request.form['District']
            if District == 'kolhapur':
                kolhapur = 1
                Nashik = 0
                Satara = 0
                Sangli = 0
                Solapur = 0
            if District == 'Nashik':
                kolhapur = 0
                Nashik = 1
                Satara = 0
                Sangli = 0
                Solapur = 0
            if District == 'Satara':
                kolhapur = 0
                Nashik = 0
                Satara = 1
                Sangli = 0
                Solapur = 0
            if District == 'Sangli':
                kolhapur = 0
                Nashik = 0
                Satara = 0
                Sangli = 1
                Solapur = 0
            if District == 'Solapur':
                kolhapur = 0
                Nashik = 0
                Satara = 0
                Sangli = 0
                Solapur = 1
            Year = float(request.form['Year'])
            Area = float(request.form['Area'])
            Production = float(request.form['Production'])
            Annual_rainfall = float(request.form['Annual_rainfall'])
            Temperature = float(request.form['Temperature'])
            pred_args = [kolhapur, Nashik, Satara, Sangli, Solapur, Year, Area, Production, Annual_rainfall, Temperature]
            pred_args_arr = np.array(pred_args)
            pred_args_arr = pred_args_arr.reshape(1,-1)
            mul_reg = open("multiple_regression_jowar_model.pkl","rb")
            ml_model = joblib.load(mul_reg)
            model_prediction = ml_model.predict(pred_args_arr)
            model_prediction = round(float(model_prediction), 2)
        except ValueError:
                return "Please check the entered values"
        return render_template('predict.html', prediction = model_prediction )

               
	

if __name__  == '__main__' :
    app.run(debug=True)