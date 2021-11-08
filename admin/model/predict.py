import CRYPTIC_module as nn
import numpy as np
import pickle as pl
open_file = open('trained.pkl', "rb")
cryptos = pl.load(open_file)
open_file.close()

pred = np.zeros(14)
pred_list = np.zeros((len(cryptos),14))
data = 0
crypto = cryptos

x = 0
for crypto in cryptos:
    net = nn.cryptic(crypto)
    for i in range(14):
        last =  net.predict_crypto(data,crypto)
        data = last
        pred[i] = last
    pred_list[x] = pred
    x+=1
