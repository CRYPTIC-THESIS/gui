import pandas as pd
import numpy as np
from sklearn.metrics import classification_report
from sklearn.metrics import mean_absolute_error as mae
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import r2_score as r2
from sklearn.metrics import precision_score as precision
from sklearn.metrics import recall_score as recall
from sklearn.metrics import f1_score as f1
from sklearn.metrics import accuracy_score as accuracy
from sklearn.metrics import confusion_matrix
from math import sqrt
import seaborn as sn

import sys 
sys.path.append('..')


def mape(actual, pred): 
    actual, pred = np.array(actual), np.array(pred)
    return np.mean(np.abs((actual - pred) / actual)) * 100


#For MAE - RMSE - R-Squared - MAPE
def error_analysis(btc_df, eth_df, doge_df):
    crypto_df = [btc_df,eth_df,doge_df]
    error_analysis_df = pd.DataFrame(columns = ['MAE','RMSE','R-Squared','Mape'])
    for df in crypto_df:
        actualPrice = pd.DataFrame(df[['actual']].values)
        predictedPrice = pd.DataFrame(df[['predicted']].values)
        mae_res = mae(actualPrice, predictedPrice)
        rmse_res = sqrt(mse(actualPrice, predictedPrice))
        r2_res = r2(actualPrice, predictedPrice)
        mape_res = mape(actualPrice, predictedPrice)
        pd_data = pd.Series([mae_res , rmse_res, r2_res , mape_res], index=error_analysis_df.columns)
        error_analysis_df = error_analysis_df.append(pd_data,ignore_index=True)
    crypto_name = ['BTC','ETH','DOGE']
    tbl_idx = pd.Index(crypto_name)
    error_analysis_df = error_analysis_df.set_index(tbl_idx)
    return error_analysis_df


#For Correlation Analysis
def corr_analysis(crypto_df):
    columns = ['actual','open','24_high','24_low','google','twitter','reddit']
    dataCorrelation=list(columns)
    corrMatrix = crypto_df[dataCorrelation].corr(method = 'pearson')
    
    sn.set(rc = {'figure.figsize':(7,5)})
    grph = sn.heatmap(corrMatrix, annot=True)
    fig = grph.get_figure()
    fig.savefig('images/corr.png', dpi=300)

    # return corrMatrix, columns


# For Precision - Recall - F1-Score - Accuracy
def classification_analysis(btc_df, eth_df, doge_df):
    crypto_df = [btc_df,eth_df,doge_df]
    classification_analysis_df = pd.DataFrame(columns = ['Precision','Recall','F1-Score','Accuracy'])
    for df in crypto_df:
        actualPrice = pd.DataFrame(df[['actual']].values)
        predictedPrice = pd.DataFrame(df[['predicted']].values)
        actualPriceDirection= [0]*(len(df)-1)
        predictedPriceDirection= [0]*(len(df)-1)
        currPrice = 0
        for index, row in actualPrice.iterrows():
            currPrice = row.values
            if (index!=0 and lastPrice<currPrice):
                actualPriceDirection[index-1] = 1
            elif (index!=0 and lastPrice>currPrice):
                actualPriceDirection[index-1] = 0
            lastPrice = row.values

        currPrice = 0
        for index, row in predictedPrice.iterrows():
            currPrice = row.values
            if (index!=0 and lastPrice<currPrice):
                predictedPriceDirection[index-1] = 1
            elif (index!=0 and lastPrice>currPrice):
                predictedPriceDirection[index-1] = 0
            lastPrice = row.values
        
        prec_sco = precision(actualPriceDirection,predictedPriceDirection)
        rec_sco = recall(actualPriceDirection,predictedPriceDirection)
        f1_sco = f1(actualPriceDirection,predictedPriceDirection)
        acc_sco = accuracy(actualPriceDirection,predictedPriceDirection)
        #Print Confusion Matrix    
        print(confusion_matrix(actualPriceDirection,predictedPriceDirection))    
        pd_data = pd.Series([prec_sco , rec_sco, f1_sco , acc_sco], index=classification_analysis_df.columns)
        classification_analysis_df = classification_analysis_df.append(pd_data,ignore_index=True)
    crypto_name = ['BTC','ETH','DOGE']
    tbl_idx = pd.Index(crypto_name)
    classification_analysis_df = classification_analysis_df.set_index(tbl_idx)
    return classification_analysis_df
        

# BTC_data = pd.read_csv("csv/BTC_Sample.csv")
# ETH_data = pd.read_csv("csv/ETH_Sample.csv")
# DOGE_data = pd.read_csv("csv/DOGE_Sample.csv")

# print(error_analysis(BTC_data,ETH_data,DOGE_data))
# print(corr_analysis(BTC_data))
# print(classification_analysis(BTC_data,ETH_data,DOGE_data))
