import CRYPTIC_module as nn
import numpy as np
cryptos = np.zeros(3)
pred = np.zeros(14)
data = np.zeros(3)
crypto = cryptos
net = nn.cryptic()
for i in range(14):
    last =  net.predict_crypto(data,crypto)
    data = data[:2]
    data[3] = last
    pred[i] = last
