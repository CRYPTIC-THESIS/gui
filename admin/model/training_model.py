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
    print(len(x_train),len(x_test))
    return x_train

mod_type = ''
cryptic_model = nn.cryptic()
dataset_all = pd.read_csv('csv/dataset.csv')
if (dataset_all.shape[1] == 7):
    mod_type = 'full'
elif (dataset_all.shape[1] == 4):
    mod_type = 'half'
else:print('Invalid Dataset')

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

    if(mod_type == 'full'):
        dataset['Twitter'] = data['Twitter Volume']
        dataset['Reddit'] = data['Reddit Volume']
        dataset['Google'] = data['GoogleTrends']
    
    df = pd.DataFrame(columns = ['actual','open','24_high','24_low','google','twitter','reddit'])
    df['actual'] = data['Closing']
    df['open'] = data['Open']
    df['24_high'] = data['High']
    df['24_low'] = data['Low']

    if(mod_type == 'full'):
        df['google'] = data['GoogleTrends']
        df['twitter'] = data['Twitter Volume']
        df['reddit'] = data['Reddit Volume']

        da.corr_analysis(df, crypto[i])

    del df
    Y = np.array(data['Date'])
    
    dataset = np.array(dataset)
    c = dataset[3,0]
    d = c*0.005
    a = c+d
    b = c-d
    #print(dataset)

    if(crypto[i]=='BTC'):
        data = split_data(dataset,crypto[i])
        btc_loss= cryptic_model.train(100,data,a,b,crypto[i],mod_type)
        losses['btc_loss'] = btc_loss
        print('BTC Model Trained!!!\n\n')
        trained.append('BTC')
    elif(crypto[i]=='ETH'):
        data = split_data(dataset,crypto[i])
        eth_loss = cryptic_model.train(100,data,a,b,crypto[i],mod_type)
        losses['eth_loss'] = eth_loss
        print('ETH Model Trained!!!\n\n')
        trained.append('ETH')

    elif(crypto[i]=='DOGE'):
        data = split_data(dataset,crypto[i])
        doge_loss = cryptic_model.train(100,data,a,b,crypto[i],mod_type)
        losses['doge_loss'] = doge_loss
        print('DOGE Model Trained!!!\n\n')
        trained.append('DOGE')

    else:
        print('Invalid Crypto')

file_name = 'model/obj/trained.pkl'

open_file = open(file_name, "wb")
pickle.dump(trained, open_file)
open_file.close()
    
