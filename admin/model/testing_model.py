import numpy as np
import pickle as pl
import CRYPTIC_module as nn
import sys
import data_analysis as da
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

        if(crypto == 'BTC'):
            btc_df = df_data
        elif(crypto == 'ETH'):
            eth_df = df_data
        elif(crypto == 'DOGE'):
            doge_df = df_data
        else:
            print('Invalid Crypto')
    except:
        print('No '+str(crypto)+' Trained Model Found')
    
error_analysis_df = da.error_analysis(btc_df, eth_df, doge_df)

error_analysis_df.to_csv('csv/Error_Analysis.csv')




    

    

