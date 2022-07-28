import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import math

ascii_grayscale = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,"^`\'.'

outfile = open('output.txt', 'w')

img = cv.imread('images/astra.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

scale = 30

if(scale != 100):
	width = int(gray.shape[1]*scale / 100)
	height = int(gray.shape[0]*scale / 100)
	dim = (width, height)

	gray = cv.resize(gray, dim)

	rows = height
	cols = width
else:
	rows = gray.shape[1]
	cols = gray.shape[0]

print(rows, cols)

fig, ax = plt.subplots(1, 2, figsize=(16,8))
fig.tight_layout()

ax[0].imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
ax[0].set_title("Original")

ax[1].imshow(cv.cvtColor(gray, cv.COLOR_BGR2RGB))
ax[1].set_title("Grayscale")

asciiDict = {'0':'$','1':'@','2':'B','3':'%','4':'8','5':'&','6':'W','7':'M','8':'#','9':'*','10':'o','11':'a','12':'h','13':'k','14':'b','15':'d','16':'p',
			'17':'q','18':'w','19':'m','20':'Z','21':'O','22':'0','23':'Q','24':'L','25':'C','26':'J','27':'U','28':'Y','29':'X','30':'z','31':'c',
			'32':'v','33':'u','34':'n','35':'x','36':'r','37':'j','38':'f','39':'t','40':'/','41':'\\','42':'|','43':'(','44':')','45':'1','46':'{',
			'47':'}','48':'[','49':']','50':'?','51':'-','52':'_','53':'+','54':'~','55':'<','56':'>','57':'i','58':'!','59':'l','60':'I','61':';',
			'62':':','63':',','64':'.'}

for i in range(rows):
	for j in range(cols):
		to_string = str(math.ceil((gray[i][j])/4))
		outfile.write(asciiDict[to_string])
	outfile.write('\n')

#plt.show()
