import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

data = {'A': [45,37,42,35,39],
        'B': [38,31,26,28,33],
        'C': [10,15,17,21,12]
        }

df = pd.DataFrame(data,columns=['A','B','C'])

corrMatrix = df.corr()
svm = sn.heatmap(corrMatrix, annot=True)
# plt.show()

figure = svm.get_figure()    
figure.savefig('svm_conf.png', dpi=96)