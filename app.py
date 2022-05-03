#flask library
from flask import Flask, render_template, request, url_for

#pickle library
import pickle

#pandas and numpy (dataframe) library
import pandas as pd
import numpy as np

#CORS Policy library
from flask_cors import CORS, cross_origin

#Flask main application
app = Flask(__name__,template_folder='view')

#open and read the RF-model
rfModel = pickle.load(open('rFModel.pickle','rb'))


@app.route("/", methods = ['GET', 'POST'])
def home():
    gender = ['Male', 'Female']
    return render_template('index.html', gender = gender)

@app.route('/predict-liver-tumor',methods=['POST'])
@cross_origin()
def predictTumor():
    age = int(request.form.get('age'))
    gender = str(request.form.get('gender'))
    totalbilirubin = float(request.form.get('totalbilirubin'))
    directbilirubin = float(request.form.get('directbilirubin'))
    alkaline = float(request.form.get('alkaline'))
    alamine = float(request.form.get('alamine'))
    aspartate = float(request.form.get('aspartate'))
    protiens = float(request.form.get('protiens'))
    albumin = float(request.form.get('albumin'))
    ratio  = float(request.form.get('ratio'))
    #print(age, gender, bilirubin, alkaline, alamine, albumin, ratio)
    predictionOfLrModel = rfModel.predict(pd.DataFrame(columns=['Age', 'Total_Bilirubin','Direct_Bilirubin', 'Alkaline_Phosphotase', 'Alamine_Aminotransferase','Aspartate_Aminotransferase','Total_Protiens', 'Albumin', 'Albumin_and_Globulin_Ratio'],
                 data = np.array([age,totalbilirubin,directbilirubin, alkaline, alamine,aspartate,protiens, albumin, ratio]).reshape(1,9)))
    print(predictionOfLrModel[0])
    return str(predictionOfLrModel[0])
if(__name__=="__main__"):
    app.run(debug=True)