from flask import request

from flask import Flask, render_template, request

#pickle library
import pickle

#pandas and numpy (dataframe) library
import numpy as np
def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1, 9)
    loaded_model = pickle.load(open("rFModel.pickle", "rb"))
    result = loaded_model.predict(to_predict)
    return result[0]
 
@app.route('/result', methods = ['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(int, to_predict_list))
        result = ValuePredictor(to_predict_list)       
        if int(result)== 1:
            prediction ='No Cure is Required'
        else:
            prediction ='Care to be taken'           
        return render_template("result.html", prediction = prediction)