import pandas as pd
import numpy as np
from sklearn.svm import LinearSVR
from sklearn.datasets import make_regression
import matplotlib.pyplot as plt
import random
from matplotlib.pyplot import figure
test_data = pd.read_csv("Sample.csv")
reference = pd.read_csv("Reference.csv")
train = reference.drop("Gene",1)
test_data = test_data.drop("gene",1)

score_adj = []
for o in range(len(test_data.columns)):
    test = test_data.loc[:,test_data.columns[o]]
    im_name = train.columns
    svr = LinearSVR(random_state=0)
    model = svr.fit(train, test)
    score = model.coef_
    score[np.where(score<0)] = 0 
    score_adj.append((score/sum(score)))
score_adj = pd.DataFrame(score_adj)
score_adj.columns = im_name
score_adj.plot(kind='bar', stacked=True,legend=False)
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.suptitle("Flow&Estimate")
plt.rcParams['figure.figsize'] = (6.69,8.86)
plt.rcParams['figure.dpi'] = 300
name = "bar.pdf"
plt.savefig(name,bbox_inches="tight" )
plt.close()
plt.boxplot(score_adj.T,patch_artist = True)
plt.suptitle("Flow&Estimate")
plt.xticks(range(8), im_name)
plt.rcParams['figure.figsize'] = (6.69,8.86)
plt.rcParams['figure.dpi'] = 300
name = "boxplot.pdf"
plt.savefig(name)

score_adj.to_csv("score.csv")
