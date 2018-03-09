# import the necessary packages
import pandas as pd

from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

import plotly.graph_objs as go
from plotly.offline import iplot
import cv2

# open image
img = cv2.imread('../img_data/data2.png')

df = pd.read_csv('../img_data/data2.csv')

# fit on just BGR values (not x and y)
X = df.iloc[:, 2:]
df["cluster"] = KMeans(n_clusters=2).fit_predict(X)

print(df.iloc[200]["x"])
print(img[200][200])

for i in range(df.shape[0]):
    if df.iloc[i]["cluster"] == 1:
        img[df.iloc[i]["x"]][df.iloc[i]['y']] = [0, 0, 0]



cv2.imwrite('testtest.png', img)
