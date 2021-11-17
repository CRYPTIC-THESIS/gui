# ------------------------------------------------------------------------------------------- #
#    CRYPTIC: AN IMPROVED CNN-LSTM CRYPTOCURRENCY PRICE FORECASTING USING INTERNET TRENDS
# 
# Authors:
# Arconado, Kristine N.             Dalay, Jeremy Tristen A.
# Berse, Nikko R.                   Faustino, Kyle C.
# 
# BSCS 4-2 AY 2021-2022
# ------------------------------------------------------------------------------------------- #

import numpy as np
import pandas as pd
import layers as layer
import pickle as pl
import matplotlib.pyplot as plt
import sys
from datetime import datetime
from datetime import timedelta
sys.path.append('..')

def progress(count, total, status=''):
        bar_len = 60
        filled_len = int(round(bar_len * count / float(total)))

        percents = round(100.0 * count / float(total), 1)
        bar = '=' * filled_len + '-' * (bar_len - filled_len)
        print('[%s] %s%s ...%s\r' % (bar, percents, '%', status))

class cryptic():
    def format_LSTM(self,data):
        
        vals = set(data)
        vals_size = len(vals)

        vals_to_idx = {w: i for i,w in enumerate(vals)} #{'vals':1,.....}
        idx_to_vals = {i: w for i,w in enumerate(vals)} 
 
        return vals_to_idx,idx_to_vals,vals,vals_size

    def LSTM_pass(self,lstm,epoch,verbose,X_trimmed,J):
        s = []         
        h_prev = np.zeros((lstm.n_h, 1))
        c_prev = np.zeros((lstm.n_h, 1))

        for j in range(0, len(X_trimmed) - lstm.seq_len, lstm.seq_len):
            # prepare batches
            x_batch = [lstm.vals_to_idx[ch] for ch in X_trimmed[j: j + lstm.seq_len]]
            y_batch = [lstm.vals_to_idx[ch] for ch in X_trimmed[j + 1: j + lstm.seq_len + 1]]

            loss, h_prev, c_prev = lstm.forward_backward(x_batch, y_batch, h_prev, c_prev)

            # smooth out loss and store in list
            lstm.smooth_loss = lstm.smooth_loss * 0.999 + loss * 0.001
            J.append(lstm.smooth_loss)

            # check gradients
            if epoch == 0 and j == 0:
                try:
                    lstm.gradient_check(x_batch, y_batch, h_prev, c_prev, num_checks=10, delta=1e-7)
                except AssertionError as msg:
                    print(msg)
            lstm.clip_grads()

            batch_num = epoch * lstm.epochs + j / lstm.seq_len + 1
            lstm.update_params(batch_num)

            # print out loss and sample string
            if verbose:
                if j % 400000 == 0:
                    print('Epoch:', epoch, '\tBatch:', j, "-", j + lstm.seq_len,'\tLoss:', round(lstm.smooth_loss, 2))
                    #s = lstm.sample(h_prev, c_prev, lstm.seq_size+1)
                    #print(s, "\n")

        return J,h_prev, c_prev  #,s

    def train(self,epochs,data,a,b,crypto,model_type):
        print('\n\nCRYPTIC NETWORK TRAINING\n')
        x = -100
        
        progress(0, epochs+1, status='Initializing Model')
        if(model_type == 'full'):
            f1 = 2
            f2 = 1
        else:
            f1 = 5
            f2 = 1

        while (x>=a)or(x<=b):
            
            con = layer.Conv(f1)
            con1 = layer.Conv(f2)
            pool = layer.MaxPool()
            out = con.forward(data)
            out = pool.forward(out)
            out = con1.forward(out)
            out = pool.forward(out)
            x = float(out[-1])
            
        progress(0.25, epochs+1, status='Convolutions Done')
        out = out.flatten()
        
        vals_to_idx,idx_to_vals,vals,vals_size = self.format_LSTM(out)
        lstm = layer.LSTM(vals_to_idx, idx_to_vals, vals_size,epochs, lr = 0.01)
        progress(0.5, epochs+1, status='Passing to LSTM')
        J = []  # to store losses
        verbose = True
    
        num_batches = len(out) // lstm.seq_len
        X_trimmed = out[: num_batches * lstm.seq_len]  # trim input to have full sequences
       
        for epoch in range(epochs):

            J,h,c = self.LSTM_pass(lstm,epoch,verbose,X_trimmed,J)
            progress(epoch+1, epochs+1, status='Wow! New knowledge Obtained')
        
        progress(epochs+1, epochs+1, status='I feel smarter already')

        print('Total Data Tested: ',len(out))
        print('Final Loss During Training: ',J[-1])
        filehandler = open('model/obj/'+str(crypto)+'_con.obj', 'wb') 
        pl.dump(con, filehandler)
        filehandler = open('model/obj/'+str(crypto)+'_con1.obj', 'wb') 
        pl.dump(con1, filehandler)
        filehandler = open('model/obj/'+str(crypto)+'_lstm.obj', 'wb') 
        pl.dump(lstm, filehandler)

        return J

    def init_trained(self,l_param,vals_to_idx,idx_to_vals,vals_size,epochs):
        lstm = layer.LSTM(vals_to_idx, idx_to_vals, vals_size,epochs, lr = 0.01)

        #print(len(lstm.params['Wv'][0]),len(l_param['Wv'][0]))
        
        for key in lstm.params:
            
            if (key == 'Wv') or (key == 'bv'):
                for i in range (len(l_param[key])):
                    lstm.params[key][i] = l_param[key][i]
                
            else:
                for i in range(len(lstm.params[key])):
                    lstm.params[key][i][:len(l_param[key][i])] = l_param[key][i]

        return lstm


    def test(self,data,crypto): 
        progress(0, len(data)+1, status='Loading Trained Model')
        file = open('model/obj/'+crypto+'_con.obj', 'rb') 
        con = pl.load(file)
        file = open('model/obj/'+crypto+'_con1.obj', 'rb') 
        con1 = pl.load(file)
        pool = layer.MaxPool()
        
        file = open('model/obj/'+crypto+'_lstm.obj', 'rb') 
        p_lstm = pl.load(file)
        progress(0.5, len(data)+1, status='Trained Model Loaded')
        out = con.forward(data)
        out = pool.forward(out)
        out = con1.forward(out)
        out = pool.forward(out)
        out = out.flatten()
        

        vi = len(p_lstm.vals_to_idx)
        iv = len(p_lstm.idx_to_vals)

        i=0
        x=0
        for i in range(len(out)):
            if(out[i] in p_lstm.vals_to_idx):
                x+=1
                #print('existing:',p_lstm.vals_to_idx[out[i-1]])
            else:
                p_lstm.vals_to_idx[out[i]] = vi+i-x
                p_lstm.idx_to_vals[iv+i-x] = out[i]
                i+=1
        
        vals_size = len(p_lstm.vals_to_idx)
        progress(0.7, len(data)+1, status='Preparing Dataset')
        lstm = self.init_trained(p_lstm.params,p_lstm.vals_to_idx,p_lstm.idx_to_vals,vals_size,p_lstm.epochs)
        progress(0.9, len(data)+1, status='Model Initialized')
        verbose = False
    
        num_batches = len(out) // lstm.seq_len
        X_trimmed = out[: num_batches * lstm.seq_len]

        s = []         
        h_prev = np.zeros((lstm.n_h, 1))
        c_prev = np.zeros((lstm.n_h, 1))

        for j in range(0, len(X_trimmed) - lstm.seq_len, lstm.seq_len):
            # prepare batches
            progress(j+1, len(data)+1, status='Testing')
            x_batch = [lstm.vals_to_idx[ch] for ch in X_trimmed[j: j + lstm.seq_len]]
            y_batch = [lstm.vals_to_idx[ch] for ch in X_trimmed[j + 1: j + lstm.seq_len + 1]]

            x, z = {}, {}
            f, i, c_bar, c, o = {}, {}, {}, {}, {}
            y_hat, v, h = {}, {}, {}

            # Values at t= - 1
            h[-1] = h_prev
            c[-1] = c_prev

            for t in range(lstm.seq_len):
                x[t] = np.zeros((lstm.seq_size, 1))
                x[t][x_batch[t]] = 1

                y_hat[t], v[t], h[t], o[t], c[t], c_bar[t], i[t], f[t], z[t] = \
                    lstm.forward_step(x[t], h[t - 1], c[t - 1])
            s = lstm.sample(h_prev, c_prev, lstm.seq_size)
        pred = s[-(len(out)-1):]
        predx = [i for i in range(len(pred))]
        outx = [i for i in range(len(out))]
        progress(len(data)+1, len(data)+1, status='Done Testing')
        print('Actual : ',out[1:])
        print('Predicted: ',pred)

        df = pd.DataFrame(columns=['actual','predicted'])
        df['actual'] = pd.Series(out[1:])
        df['predicted'] = pd.Series(pred)

        return df

    def retrain(self,epochs,data,crypto,end):
        date = []
        begin = datetime.strptime(str(end), "%Y-%m-%d")
        file = open('model/obj/'+crypto+'_con.obj', 'rb') 
        con = pl.load(file)
        file = open('model/obj/'+crypto+'_con1.obj', 'rb') 
        con1 = pl.load(file)
        pool = layer.MaxPool()
        file = open('model/obj/'+crypto+'_lstm.obj', 'rb') 
        p_lstm = pl.load(file)

        out = con.forward(data)
        out = pool.forward(out)
        out = con1.forward(out)
        out = pool.forward(out)
        out = out.flatten()
        
        for i in range(14):
            progress(i, 14, status='Retraining')
            vi = len(p_lstm.vals_to_idx)
            iv = len(p_lstm.idx_to_vals)

            i=0
            x=0
            for i in range(len(out)):
                if(out[i] in p_lstm.vals_to_idx):
                    x+=1
                    #print('existing:',p_lstm.vals_to_idx[out[i-1]])
                else:
                    p_lstm.vals_to_idx[out[i]] = vi+i-x
                    p_lstm.idx_to_vals[iv+i-x] = out[i]
                    i+=1
            
            vals_size = len(p_lstm.vals_to_idx)
            lstm = self.init_trained(p_lstm.params,p_lstm.vals_to_idx,p_lstm.idx_to_vals,vals_size,p_lstm.epochs)

            J = []  # to store losses
            verbose = False
        
            num_batches = len(out) // lstm.seq_len
            X_trimmed = out[: num_batches * lstm.seq_len]  # trim input to have full sequences
        
            for epoch in range(epochs):
                J,h,c = self.LSTM_pass(lstm,epoch,verbose,X_trimmed,J)
            # print('Loss: ',J[-1])
            s = lstm.sample(h, c, lstm.seq_size)
            pred = s[-1]

            out = np.append(out,[pred])

            p_lstm = lstm
            day = begin + timedelta(days=1)
            date.append(str(day))
            begin = day

        progress(14, 14, status='Finished Retraining')
        print('Sending Predictions to Database')
        
        s = lstm.sample(h, c, lstm.seq_size)
        pred = s[-14:]

        return date,pred




            

            