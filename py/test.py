# import the necessary packages
import pandas as pd
from sklearn.cluster import KMeans
import cv2


# Check if a pixel is on the border
# between a cluster and its complementary cluster
# def is_border(x, y, cluster, comp_cluster):


# open image
data_name = "data4"
img = cv2.imread('../img_data/' + data_name + '.png')
width = img.shape[0]
height = img.shape[1]

df = pd.read_csv('../img_data/' + data_name + '.csv')

# fit on just BGR values (not x and y)
X = df.iloc[:, 2:]
df["cluster"] = KMeans(n_clusters=2).fit_predict(X)
print(pd.DataFrame.head(df))
print(height)

# for i in range(df.shape[0]):
#     if df.iloc[i]["cluster"] == 1:
#
#         # VERY primitive image correction
#         # Just add more red
#         # and subtract some green
#
#         R = df.iloc[i]['R']
#         G = df.iloc[i]['G']
#         new_R = 255 if R + 10 > 255 else R + 15
#         new_G = 0 if G - 10 < 0 else G - 10
#         x = df.iloc[i]["x"]
#         img[int(df.iloc[i]["x"])][int(df.iloc[i]['y'])] = [df.iloc[i]['B'], new_G, new_R]


# check if bordering different cluster
for i in range(df.shape[0]):
    clust = df.iloc[i]["cluster"]
    if (df.iloc[i]['y']-1 > 0 and df.iloc[i-height]["cluster"] != clust and df.iloc[i-height]["cluster"] != 2) or \
        (df.iloc[i]['y'] + 1 < height and df.iloc[i + height]["cluster"] != clust and df.iloc[i + height]["cluster"] != 2) or \
        (df.iloc[i]['x'] + 1 > width and i + df.iloc[i + 1]["cluster"] != clust and df.iloc[i + 1]["cluster"] != 2) or \
        (df.iloc[i]['x'] - 1 > 0 and df.iloc[i - 1]["cluster"] != clust and df.iloc[i - 1]["cluster"] != 2):
        df.at[i, 'cluster'] = 2
        img[int(df.iloc[i]["x"])][int(df.iloc[i]['y'])] = [255, 255, 255]

cv2.imwrite(data_name+'_test.png', img)
