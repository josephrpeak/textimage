import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import math

ascii_grayscale = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,"^`\'.'

outfile = open('output.txt', 'w')

img = cv.imread('sponge.jpeg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

fig, ax = plt.subplots(1, 2, figsize=(16,8))
fig.tight_layout()

ax[0].imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
ax[0].set_title("Original")

ax[1].imshow(cv.cvtColor(gray, cv.COLOR_BGR2RGB))
ax[1].set_title("Grayscale")

rows = gray.shape[1]
cols = gray.shape[0]

print(rows, cols)

asciiDict = {'1':'$','2':'@','3':'B','4':'%','5':'8','6':'&','7':'W','8':'M','9':'#','10':'*','11':'o','12':'a','13':'h','14':'k','15':'b','16':'d',
			'17':'p','18':'q','19':'w','20':'m','21':'Z','22':'O','23':'0','24':'Q','25':'L','26':'C','27':'J','28':'U','29':'Y','30':'X','31':'z',
			'32':'c','33':'v','34':'u','35':'n','36':'x','37':'r','38':'j','39':'f','40':'t','41':'/','42':'\\','43':'|','44':'(','45':')','46':'1',
			'47':'{','48':'}','49':'[','50':']','51':'?','52':'-','53':'_','54':'+','55':'~','56':'<','57':'>','58':'i','59':'!','60':'l','61':'I',
			'62':';','63':':','64':','}
			
		#print("Numerical Value: " + str(gray[j][i]))'''

for i in range(rows):
	for j in range(cols):
		if(gray[i][j] == 0):
			gray[i][j] = 1
		to_string = str(math.ceil((gray[i][j])/4))
		outfile.write(asciiDict[to_string])
		#outfile.write(to_string)
		#print(gray[i][j])
	outfile.write('\n')

#plt.show()
