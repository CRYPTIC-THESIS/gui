import numpy as np
import layers as layer
import pandas as pd


class cryptic():
    def __init__(self,crypto):
        self.network_name = crypto
    def format_LSTM(self,data):
        
        vals = set(data)
        vals_size = len(vals)

        vals_to_idx = {w: i for i,w in enumerate(vals)}
        idx_to_vals = {i: w for i,w in enumerate(vals)}
 
        return vals_to_idx,idx_to_vals,vals,vals_size

    def LSTM_pass(self,lstm,epoch,verbose,X_trimmed,J):
                
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
                    s = lstm.sample(h_prev, c_prev, sample_size=250)
                    print(s, "\n")

        return J,h_prev, c_prev

    def train(self,epochs,data,X):
        print('CRYPTIC NETWORK TRAINING\n\n')
        con = layer.Conv(5)
        con1 = layer.Conv(3)
        
        out = con.forward(data)
        out = layer.maxpool(out)
        out = con1.forward(out)
        out = layer.maxpool(out)
        out = out.flatten()
        vals_to_idx,idx_to_vals,vals,vals_size = self.format_LSTM(out)
        lstm = layer.LSTM(vals_to_idx, idx_to_vals, vals_size, epochs, lr = 0.01)
        J = []  # to store losses
        verbose = True
    
        num_batches = len(out) // lstm.seq_len
        X_trimmed = out[: num_batches * lstm.seq_len]  # trim input to have full sequences
        print('X_trimmed:',len(X_trimmed),'\nnum_batches:',num_batches)
        for epoch in range(epochs):

            J,h,c = self.LSTM_pass(lstm,epoch,verbose,X_trimmed,J)
            
            net = [con,con1,lstm,h,c]

        return J,con.filters,con1.filters,lstm.params,net

    def test(self,data,network):

        out = network[0].forward(data)
        out = layer.maxpool(out)
        out = network[1].forward(out)
        out = layer.maxpool(out)
        out = out.flatten()

        vi = len(network[2].vals_to_idx)
        iv = len(network[2].idx_to_vals)
        
        for i in range(1,len(out)+1):
            if(out[i-1] in network[2].vals_to_idx):
                i -= 1
                #print('existing:',network[2].vals_to_idx[out[i-1]])
            else:
                network[2].vals_to_idx[out[i-1]] = vi+i
                network[2].idx_to_vals[iv+i] = out[i-1]
                #print('added')
        #print(network[2].params['Wf'][-1][-1])
        data_a = [network[2].vals_to_idx[ch] for ch in out]
        for data in data_a:
            h_prev = network[3][-1]
            c_prev = network[4][-1]
            z = np.row_stack((h_prev,data))
            
            f = network[2].sigmoid(np.dot(network[2].params["Wf"][-1][-1], z) + network[2].params["bf"][-1][-1])
            i = network[2].sigmoid(np.dot(network[2].params["Wi"][-1][-1], z) + network[2].params["bi"][-1][-1])
            c_bar = np.tanh(np.dot(network[2].params["Wc"][-1][-1], z) + network[2].params["bc"][-1][-1])

            c = f * c_prev + i * c_bar
            o = network[2].sigmoid(np.dot(network[2].params["Wo"][-1][-1], z) + network[2].params["bo"][-1][-1])
            h = o * np.tanh(c)

            v = np.dot(network[2].params["Wv"][-1][-1], h) + network[2].params["bv"][-1][-1]
            
            y_hat = network[2].softmax(v)
            h_prev = h[-1]
            c_prev = c[-1]
            print(-np.log(y_hat))
        '''
        pred = []
        actual = []
        out = network[0].forward(data)
        out = layer.maxpool(out)
        out = network[1].forward(out)
        out = layer.maxpool(out)
        data_a = out.flatten()
        J = []  # to store losses
        verbose = True
        vi = len(network[2].vals_to_idx)
        iv = len(network[2].idx_to_vals)
        
        for i in range(1,len(data_a)+1):
            if(data_a[i-1] in network[2].vals_to_idx):
                i -= 1
                #print('existing:',network[2].vals_to_idx[data_a[i-1]])
            else:
                network[2].vals_to_idx[data_a[i-1]] = vi+i
                network[2].idx_to_vals[iv+i] = data_a[i-1]
                #print('added')

        num_batches = len(data_a) // network[2].seq_len
        X_trimmed = data_a[: num_batches * network[2].seq_len]
        h_prev = np.zeros((network[2].n_h, 1))
        c_prev = np.zeros((network[2].n_h, 1))
        network[2].seq_size = len(network[2].vals_to_idx)

        for j in range(0, len(X_trimmed) - network[2].seq_len, network[2].seq_len):
            # prepare batches
            x_batch = [network[2].vals_to_idx[ch] for ch in X_trimmed[j: j + network[2].seq_len]]
            y_batch = [network[2].vals_to_idx[ch] for ch in X_trimmed[j + 1: j + network[2].seq_len + 1]]

            x, z = {}, {}
            f, i, c_bar, c, o = {}, {}, {}, {}, {}
            y_hat, v, h = {}, {}, {}

            # Values at t= - 1
            h[-1] = network[3]
            c[-1] = network[4]

            loss = 0
            for t in range(network[2].seq_len):
                x[t] = np.zeros((network[2].seq_size, 1))
                x[t][x_batch[t]] = 1

                y_hat[t], v[t], h[t], o[t], c[t], c_bar[t], i[t], f[t], z[t] = \
                    network[2].forward_step(x[t], h[t - 1], c[t - 1])

                loss += -np.log(y_hat[t][y_batch[t], 0])
                network[3] = h[-1]
                network[4] = c[-1] 
                print('Loss:',loss)'''

    def test_v(self,c_param,c2_param,l_param,data):
        con = layer.Conv(5)
        con1 = layer.Conv(3)
        con.filters = c_param
        con1.filters = c2_param

        out = con.forward(data)
        
        out = layer.maxpool(out)
        out = con1.forward(out)
        out = layer.maxpool(out)
        out = out.flatten()
        vals_to_idx,idx_to_vals,vals,vals_size = self.format_LSTM(out)
        lstm = layer.LSTM(vals_to_idx, idx_to_vals, vals_size, epochs=1, lr = 0.01)

        lstm.params = l_param

        J = []  # to store losses
        verbose = False
    
        num_batches = len(out) // lstm.seq_len
        X_trimmed = out[: num_batches * lstm.seq_len]
        h_prev = np.zeros((lstm.n_h, 1))
        c_prev = np.zeros((lstm.n_h, 1))
        lstm.seq_size = len(lstm.vals_to_idx)

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

            loss = 0
            for t in range(lstm.seq_len):
                x[t] = np.zeros((lstm.seq_size, 1))
                x[t][x_batch[t]] = 1

                y_hat[t], v[t], h[t], o[t], c[t], c_bar[t], i[t], f[t], z[t] = \
                    lstm.forward_step(x[t], h[t - 1], c[t - 1])

                loss += -np.log(y_hat[t][y_batch[t], 0])
                h_prev = h[-1]
                c_prev = c[-1] 
                print('Loss:',loss)



            
    def predict_crypto(self,network,input):
        #predict cryptocurrency up to 14 days

        #Initialize Model
        for i  in range(14):
            out = network[0].forward(input)
            out = layer.maxpool(out)
            out = network[1].forward(out)
            out = layer.maxpool(out)
            
            out = network[2].forward_step(out,network[3],network[4])
