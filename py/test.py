# import the necessary packages
import pandas as pd
from sklearn.cluster import KMeans
import cv2


# Check if a pixel is on the border
# between a cluster and its complementary cluster
# def is_border(x, y, cluster, comp_cluster):



# open image
data_name = "data1"
img = cv2.imread('../img_data/' + data_name + '.png')

df = pd.read_csv('../img_data/' + data_name + '.csv')

# fit on just BGR values (not x and y)
X = df.iloc[:, 2:]
df["cluster"] = KMeans(n_clusters=2).fit_predict(X)


for i in range(df.shape[0]):
    if df.iloc[i]["cluster"] == 1:

        # VERY primitive image correction
        # Just add more red
        # and subtract some green

        R = df.iloc[i]['R']
        G = df.iloc[i]['G']
        new_R = 255 if R + 10 > 255 else R + 15
        new_G = 0 if G - 10 < 0 else G - 10
        x = df.iloc[i]["x"]
        img[int(df.iloc[i]["x"])][int(df.iloc[i]['y'])] = [df.iloc[i]['B'], new_G, new_R]


cv2.imwrite('testtest.png', img)
