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
    mod_type = 'full'
elif (dataset_all.shape[1] == 4):
    mod_type = 'half'
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
        dataset['Twitter'] = data['Twitter Volume']
        dataset['Reddit'] = data['Reddit Volume']
        dataset['Google'] = data['GoogleTrends']

    Y = np.array(data['Date'])
    
    data = np.array(dataset)

    if(crypto[i]=='BTC'):
        print('Retraining BTC Model Before Deployment')
        date,pred = cryptic_model.retrain(10,data,crypto[i],Y[-1]) 
        db.add_predictions('BTC_predict',pred,date)    
        print('BTC Model Deployed!!!\n\n')
        deployed.append('BTC')
    elif(crypto[i]=='ETH'):
        print('Retraining ETH Model Before Deployment')
        date,pred = cryptic_model.retrain(10,data,crypto[i],Y[-1])        
        db.add_predictions('ETH_predict',pred,date)
        print('ETH Model Deployed!!!\n\n')
        deployed.append('ETH')

    elif(crypto[i]=='DOGE'):
        print('Retraining Doge Model Before Deployment')
        date,pred = cryptic_model.retrain(10,data,crypto[i],Y[-1])
        db.add_predictions('DOGE_predict',pred,date)
        print('DOGE Model Deployed!!!\n\n')
        deployed.append('DOGE')

    else:
        print('Invalid Crypto')

file_name = 'model/obj/deployed.pkl'

open_file = open(file_name, "wb")
pickle.dump(deployed, open_file)
open_file.close()