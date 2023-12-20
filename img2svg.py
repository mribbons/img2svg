import sys
import cv2
import numpy as np

print(f'converting {sys.argv[1]} to {sys.argv[2]}')

input = cv2.imread(sys.argv[1])
input = cv2.cvtColor(input, cv2.COLOR_BGR2GRAY)
ret, input = cv2.threshold(input, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(input, cv2.RETR_TREE , cv2.CHAIN_APPROX_SIMPLE)

# remove border
contours = contours[1:]

f = open(sys.argv[2], 'w+')
f.write('<svg width="'+str(input.shape[1])+'" height="'+str(input.shape[0])+'" xmlns="http://www.w3.org/2000/svg">\n')
f.write('\t<circle r="1e5" fill="black"/>')

for c in contours:
    f.write('\t<path fill="white" d="M ')
    for i in range(len(c)):
        x, y = c[i][0]
        f.write(str(x)+  ' ' + str(y)+' ')

    # f.write('"/>\n')
    f.write(' Z "/>\n')
f.write('</svg>')
f.close()
