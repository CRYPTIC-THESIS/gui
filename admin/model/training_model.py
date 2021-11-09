import pandas as pd
import numpy as np
import CRYPTIC_module as nn
import sys 
import pickle
sys.path.append('..')

from sklearn.model_selection import train_test_split

def split_data(x,crypto):
    x_train, x_test = train_test_split(x, test_size=0.30)
    np.savetxt('csv/'+str(crypto)+"_train_set.csv", x_train, delimiter=",")
    np.savetxt('csv/'+str(crypto)+"_test_set.csv", x_test, delimiter=",")
    print(len(x_train),len(x_test))
    return x_train

dataset_all = pd.read_csv('csv/dataset.csv')

crypto = np.array(dataset_all['Cryptocurrency'])
crypto = np.unique(crypto)
losses = pd.DataFrame()
trained = []
for i in range(len(crypto)):
    data = dataset_all.loc[dataset_all['Cryptocurrency'] == crypto[i]]
    dataset = pd.DataFrame()
    
    dataset['Open'] = data['Open']
    dataset['High'] = data['High']
    dataset['Low'] = data['Low']
    dataset['Close'] = data['Closing']
    dataset['Twitter'] = data['Twitter Volume']
    dataset['Reddit'] = data['Reddit Volume']
    dataset['Google'] = data['GoogleTrends']
    
    Y = np.array(data['Date'])
    
    dataset = np.array(dataset)
    a = dataset[1,0]
    b = dataset[2,0]
    #print(dataset)

    if(crypto[i]=='BTC'):
        btc_model = nn.cryptic(crypto[i])
        data = split_data(dataset,crypto[i])
        btc_loss= btc_model.train(100,data,a,b,crypto[i])
        losses['btc_loss'] = btc_loss
        print('BTC Model Trained!!!')
        trained.append('BTC')
    elif(crypto[i]=='ETH'):
        eth_model = nn.cryptic(crypto[i])
        data = split_data(dataset,crypto[i])
        eth_loss = eth_model.train(100,data,a,b,crypto[i])
        losses['eth_loss'] = eth_loss
        print('ETH Model Trained!!!')
        trained.append('ETH')

    elif(crypto[i]=='DOGE'):
        doge_model = nn.cryptic(crypto[i])
        data = split_data(dataset,crypto[i])
        doge_loss = doge_model.train(100,data,a,b,crypto[i])
        losses['doge_loss'] = doge_loss
        print('DOGE Model Trained!!!')
        trained.append('DOGE')

    else:
        print('Invalid Crypto')

file_name = 'model/obj/trained.pkl'

open_file = open(file_name, "wb")
pickle.dump(trained, open_file)
open_file.close()
    
