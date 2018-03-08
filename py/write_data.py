import cv2
import csv

# open image
img = cv2.imread('../img_data/data1.png')
width = img.shape[0]
height = img.shape[1]

# write to CSV
with open("../img_data/data1.csv", 'w', newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(['x', 'y', 'B', 'G', 'R'])
    for i in range(width):
        for j in range(height):
            writer.writerow([i, j, img[i, j, 0], img[i, j, 1], img[i, j, 2]])

