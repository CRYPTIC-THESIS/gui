import numpy as np
import pickle as pl
import CRYPTIC_module as nn

cryptos = np.genfromtxt('trained_list.csv', delimiter=',')

for crypto in cryptos:
    data  = np.genfromtxt(crypto+"_test_set.csv", delimiter=',')
    model = nn.cryptic(crypto)
    model.test(data,crypto)
    

