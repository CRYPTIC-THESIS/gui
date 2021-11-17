import pandas as pd
import numpy as np
import CRYPTIC_module as nn
import sys 
sys.path.append('..')
import pickle
from admin import dbconnect as db

cryptic_model = nn.cryptic()
dataset_all = pd.read_csv('csv/dataset.csv')
mod_type = ''
if (dataset_all.shape[1] == 7):
    mod_type = 'half'
else:
    mod_type = 'full'
crypto = np.array(dataset_all['Cryptocurrency'])
crypto = np.unique(crypto)
losses = pd.DataFrame()
deployed = []

for i in range(len(crypto)):
    data = dataset_all.loc[dataset_all['Cryptocurrency'] == crypto[i]]
    dataset = pd.DataFrame()
    
    dataset['Open'] = data['Open']
    dataset['High'] = data['High']
    dataset['Low'] = data['Low']
    dataset['Close'] = data['Closing']
    if(mod_type == 'full'):
        dataset['Twitter'] = data['Twitter']
        dataset['Reddit'] = data['Reddit']
        dataset['Google'] = data['GoogleTrends']

    Y = np.array(data['Date'])
    
    data = np.array(dataset)
    preds = pd.DataFrame(columns = ['date','pred'])
    if(crypto[i]=='BTC'):
        print('Retraining BTC Model Before Deployment')
        date,pred = cryptic_model.retrain(10,data,crypto[i],Y[-1]) 
        preds['date'] = pd.Series(date)  
        preds['pred'] = pd.Series(pred)
        preds.to_csv('csv/BTC_Predictions.csv')
        deployed.append('BTC')
    elif(crypto[i]=='ETH'):
        print('Retraining ETH Model Before Deployment')
        date,pred = cryptic_model.retrain(10,data,crypto[i],Y[-1])        
        preds['date'] = pd.Series(date)  
        preds['pred'] = pd.Series(pred)
        preds.to_csv('csv/ETH_Predictions.csv')
        deployed.append('ETH')

    elif(crypto[i]=='DOGE'):
        print('Retraining Doge Model Before Deployment')
        date,pred = cryptic_model.retrain(10,data,crypto[i],Y[-1])
        preds['date'] = pd.Series(date)  
        preds['pred'] = pd.Series(pred)
        preds.to_csv('csv/DOGE_Predictions.csv')
        deployed.append('DOGE')

    else:
        print('Invalid Crypto')

file_name = 'model/obj/ready_to_deploy.pkl'

open_file = open(file_name, "wb")
pickle.dump(deployed, open_file)
open_file.close()