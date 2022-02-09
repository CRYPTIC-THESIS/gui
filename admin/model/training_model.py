import pandas as pd
import numpy as np
import CRYPTIC_module as nn
import data_analysis as da
import sys 
import pickle
sys.path.append('..')

from sklearn.model_selection import train_test_split

def split_data(x,crypto):
    x_train, x_test = train_test_split(x, test_size=0.30)
    np.savetxt('csv/'+str(crypto)+"_train_set.csv", x_train, delimiter=",")
    np.savetxt('csv/'+str(crypto)+"_test_set.csv", x_test, delimiter=",")
    return x_train

mod_type = ''
cryptic_model = nn.cryptic()
dataset_all = pd.read_csv('csv/dataset.csv')

if (dataset_all.shape[1] == 7):
    mod_type = 'half'
else:mod_type = 'full'

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
    dataset['Close'] = data['Close']

    if(mod_type == 'full'):
        dataset['Twitter'] = data['Twitter']
        dataset['Reddit'] = data['Reddit']
        dataset['Google'] = data['GoogleTrends']
    
    df = pd.DataFrame(columns = ['actual','open','24_high','24_low','google','twitter','reddit'])
    df['actual'] = data['Close']
    df['open'] = data['Open']
    df['24_high'] = data['High']
    df['24_low'] = data['Low']

    da.corr_analysis(df, crypto[i])

    if(mod_type == 'full'):
        df['google'] = data['GoogleTrends']
        df['twitter'] = data['Twitter']
        df['reddit'] = data['Reddit']

        da.corr_analysis(df, crypto[i])

    # del df
    Y = np.array(data['Date'])
    
    dataset = np.array(dataset)
    l = dataset[-1:]
    c = l[0][3]
    d = c*0.01
    a = c+d
    b = c-d
    
    if(crypto[i]=='BTC'):
        data = split_data(dataset,crypto[i])
        c = data[-1][3]
        d = c*0.01
        a = c+d
        b = c-d
        btc_loss= cryptic_model.train(200,data,a,b,crypto[i],mod_type)
        losses['btc_loss'] = btc_loss
        print('BTC Model Trained!!!\n\n')
        trained.append('BTC')
    elif(crypto[i]=='ETH'):
        data = split_data(dataset,crypto[i])
        c = data[-1][3]
        d = c*0.01
        a = c+d
        b = c-d
        eth_loss = cryptic_model.train(200,data,a,b,crypto[i],mod_type)
        losses['eth_loss'] = eth_loss
        print('ETH Model Trained!!!\n\n')
        trained.append('ETH')

    elif(crypto[i]=='DOGE'):
        data = split_data(dataset,crypto[i])
        c = data[-1][3]
        d = c*0.01
        a = c+d
        b = c-d
        doge_loss = cryptic_model.train(200,data,a,b,crypto[i],mod_type)
        losses['doge_loss'] = doge_loss
        print('DOGE Model Trained!!!\n\n')
        trained.append('DOGE')

    else:
        print('Invalid Crypto')

file_name = 'model/obj/trained.pkl'

open_file = open(file_name, "wb")
pickle.dump(trained, open_file)
open_file.close()

