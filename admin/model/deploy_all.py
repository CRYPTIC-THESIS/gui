import numpy as np
import pandas as pd
from admin import dbconnect as db
import pickle

open_file = open('model/obj/ready_to_deploy.pkl', "rb")
to_deploy = pl.load(open_file)
open_file.close()

for crypto in to_deploy:

    data = pd.read_csv('csv/'+crypto+'_Predictions.csv')
    pred = data['pred'].values
    date = data['date'].values
    db.add_predictions(crypto+'_predict',pred,date)
    print(crypto+' Model Deployed!!!\n\n')

file_name = 'model/obj/deployed.pkl'
open_file = open(file_name, "wb")
pickle.dump(deployed, open_file)
open_file.close()




