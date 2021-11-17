import numpy as np
from numpy.core.fromnumeric import argmax
import pandas as pd
from random import uniform

class Conv:
    
    def __init__(self, num_filters):
        self.num_filters = num_filters
        self.filters = np.random.randn(num_filters, 1, 3)/3
            
    def iterate_regions(self, image):
        #generates all possible 3*3 image regions using valid padding
        
        h,w = image.shape
        
        for i in range(h):
            for j in range(w-2):
                im_region = image[i:(i+1), j:(j+3)]
                yield im_region, i, j
                
    def forward(self, input):
        self.last_input = input
        
        h,w = input.shape
        
        output = np.zeros((h, w-2, self.num_filters))
        
        for im_regions, i, j in self.iterate_regions(input):
            output[i, j] = np.sum(im_regions * self.filters, axis=(1,2))
        return output
    
    def backprop(self, d_l_d_out, learn_rate):
        '''
        Performs a backward pass of the conv layer.
        - d_L_d_out is the loss gradient for this layer's outputs.
        - learn_rate is a float.
        '''
        d_l_d_filters = np.zeros(self.filters.shape)

        for im_region, i, j in self.iterate_regions(self.last_input):
            for f in range(self.num_filters):
                d_l_d_filters[f] += d_l_d_out[i,j,f] * im_region

        #update filters
        self.filters -= learn_rate * d_l_d_filters

        return None
