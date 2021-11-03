import pandas as pd
import numpy as np
import CRYPTIC_module as nn

from sklearn.model_selection import train_test_split

def split_data(x,crypto):
    x_train, x_test = train_test_split(x, test_size=0.30)
    #np.savetxt(str(crypto)+"_train_set.csv", x_train, delimiter=",")
    #np.savetxt(str(crypto)+"_test_set.csv", x_test, delimiter=",")
    return x_train,x_test 

dataset_all = pd.read_csv('./dataset.csv')

crypto = np.array(dataset_all['Cryptocurrency'])
crypto = np.unique(crypto)
losses = pd.DataFrame()
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
        data,bt_test = split_data(dataset,crypto[i])
        btc_loss,c_param, c2_param, l_param ,bt_net= btc_model.train(100,data,X)
        
        losses['btc_loss'] = btc_loss
        print('BTC Model Trained!!!')
    elif(crypto[i]=='ETH'):
        eth_model = nn.cryptic(crypto[i])
        data = split_data(dataset,crypto[i])
        eth_loss,eth_trained = eth_model.train(300,data,X)
        losses['eth_loss'] = eth_loss
        print('ETH Model Trained!!!')
    elif(crypto[i]=='DOGE'):
        doge_model = nn.cryptic(crypto[i])
        data = split_data(dataset,crypto[i])
        doge_loss,doge_trained = doge_model.train(300,data,X)
        losses['doge_loss'] = doge_loss
        print('DOGE Model Trained!!!')
    else:
        print('Invalid Crypto')



#btc_model.test(bt_test,bt_net)

    
