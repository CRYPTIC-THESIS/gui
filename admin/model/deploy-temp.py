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

def retrain_data():
    global btc_date, btc_pred, eth_date, eth_pred, doge_date, doge_pred
    btc_date = None
    btc_pred = None
    eth_pred = None
    eth_date = None
    doge_date = None
    doge_pred = None

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
        preds = pd.DataFrame(columns = ['date','prediction'])

        if(crypto[i]=='BTC'):
            print('Retraining BTC Model Before Deployment')
            btc_date,btc_pred = cryptic_model.retrain(10,data,crypto[i],Y[-1]) 
            # db.add_predictions('BTC_predict',pred,date)
            preds['date'] = pd.Series(btc_date)  
            preds['pred'] = pd.Series(btc_pred)
            preds.to_csv('csv/BTC_Predictions.csv')
            del preds
            # print('BTC Model Deployed!!!\n\n')
            # deployed.append('BTC')
        elif(crypto[i]=='ETH'):
            print('Retraining ETH Model Before Deployment')
            eth_date,eth_pred = cryptic_model.retrain(10,data,crypto[i],Y[-1])        
            # db.add_predictions('ETH_predict',pred,date)
            # print('ETH Model Deployed!!!\n\n')
            # deployed.append('ETH')

        elif(crypto[i]=='DOGE'):
            print('Retraining Doge Model Before Deployment')
            doge_date,doge_pred = cryptic_model.retrain(10,data,crypto[i],Y[-1])
            # db.add_predictions('DOGE_predict',pred,date)
            # print('DOGE Model Deployed!!!\n\n')
            # deployed.append('DOGE')

        else:
            print('Invalid Crypto')

retrain_data()

if (btc_date is not None) and (btc_pred is not None):
    # db.add_predictions('BTC_predict',btc_pred,btc_date)
    print(btc_pred,btc_date)
    print('BTC Model Deployed!!!\n\n')
    deployed.append('BTC')

# if eth_date and eth_pred:
#     db.add_predictions('ETH_predict',eth_pred,eth_date)
#     print('ETH Model Deployed!!!\n\n')
#     deployed.append('ETH')

# if doge_date and doge_pred:
#     db.add_predictions('DOGE_predict',doge_pred,doge_date)
#     print('DOGE Model Deployed!!!\n\n')
#     deployed.append('DOGE')


file_name = 'model/obj/deployed.pkl'

open_file = open(file_name, "wb")
pickle.dump(deployed, open_file)
open_file.close()