import pandas as pd
import numpy as np
import CRYPTIC_module as nn
dataset_all = pd.read_csv('./dataset.csv')

crypto = np.array(dataset_all['Cryptocurrency'])
crypto = np.unique(crypto)

for i in range(len(crypto)):
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

    dataset = np.array(dataset)

    #print(dataset)

    if(crypto[i]=='BTC'):
        btc_model = nn.cryptic(crypto[i])
        btc_loss,btc_trained = btc_model.train(300,dataset,X)
    elif(crypto[i]=='ETH'):
        eth_model = nn.cryptic(crypto[i])
        eth_loss,eth_trained = eth_model.train(300,dataset,X)
    elif(crypto[i]=='DOGE'):
        doge_model = nn.cryptic(crypto[i])
        doge_loss,doge_trained = doge_model.train(300,dataset,X)
    else:
        print('Invalid Crypto')
