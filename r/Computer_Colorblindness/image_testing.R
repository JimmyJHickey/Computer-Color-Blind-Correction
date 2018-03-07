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
img2copy = img2

# Display the matricies of each color
plot(img2copy)
color.at(img2copy, x = 2, y = 4 ) = c(0, 0 ,255, 0)
plot(img2copy)
B(img2copy) = 0.3
plot(img2copy)


# Data?
# http://www.colour-blindness.com/colour-blindness-tests/ishihara-colour-test-plates/