class MaxPool:
    def iterate_regions(self, image):
        h, w, _ = image.shape
        
        new_h = h // 1
        new_w = w // 2
        
        for i in range(new_h):
            for j in range(new_w):
                im_region = image[(i):(i+1), (j):(j+2)]
                yield im_region, i, j
                
    def forward(self, input):
        
        self.last_input = input
        
        h, w, num_filters = input.shape
        output = np.zeros((h//1, w//2, num_filters))
        
        for im_region, i, j in self.iterate_regions(input):
            output[i,j] = np.amax(im_region,axis=(0,1))
        output = output.reshape(output.shape[0], (output.shape[1]*output.shape[2]))
        return output
    
    def backprop(self, d_l_d_out):
        '''
        Performs a backward pass of the maxpool layer.
        Returns the loss gradient for this layer's inputs.
        - d_L_d_out is the loss gradient for this layer's outputs.
        '''
        d_l_d_input = np.zeros(self.last_input.shape)

        for im_region, i, j in self.iterate_regions(self.last_input):
            h, w, f = im_region.shape
            amax = np.amax(im_region, axis=(0,1))

            for i2 in range(h):
                for j2 in range(w):
                    for f2 in range(f):
                        #if the pixel was the max value, copy the gradient to it
                        if(im_region[i2,j2,f2] == amax[f2]):
                            d_l_d_input[i*2+i2, j*2+j2 ,f2] = d_l_d_out[i, j, f2]
                            break;
        return d_l_d_input

class LSTM:
    def __init__(self, value_to_idx, idx_to_value, seq_size, epochs, n_h=100, seq_len=1, lr=0.001, beta1=0.9, beta2=0.999):
        """
        Implementation of simple character-level LSTM using Numpy
        """
        self.layer_name = 'LSTM Block'
        self.vals_to_idx = value_to_idx  # characters to indices mapping
        self.idx_to_vals = idx_to_value  # indices to characters mapping
        self.seq_size = seq_size  # no. of unique characters in the training data
        self.n_h = n_h  # no. of units in the hidden layer
        self.seq_len = seq_len  # no. of time steps, also size of mini batch
        self.epochs = epochs  # no. of training iterations
        self.lr = lr  # learning rate
        self.beta1 = beta1  # 1st momentum parameter
        self.beta2 = beta2  # 2nd momentum parameter

        # -----initialise weights and biases-----#
        self.params = {}
        std = (1.0 / np.sqrt(self.seq_size + self.n_h))  # Xavier initialisation

        # forget gate
        self.params["Wf"] = np.random.randn(self.n_h, self.n_h + self.seq_size) * std
        self.params["bf"] = np.ones((self.n_h, 1))

        # input gate
        self.params["Wi"] = np.random.randn(self.n_h, self.n_h + self.seq_size) * std
        self.params["bi"] = np.zeros((self.n_h, 1))

        # cell gate
        self.params["Wc"] = np.random.randn(self.n_h, self.n_h + self.seq_size) * std
        self.params["bc"] = np.zeros((self.n_h, 1))

        # output gate
        self.params["Wo"] = np.random.randn(self.n_h, self.n_h + self.seq_size) * std
        self.params["bo"] = np.zeros((self.n_h, 1))

        # output
        self.params["Wv"] = np.random.randn(self.seq_size, self.n_h) * \
                            (1.0 / np.sqrt(self.seq_size))
        self.params["bv"] = np.zeros((self.seq_size, 1))

        # -----initialise gradients and Adam parameters-----#
        self.grads = {}
        self.adam_params = {}

        for key in self.params:
            self.grads["d" + key] = np.zeros_like(self.params[key])
            self.adam_params["m" + key] = np.zeros_like(self.params[key])
            self.adam_params["v" + key] = np.zeros_like(self.params[key])

        self.smooth_loss = -np.log(1.0 / self.seq_size) * self.seq_len
        return

    def sigmoid(self, x):
        """
        Smoothes out values in the range of [0,1]
        """
        return 1 / (1 + np.exp(-x))

    def relu(self,X):
        out = np.maximum(X, 0)
        cache = X
        return out, cache

    def relu_b(self,dout, cache):
        dX = dout.copy()
        dX[cache <= 0] = 0
        return dX
    
    def dropout(self,X, p_dropout):
        u = np.random.binomial(1, p_dropout, size=X.shape) / p_dropout
        out = X * u
        cache = u
        return out, cache


    def dropout_b(self,dout, cache):
        dX = dout * cache
        return dX

    def softmax(self, x):
        """
        Normalizes output into a probability distribution
        """
        e_x = np.exp(x - np.max(x))  # max(x) subtracted for numerical stability
        return e_x / np.sum(e_x)
    
    def batchnorm(self,x, gamma, beta,param):
        mode = param['mode']
        eps = param.get('eps', 1e-5)
        momentum = param.get('momentum', 0.9)

        N, D = x.shape
        running_mean = param.get('running_mean', np.zeros(D, dtype=x.dtype))
        running_var = param.get('running_var', np.zeros(D, dtype=x.dtype))

        if mode == 'train':
            sample_mean = x.mean(axis=0)
            sample_var = x.var(axis=0)
            
            running_mean = momentum * running_mean + (1 - momentum) * sample_mean
            running_var = momentum * running_var + (1 - momentum) * sample_var
            
            std = np.sqrt(sample_var + eps)
            x_centered = x - sample_mean
            x_norm = x_centered / std
            out = gamma * x_norm + beta
            
            cache = (x_norm, x_centered, std, gamma)
            
        elif mode == 'test':
            x_norm = (x - running_mean) / np.sqrt(running_var + eps)
            out = out = gamma * x_norm + beta
        
        else:
            raise ValueError('Invalid forward batchnorm mode "%s"' % mode)

        # Store the updated running means back into param
        param['running_mean'] = running_mean
        param['running_var'] = running_var

        return out, cache

    def batchnorm_b(self,dout, cache):
        
        N = dout.shape[0]
        x_norm, x_centered, std, gamma = cache
        
        dgamma = (dout * x_norm).sum(axis=0)
        dbeta = dout.sum(axis=0)
        
        dx_norm = dout * gamma
        dx = 1/N / std * (N * dx_norm - 
                        dx_norm.sum(axis=0) - 
                        x_norm * (dx_norm * x_norm).sum(axis=0))
        return dx, dgamma, dbeta

    def clip_grads(self):
        """
        Limits the magnitude of gradients to avoid exploding gradients
        """
        for key in self.grads:
            np.clip(self.grads[key], -5, 5, out=self.grads[key])
        return

    def reset_grads(self):
        """
        Resets gradients to zero before each backpropagation
        """
        for key in self.grads:
            self.grads[key].fill(0)
        return

    def update_params(self, batch_num):
        """
        Updates parameters with Adam
        """
        for key in self.params:
            self.adam_params["m" + key] = self.adam_params["m" + key] * self.beta1 + \
                                          (1 - self.beta1) * self.grads["d" + key]
            self.adam_params["v" + key] = self.adam_params["v" + key] * self.beta2 + \
                                          (1 - self.beta2) * self.grads["d" + key] ** 2

            m_correlated = self.adam_params["m" + key] / (1 - self.beta1 ** batch_num)
            v_correlated = self.adam_params["v" + key] / (1 - self.beta2 ** batch_num)
            self.params[key] -= self.lr * m_correlated / (np.sqrt(v_correlated) + 1e-8)
        return

    def sample(self, h_prev, c_prev, sample_size):
        """
        Outputs a sample sequence from the model
        """
        x = np.zeros((self.seq_size,1))
        h = h_prev
        c = c_prev
        pred = np.zeros(sample_size)
        
        for t in range(sample_size):
            y_hat, _, h, _, c, _, _, _, _ = self.forward_step(x, h, c)

            # get a random index within the probability distribution of y_hat(ravel())
            idx = np.random.choice(range(self.seq_size), p=y_hat.ravel())
            #idx = np.argmax(y_hat)
            x = np.zeros((self.seq_size, 1))
            x[idx] = 1

            # find the char with the sampled index and concat to the output string
            val = self.idx_to_vals[idx]
            pred[t] = val
        return pred

    def forward_step(self, x, h_prev, c_prev):
        """
        Implements the forward propagation for one time step
        """

        z = np.row_stack((h_prev, x))

        f = self.sigmoid(np.dot(self.params["Wf"], z) + self.params["bf"])
        i = self.sigmoid(np.dot(self.params["Wi"], z) + self.params["bi"])
        c_bar = np.tanh(np.dot(self.params["Wc"], z) + self.params["bc"])

        c = f * c_prev + i * c_bar
        o = self.sigmoid(np.dot(self.params["Wo"], z) + self.params["bo"])
        h = o * np.tanh(c)

        v = np.dot(self.params["Wv"], h) + self.params["bv"]

        out,ca_re = self.relu(v)
        N, D = out.shape
        gamma = np.random.randn(D)
        beta = np.random.randn(D)
        dout = np.random.randn(N, D)
        gamma1 = np.random.randn(D)
        beta1 = np.random.randn(D)
        dout1 = np.random.randn(N, D)
        bn_param = {'mode': 'train'}
        bn_param1 = {'mode': 'train'}
        out,ca_bn = self.batchnorm(out, gamma, beta, bn_param)
        out,ca_dr = self.dropout(out, 0.3)
        out,ca_re1 = self.relu(out)
        out,ca_bn1 = self.batchnorm(out, gamma1, beta1, bn_param1)
        out,ca_dr1 = self.dropout(out, 0.3)
        
        y_hat = self.softmax(out)
        
        return y_hat, v, h, o, c, c_bar, i, f, z

    def backward_step(self, y, y_hat, dh_next, dc_next, c_prev, z, f, i, c_bar, c, o, h):
        """
        Implements the backward propagation for one time step
        """
        
        dv = np.copy(y_hat)
        dv[y] -= 1  # yhat - y

        self.grads["dWv"] += np.dot(dv, h.T)
        self.grads["dbv"] += dv

        dh = np.dot(self.params["Wv"].T, dv)
        dh += dh_next

        do = dh * np.tanh(c)
        da_o = do * o * (1 - o)
        self.grads["dWo"] += np.dot(da_o, z.T)
        self.grads["dbo"] += da_o

        dc = dh * o * (1 - np.tanh(c) ** 2)
        dc += dc_next

        dc_bar = dc * i
        da_c = dc_bar * (1 - c_bar ** 2)
        self.grads["dWc"] += np.dot(da_c, z.T)
        self.grads["dbc"] += da_c

        di = dc * c_bar
        da_i = di * i * (1 - i)
        self.grads["dWi"] += np.dot(da_i, z.T)
        self.grads["dbi"] += da_i

        df = dc * c_prev
        da_f = df * f * (1 - f)
        self.grads["dWf"] += np.dot(da_f, z.T)
        self.grads["dbf"] += da_f

        dz = (np.dot(self.params["Wf"].T, da_f)
              + np.dot(self.params["Wi"].T, da_i)
              + np.dot(self.params["Wc"].T, da_c)
              + np.dot(self.params["Wo"].T, da_o))

        dh_prev = dz[:self.n_h, :]
        dc_prev = f * dc
        return dh_prev, dc_prev

    def forward_backward(self, x_batch, y_batch, h_prev, c_prev):
        """
        Implements the forward and backward propagation for one batch
        """
        x, z = {}, {}
        f, i, c_bar, c, o = {}, {}, {}, {}, {}
        y_hat, v, h = {}, {}, {}

        # Values at t= - 1
        h[-1] = h_prev
        c[-1] = c_prev

        loss = 0
        for t in range(self.seq_len):
            x[t] = np.zeros((self.seq_size, 1))
            x[t][x_batch[t]] = 1

            y_hat[t], v[t], h[t], o[t], c[t], c_bar[t], i[t], f[t], z[t] = \
                self.forward_step(x[t], h[t - 1], c[t - 1])

            loss += -np.log(y_hat[t][y_batch[t], 0])

        self.reset_grads()

        dh_next = np.zeros_like(h[0])
        dc_next = np.zeros_like(c[0])

        for t in reversed(range(self.seq_len)):
            dh_next, dc_next = self.backward_step(y_batch[t], y_hat[t], dh_next,
                                                  dc_next, c[t - 1], z[t], f[t], i[t],
                                                  c_bar[t], c[t], o[t], h[t])
        return loss, h[self.seq_len - 1], c[self.seq_len - 1]

    def gradient_check(self, x, y, h_prev, c_prev, num_checks=10, delta=1e-6):
        """
        Checks the magnitude of gradients against expected approximate values
        """
        #print("**********************************")
        #print("Gradient check...\n")

        _, _, _ = self.forward_backward(x, y, h_prev, c_prev)
        grads_numerical = self.grads

        for key in self.params:
            #print("---------", key, "---------")
            test = True

            dims = self.params[key].shape
            grad_numerical = 0
            grad_analytical = 0

            for _ in range(num_checks):  # sample 10 neurons

                idx = int(uniform(0, self.params[key].size))
                old_val = self.params[key].flat[idx]

                self.params[key].flat[idx] = old_val + delta
                J_plus, _, _ = self.forward_backward(x, y, h_prev, c_prev)

                self.params[key].flat[idx] = old_val - delta
                J_minus, _, _ = self.forward_backward(x, y, h_prev, c_prev)

                self.params[key].flat[idx] = old_val

                grad_numerical += (J_plus - J_minus) / (2 * delta)
                grad_analytical += grads_numerical["d" + key].flat[idx]

            grad_numerical /= num_checks
            grad_analytical /= num_checks

            rel_error = abs(grad_analytical - grad_numerical) / abs(grad_analytical + grad_numerical)

            if rel_error > 1e-2:
                if not (grad_analytical < 1e-6 and grad_numerical < 1e-6):
                    test = False
                    assert (test)

            #print('Approximate: \t%e, Exact: \t%e =>  Error: \t%e' % (grad_numerical, grad_analytical, rel_error))
        #print("\nGradient Test successful!")