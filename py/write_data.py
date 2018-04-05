import cv2
import csv
import numpy as np


# Add random noise in the range of [0, 255]
# If underflow or overflow take min or max respectively
def noise_with_bounds(data, mean, sd):
    noise = np.ceil(np.random.normal(mean, sd))
    if noise + data < 0:
        return 0
    elif noise + data > 255:
        return 255
    else:
        return np.ceil(data + noise)


# open image
data_name = "noise_data2"
# img = cv2.imread('../img_data/' + data_name + '.png')
img = cv2.imread(data_name + ".png")
width = img.shape[0]
height = img.shape[1]


# write to CSV
with open("../img_data/" + data_name + ".csv", 'w+', newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(['x', 'y', 'B', 'G', 'R'])
    for i in range(width):
        for j in range(height):

            # Add normal noise to the data to quell over fitting
            B = noise_with_bounds(img[i, j, 0], 0, 3)
            G = noise_with_bounds(img[i, j, 1], 0, 3)
            R = noise_with_bounds(img[i, j, 2], 0, 3)
            writer.writerow([i, j, B, G, R])
            img[i][j] = [B, G, R]

cv2.imwrite('noise_' + data_name + '.png', img)