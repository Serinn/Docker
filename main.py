import pandas as pd
from flask import Flask,render_template,request,jsonify
import json
import numpy as np
import pickle

app = Flask(__name__)
@app.route('/')
def index1():
    return 'Hello, World!'

def get_arguments():
    parser = argparse.ArgumentParser(description='Get pickle file')
    parser.add_argument('-path', help='get pickle file', required=True)
    args = parser.parse_args()
    return args.path

@app.route('/predict', methods = ["GET", "POST"]) 

def price_prediction():
    #if the request is POST request
    if request.method == 'POST':
        data = request.get_json()
        for i in range(6):    
           features.append(json_req['features'])
        
        features = np.array(features, dtype=float).reshape(1,6)
        predicted_price = loaded_model.price_prediction(features)[0]
        prediction = {'predicted_price': predicted_price}
        return jsonify(prediction)
    else:
        data = request.get_json()
        for i in range(6):
        transaction_date = request.args.get('transaction_date'))
        house_age = request.args.get('house_age'))
        nearest_distance = request.args.get('nearest_distance'))
        num_convenience_stores = request.args.get('num_convenience_stores'))
        latitude = request.args.get('latitude'))
        longitude = request.args.get('longitude'))
        features = np.array([transaction_date, house_age, nearest_distance,
                                   num_convenience_stores, latitude, longitude]).reshape(1, 6)
        predicted_price = loaded_model.price_prediction(features)[0]
        pred_price = {'predicted_price': predicted_price}
        return jsonify(pred_price)
         
    
if __name__=='__main__':
  file_path = get_arguments()
  #Load the model 
  loaded_model = pickle.load(open(file_path, 'rb'))  
  app.run(debug=True, host='0.0.0.0', port=5000)
