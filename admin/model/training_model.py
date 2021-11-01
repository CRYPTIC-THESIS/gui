import pandas as pd
import numpy as np
import sys
import CRYPTIC_module as nn
dataset_all = pd.read_csv('./dataset.csv')

crypto = np.array(dataset_all['Cryptocurrency'])
crypto = np.unique(crypto)

#for i in range(len(crypto)):
data = dataset_all.loc[dataset_all['Cryptocurrency'] == crypto[0]]
dataset = pd.DataFrame(columns = ['High','Low','Open','Closing','Twitter Volume','Reddit Volume','GoogleTrends'])
dataset['Open'] = data['Open']
dataset['High'] = data['High']
dataset['Low'] = data['Low']
dataset['Close'] = data['Closing']
dataset['Twitter'] = data['Twitter Volume']
dataset['Reddit'] = data['Reddit Volume']
dataset['Google'] = data['GoogleTrends']
dataset = dataset.fillna(0)
Y = np.array(data['Date'])
X = np.array(dataset['Close'])
dataset = np.array(dataset)

labels = [i for i in range(len(dataset))]
labels = np.array(labels,dtype=int)

if(crypto[0]=='BTC'):
    btc_model = nn.cryptic(crypto[0])
    loss,btc_trained = btc_model.train(300,dataset,X)
elif(crypto[0]=='ETH'):
    eth_model = nn.cryptic(crypto[0])
    loss,eth_trained = eth_model.train(300,dataset,X)
elif(crypto[0]=='DOGE'):
    doge_model = nn.cryptic(crypto[0])
    loss,doge_trained = doge_model.train(300,dataset,X)
else:
    print('Invalid Crypto')

