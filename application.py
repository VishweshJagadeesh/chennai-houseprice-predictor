import pickle
from flask import Flask, request, render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import PredictPipeline, CustomData
from src.exception import CustomException


application = Flask(__name__)
app=application

##Route for home page##


@application.route('/', methods=['GET','POST'])
def predict_datapoint():
    if request.method=="GET":
        return render_template('app.html')
    else:
        data= CustomData(
            AREA=request.form['area'],
            SALE_COND=request.form['sale_cond'],
            PARK_FACIL=int(request.form['park_facil']=='yes'),
            UTILITY_AVAIL=request.form['utility_avail'],
            BUILDTYPE=request.form['buildtype'],
            STREET=request.form['street'],
            MZZONE=request.form['mzzone'],
            PROPERTY_AGE=int(request.form['property_age']),
            INT_SQFT=int(request.form['int_sqft']),
            N_BEDROOM=int(request.form['n_bedroom']),
            N_BATHROOM=int(request.form['n_bathroom']),
            N_ROOM=int(request.form['n_room'])
        )
        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline=PredictPipeline()
        print("Mid Prediction")
        results=predict_pipeline.predict(pred_df)
        print("after Prediction")
        return render_template('app.html',results=results[0])
    

if __name__=="__main__":
    application.run(host="0.0.0.0",debug=True)