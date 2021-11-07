import numpy as np
import layers as layer
import pickle as pl

def progress(count, total, status=''):
        bar_len = 60
        filled_len = int(round(bar_len * count / float(total)))

        percents = round(100.0 * count / float(total), 1)
        bar = '=' * filled_len + '-' * (bar_len - filled_len)
        print('[%s] %s%s ...%s\r' % (bar, percents, '%', status))

class cryptic():
    def __init__(self,crypto):
        self.network_name = crypto
    def format_LSTM(self,data):
        
        vals = set(data)
        vals_size = len(vals)
        print(vals_size)

        vals_to_idx = {w: i for i,w in enumerate(vals)}
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
                lstm.gradient_check(x_batch, y_batch, h_prev, c_prev, num_checks=10, delta=1e-7)

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

    def train(self,epochs,data,X,crypto):
        print('\n\nCRYPTIC NETWORK TRAINING\n')
        
        x = -2.1
        progress(0, epochs, status='Aral tayo')
        while(x>=X[0]+100)or(x<=X[0]-100):
            con = layer.Conv(5)
            con1 = layer.Conv(3)
            out = con.forward(data)
            out = layer.maxpool(out)
            out = con1.forward(out)
            out = layer.maxpool(out)
            x = out[0].astype(float)

        out = out.flatten()
        out = out.astype(int)
        vals_to_idx,idx_to_vals,vals,vals_size = self.format_LSTM(out)
        lstm = layer.LSTM(vals_to_idx, idx_to_vals, vals_size,epochs, lr = 0.01)
        J = []  # to store losses
        verbose = True
    
        num_batches = len(out) // lstm.seq_len
        X_trimmed = out[: num_batches * lstm.seq_len]  # trim input to have full sequences
        print('X_trimmed:',len(X_trimmed),'\nnum_batches:',num_batches)
        for epoch in range(epochs):

            J,h,c = self.LSTM_pass(lstm,epoch,verbose,X_trimmed,J)
            progress(epoch, epochs, status='Nag-aaral pa aku beh')
        net = [con,con1,lstm,h,c]
        progress(epochs, epochs, status='Kapagod mag-aral beh')

        
        filehandler = open(str(crypto)+'_con.obj', 'wb') 
        pl.dump(con, filehandler)
        filehandler = open(str(crypto)+'_con1.obj', 'wb') 
        pl.dump(con1, filehandler)
        filehandler = open(str(crypto)+'_lstm.obj', 'wb') 
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
        file = open(crypto+'_con.obj', 'rb') 
        con = pl.load(file)
        file = open(crypto+'_con1.obj', 'rb') 
        con1 = pl.load(file)
        file = open(crypto+'_lstm.obj', 'rb') 
        p_lstm = pl.load(file)

        out = con.forward(data)
        out = layer.maxpool(out)
        out = con1.forward(out)
        out = layer.maxpool(out)
        out = out.flatten()
        out = out.astype(int)

        vi = len(p_lstm.vals_to_idx)
        iv = len(p_lstm.idx_to_vals)

        i=0
        x=0
        for i in range(len(out)):
            print(i,len(out))
            if(out[i] in p_lstm.vals_to_idx):
                x+=1
                #print('existing:',p_lstm.vals_to_idx[out[i-1]])
            else:
                p_lstm.vals_to_idx[out[i]] = vi+i-x
                p_lstm.idx_to_vals[iv+i-x] = out[i]
                i+=1
        
        vals_size = len(p_lstm.vals_to_idx)

        lstm = self.init_trained(p_lstm.params,p_lstm.vals_to_idx,p_lstm.idx_to_vals,vals_size,p_lstm.epochs)

        verbose = False
    
        num_batches = len(out) // lstm.seq_len
        X_trimmed = out[: num_batches * lstm.seq_len]

        s = []         
        h_prev = np.zeros((lstm.n_h, 1))
        c_prev = np.zeros((lstm.n_h, 1))

        for j in range(0, len(X_trimmed) - lstm.seq_len, lstm.seq_len):
            # prepare batches
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
        print(out)
        print(s[-len(out):])
        
    
    def predict_crypto(self,network,input):
        #predict cryptocurrency up to 14 days

        #Initialize Model
        for i  in range(14):
            out = network[0].forward(input)
            out = layer.maxpool(out)
            out = network[1].forward(out)
            out = layer.maxpool(out)
            
            out = network[2].forward_step(out,network[3],network[4])
