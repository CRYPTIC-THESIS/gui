import numpy as np
import pickle as pl
import CRYPTIC_module as nn

cryptos = np.genfromtxt('trained_list.csv', delimiter=',')

for crypto in cryptos:
    print("\n\nTesting "+str(crypto)+"model...")
    data  = np.genfromtxt(str(crypto)+"_test_set.csv", delimiter=',')
    model = nn.cryptic(crypto)
    model.test(data,crypto)
    

