########################################################
#
# Computer Colorblindness correction
# Jimmy Hickey
# Jan 30 2018
#
########################################################

# imager documentation
require(imager)
library(imager)

file = system.file('~/Documents/Programming/git/Computer-Color-Blind-Correction/test_data/rgb1.png', package='imager')
img = load.image('~/Documents/Programming/git/Computer-Color-Blind-Correction/test_data/rgb1.png')
plot(img)
img

img2 = load.image('~/Documents/Programming/git/Computer-Color-Blind-Correction/test_data/rgb2.png')
plot(img2)
R(img2)
img2copy = img2

# Display the matricies of each color
color.at(img)
channel(img2copy)
G(img2copy) = 0
B(img2copy) = 255
R(img2copy) = 244
plot(img2copy)



#### png library
library(png)
pimg = readPNG(source = "~/Documents/Programming/git/Computer-Color-Blind-Correction/test_data/rgb1.png")
dim(pimg)
pimg
plot(pimg)
img3 = load.image(pimg)