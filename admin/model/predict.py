import CRYPTIC_module as nn
import numpy as np
import pickle as pl
open_file = open('trained.pkl', "rb")
cryptos = pl.load(open_file)
open_file.close()

pred = np.zeros(14)
pred_list = np.zeros((len(cryptos),14))
data = np.zeros(3)
crypto = cryptos
net = nn.cryptic()
x = 0
for crypto in cryptos:
    for i in range(14):
        last =  net.predict_crypto(data,crypto)
        data = data[:2]
        data[3] = last
        pred[i] = last
    pred_list[x] = pred
    x+=1
