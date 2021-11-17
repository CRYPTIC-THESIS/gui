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
import matplotlib.pyplot as plt

import sys 
sys.path.append('..')


def mape(actual, pred): 
    actual, pred = np.array(actual), np.array(pred)
    return np.mean(np.abs((actual - pred) / actual)) * 100


#For MAE - RMSE - R-Squared - MAPE
def error_analysis(crypto_df, crypto_name):
    # crypto_df = [btc_df,eth_df,doge_df]
    error_analysis_df = pd.DataFrame(columns = ['MAE','RMSE','R-Squared','Mape'])
    for df in crypto_df:
        #print(df)
        actualPrice = df['actual']
        predictedPrice = df['predicted']
        mae_res = mae(actualPrice, predictedPrice)
        rmse_res = sqrt(mse(actualPrice, predictedPrice))
        r2_res = r2(actualPrice, predictedPrice)
        mape_res = mape(actualPrice, predictedPrice)
        pd_data = pd.Series([mae_res , rmse_res, r2_res , mape_res], index=error_analysis_df.columns)
        error_analysis_df = error_analysis_df.append(pd_data,ignore_index=True)
    # crypto_name = ['BTC','ETH','DOGE']
    tbl_idx = pd.Index(crypto_name)
    error_analysis_df = error_analysis_df.set_index(tbl_idx)
    return error_analysis_df


#For Correlation Analysis
def corr_analysis(crypto_df,crypto):
    columns = ['actual','open','24_high','24_low','google','twitter','reddit']
    dataCorrelation=list(columns)
    corrMatrix = crypto_df[dataCorrelation].corr(method = 'pearson')
    
    sn.set(rc = {'figure.figsize':(7,5), 'figure.facecolor': '#21252B', 'xtick.color': 'white', 'ytick.color': 'white'})
    grph = sn.heatmap(corrMatrix, annot=True)
    fig = grph.get_figure()
    fig.savefig('images/'+crypto+'_corr.png', dpi=150, bbox_inches='tight')
    plt.close()
    
    # return corrMatrix, columns


# For Precision - Recall - F1-Score - Accuracy
def classification_analysis(crypto_df,crypto):
    #print(crypto_df)
    classification_analysis_df = pd.DataFrame(columns = ['Precision','Recall','F1-Score','Accuracy'])
    actualPrice = crypto_df[['actual']]
    predictedPrice = crypto_df[['predicted']]
    actualPriceDirection= [0]*(len(crypto_df)-1)
    predictedPriceDirection= [0]*(len(crypto_df)-1)
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
    

    #Print Confusion Matrix and Plot  
    cm = confusion_matrix(actualPriceDirection, predictedPriceDirection)
    group_names = ['True Neg','False Pos','False Neg','True Pos']
    group_counts = ["{0:0.0f}".format(value) for value in
                    cm.flatten()]
    group_percentages = ["{0:.2%}".format(value) for value in
                        cm.flatten()/np.sum(cm)]
    labels = [f"{v1}\n{v2}\n{v3}" for v1, v2, v3 in
            zip(group_names,group_counts,group_percentages)]
    labels = np.asarray(labels).reshape(2,2)
    
    sn.set(rc = {'figure.figsize':(7,5), 'figure.facecolor': '#21252B', 'xtick.color': 'white', 'ytick.color': 'white', 'axes.labelcolor': 'white', })
    # cmap = sn.diverging_palette(240, 10, n=4, center="dark", as_cmap=True)
    grph = sn.heatmap(cm, annot=labels, fmt='')
    
    plt.title('Price Direction (Increased or Decreased)', color='w')
    plt.yticks([0.5,1.5], ['Decreased', 'Increased'],va='center', weight = 'bold')
    plt.xticks([0.5,1.5], ['Decreased', 'Increased'],va='center', weight = 'bold')
    plt.ylabel('Actual Price')
    plt.xlabel('Predicted Price')
    plt.savefig('images/'+crypto+'_conf.png', dpi=150, bbox_inches='tight')
    plt.close()
    
    pd_data = pd.Series([prec_sco , rec_sco, f1_sco , acc_sco], index=classification_analysis_df.columns)
    classification_analysis_df = classification_analysis_df.append(pd_data,ignore_index=True)
    return classification_analysis_df
