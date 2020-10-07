import pandas as pd
from flask import Flask,render_template,request,jsonify
import json
import numpy as np
import pickle

app = Flask(__name__)
@app.route('/')
def index1():
    return 'Hello, World!'

@app.route('/predict', methods = ["GET", "POST"]) 
def price_pred():
    #if the request is POST request
    if request.method == 'POST':
         price = 0
            # get the features
        features = request.get_json()
            #load the linear model
        loaded_model = pickle.load(open('./model.sav', 'rb'))
        # calculate the price
        for index, feature in enumerate(features["features"]):
            price += float(feature) * float(thetas[index])
        x = np.array(features["features"]).reshape(1,6)
        result = loaded_model.predict(x)
        price += theta0    
        if x.shape[0] == 1:
            result = result[0]
            print(result)
            return json.dumps(price)

        return json.dumps(result)
    else:
        return
if __name__=='__main__':
    theta0 = None
    thetas = None

    paras = pd.read_csv('lm_parameters.csv')
    theta0 = paras.iloc[0,0] 
    thetas = paras.columns 
    app.run(debug=True, host='0.0.0.0')