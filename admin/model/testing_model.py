import numpy as np
import pickle as pl
import CRYPTIC_module as nn
import sys
sys.path.append('..')

open_file = open('model/obj/trained.pkl', "rb")
trained_list = pl.load(open_file)
open_file.close()


for crypto in trained_list:
    print("\n\nTesting "+str(crypto)+" model...")
    data  = np.genfromtxt('csv/'+str(crypto)+"_test_set.csv", delimiter=',')
    model = nn.cryptic()
    pred,actual = model.test(data,crypto)
    
    

