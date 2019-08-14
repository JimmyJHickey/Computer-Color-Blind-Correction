# import the necessary packages
import pandas as pd
from sklearn.cluster import KMeans
import cv2


# Check if a pixel is on the border
# between a cluster and its complementary cluster
# def is_border(x, y, cluster, comp_cluster):


# open image
data_name = "noise_data4"
# img = cv2.imread('../img_data/' + data_name + '.png')
img = cv2.imread(data_name + '.png')
width =x img.shape[0]
height = img.shape[1]

df = pd.read_csv('../img_data/' + data_name + '.csv')
# df = pd.read_csv('../img_data/heart.csv')


# fit on just BGR values (not x and y)
X = df.iloc[:, 2:]
df["cluster"] = KMeans(n_clusters=2).fit_predict(X)




print(pd.DataFrame.head(df))
print(height)

for i in range(df.shape[0]):
    if df.iloc[i]["cluster"] == 1:
        img[int(df.iloc[i]["x"])][int(df.iloc[i]['y'])] = [255, 255, 255]
    elif df.iloc[i]["cluster"] == 0:
        img[int(df.iloc[i]["x"])][int(df.iloc[i]['y'])] = [0, 0, 0]

#
#         # VERY primitive image correction
#         # Just add more red
#         # and subtract some green
#
#         R = df.iloc[i]['R']
#         G = df.iloc[i]['G']
#         new_R = 255 if R + 10 > 255 else R + 10
#         new_G = 0 if G - 10 < 0 else G - 10
#         x = df.iloc[i]["x"]
#         img[int(df.iloc[i]["x"])][int(df.iloc[i]['y'])] = [df.iloc[i]['B'], new_G, new_R]
#
# print("x: %d \t\t y: %d" % (df.iloc[-1]['x'], df.iloc[-1]['y']))


# check if bordering different cluster
# for i in range(df.shape[0]):
#     clust = df.iloc[i]["cluster"]
#     print("x: %d \t\t y: %d" % (df.iloc[i]['x'], df.iloc[i]['y']))
#     if (df.iloc[i]['y'] - 1 > 0 and df.iloc[i - 1]["cluster"] != clust and df.iloc[i - 1]["cluster"] != 2):
#         df.at[i, 'cluster'] = 2
#         img[int(df.iloc[i]["x"])][int(df.iloc[i]['y'])] = [0, 0, 0]
#         print("WROTE A BORDER PIXEL b/c lower y %d" % i)
#
#     elif (df.iloc[i]['y'] + 1 < height and df.iloc[i + 1]["cluster"] != clust and df.iloc[i + 1]["cluster"] != 2):
#         df.at[i, 'cluster'] = 2
#         img[int(df.iloc[i]["x"])][int(df.iloc[i]['y'])] = [0, 0, 0]
#         print("WROTE A BORDER PIXEL b/c upper y %d" % i)
#
#     elif (df.iloc[i]['x'] + 1 < width and df.iloc[i + width]["cluster"] != clust and df.iloc[i + width]["cluster"] != 2):
#         df.at[i, 'cluster'] = 2
#         img[int(df.iloc[i]["x"])][int(df.iloc[i]['y'])] = [0, 0, 0]
#         print("WROTE A BORDER PIXEL b/c right x %d" % i)
#
#     elif (df.iloc[i]['x'] - 1 > 0 and df.iloc[i - width]["cluster"] != clust and df.iloc[i - width]["cluster"] != 2):
#         df.at[i, 'cluster'] = 2
#         img[int(df.iloc[i]["x"])][int(df.iloc[i]['y'])] = [0, 0, 0]
#         print("WROTE A BORDER PIXEL b/c left  x %d" % i)


cv2.imwrite(data_name+'_bw.png', img)
