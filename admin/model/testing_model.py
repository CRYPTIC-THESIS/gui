import numpy as np
import pickle as pl
import CRYPTIC_module as nn
import sys
import data_analysis as da
import pandas as pd
sys.path.append('..')

open_file = open('model/obj/trained.pkl', "rb")
trained_list = pl.load(open_file)
open_file.close()
btc_df = pd.DataFrame()
eth_df = pd.DataFrame()
doge_df = pd.DataFrame()

for crypto in trained_list:
    print("\n\nTesting "+str(crypto)+" model...")
    try:
        data  = np.genfromtxt('csv/'+str(crypto)+"_test_set.csv", delimiter=',')
        model = nn.cryptic()
        df_data = model.test(data,crypto)
        
        try:
            classi_analysis = da.classification_analysis(df_data, str(crypto))
            classi_analysis.to_csv('csv/'+str(crypto)+'_classification_analysis.csv')
        except Exception:
            pass

        if(crypto == 'BTC'):
            btc_df = df_data
        elif(crypto == 'ETH'):
            eth_df = df_data
        elif(crypto == 'DOGE'):
            doge_df = df_data
        else:
            print('Invalid Crypto')
    except Exception:
        pass
        
crypto_df = list()
crypto_name = list()

if btc_df.empty == False:
    crypto_df.append(btc_df)
    crypto_name.append('BTC')

if eth_df.empty == False:
    crypto_df.append(eth_df)
    crypto_name.append('ETH')

if doge_df.empty == False:
    crypto_df.append(doge_df)
    crypto_name.append('DOGE')

error_analysis_df = da.error_analysis(crypto_df, crypto_name)

error_analysis_df.to_csv('csv/All_Error_Analysis.csv')