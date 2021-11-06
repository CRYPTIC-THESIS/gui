import numpy as np
import pickle as pl
import CRYPTIC_module as nn

open_file = open('trained.pkl', "rb")
trained_list = pl.load(open_file)
open_file.close()


for crypto in trained_list:
    print("\n\nTesting "+str(crypto)+"model...")
    data  = np.genfromtxt(str(crypto)+"_test_set.csv", delimiter=',')
    model = nn.cryptic(crypto)
    model.test(data,crypto)
    

