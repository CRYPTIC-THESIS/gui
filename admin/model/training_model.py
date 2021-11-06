import pandas as pd
import numpy as np
import CRYPTIC_module as nn
import sys 
import pickle
sys.path.append('..')

from sklearn.model_selection import train_test_split

def split_data(x,crypto):
    x_train, x_test = train_test_split(x, test_size=0.30)
    np.savetxt(str(crypto)+"_train_set.csv", x_train, delimiter=",")
    np.savetxt(str(crypto)+"_test_set.csv", x_test, delimiter=",")
    return x_train

dataset_all = pd.read_csv('csv/dataset.csv')

crypto = np.array(dataset_all['Cryptocurrency'])
crypto = np.unique(crypto)
losses = pd.DataFrame()
trained = []
for i in range(1):
    data = dataset_all.loc[dataset_all['Cryptocurrency'] == crypto[i]]
    dataset = pd.DataFrame()
    dataset['Close'] = data['Closing']
    dataset['Open'] = data['Open']
    dataset['High'] = data['High']
    dataset['Low'] = data['Low']
    dataset['Twitter'] = data['Twitter Volume']
    dataset['Reddit'] = data['Reddit Volume']
    dataset['Google'] = data['GoogleTrends']

    dataset = dataset.fillna(0)
    Y = np.array(data['Date'])
    X = np.array(dataset['Close'])
    X = X.astype(int)

    dataset = np.array(dataset)
    dataset = dataset.astype(int)
    #print(dataset)

    if(crypto[i]=='BTC'):
        btc_model = nn.cryptic(crypto[i])
        data = split_data(dataset,crypto[i])
        btc_loss= btc_model.train(10,data,X,crypto[i])
        losses['btc_loss'] = btc_loss
        print('BTC Model Trained!!!')
        trained.append('BTC')
    elif(crypto[i]=='ETH'):
        eth_model = nn.cryptic(crypto[i])
        data = split_data(dataset,crypto[i])
        eth_loss = eth_model.train(10,data,X,crypto[i])
        losses['eth_loss'] = eth_loss
        print('ETH Model Trained!!!')
        trained.append('ETH')

    elif(crypto[i]=='DOGE'):
        doge_model = nn.cryptic(crypto[i])
        data = split_data(dataset,crypto[i])
        doge_loss = doge_model.train(10,data,X,crypto[i])
        losses['doge_loss'] = doge_loss
        print('DOGE Model Trained!!!')
        trained.append('DOGE')

    else:
        print('Invalid Crypto')

file_name = "trained.pkl"

open_file = open(file_name, "wb")
pickle.dump(trained, open_file)
open_file.close()
    
