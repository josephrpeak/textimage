import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

ascii_grayscale = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,"^`\'.'

outfile = open('output.txt', 'w')

img = cv.imread('homer.jpg')
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

for i in range(rows):
	for j in range(cols):
		if(gray[i][j] < 4):
			print('$')
			outfile.write('$')
		elif(gray[i][j] < 8):
			print('@')
			outfile.write('@')
		elif(gray[i][j] < 12):
			print('B')
			outfile.write('B')
		elif(gray[i][j] < 16):
			print('%')
			outfile.write('%')
		elif(gray[i][j] < 20):
			print('8')
			outfile.write('8')
		elif(gray[i][j] < 24):
			print('&')
			outfile.write('&')
		elif(gray[i][j] < 28):
			print('W')
			outfile.write('W')
		elif(gray[i][j] < 32):
			print('M')
			outfile.write('M')
		elif(gray[i][j] < 36):
			print('#')
			outfile.write('#')
		elif(gray[i][j] < 40):
			print('*')
			outfile.write('*')
		elif(gray[i][j] < 44):
			print('o')
			outfile.write('o')
		elif(gray[i][j] < 48):
			print('a')
			outfile.write('a')
		elif(gray[i][j] < 52):
			print('h')
			outfile.write('h')
		elif(gray[i][j] < 56):
			print('k')
			outfile.write('k')
		elif(gray[i][j] < 60):
			print('b')
			outfile.write('b')
		elif(gray[i][j] < 64):
			print('d')
			outfile.write('d')
		elif(gray[i][j] < 68):
			print('p')
			outfile.write('p')
		elif(gray[i][j] < 72):
			print('q')
			outfile.write('q')
		elif(gray[i][j] < 76):
			print('w')
			outfile.write('w')
		elif(gray[i][j] < 80):
			print('m')
			outfile.write('m')
		elif(gray[i][j] < 84):
			print('Z')
			outfile.write('Z')
		elif(gray[i][j] < 88):
			print('O')
			outfile.write('O')
		elif(gray[i][j] < 92):
			print('0')
			outfile.write('0')
		elif(gray[i][j] < 96):
			print('Q')
			outfile.write('Q')
		elif(gray[i][j] < 100):
			print('L')
			outfile.write('L')
		elif(gray[i][j] < 104):
			print('C')
			outfile.write('C')
		elif(gray[i][j] < 108):
			print('J')
			outfile.write('J')
		elif(gray[i][j] < 112):
			print('U')
			outfile.write('U')
		elif(gray[i][j] < 116):
			print('Y')
			outfile.write('Y')
		elif(gray[i][j] < 120):
			print('X')
			outfile.write('X')
		elif(gray[i][j] < 124):
			print('z')
			outfile.write('z')
		elif(gray[i][j] < 128):
			print('c')
			outfile.write('c')
		elif(gray[i][j] < 132):
			print('v')
			outfile.write('v')
		elif(gray[i][j] < 136):
			print('u')
			outfile.write('u')
		elif(gray[i][j] < 140):
			print('n')
			outfile.write('n')
		elif(gray[i][j] < 144):
			print('x')
			outfile.write('x')
		elif(gray[i][j] < 148):
			print('r')
			outfile.write('r')
		elif(gray[i][j] < 152):
			print('j')
			outfile.write('j')
		elif(gray[i][j] < 156):
			print('f')
			outfile.write('f')
		elif(gray[i][j] < 160):
			print('t')
			outfile.write('t')
		elif(gray[i][j] < 164):
			print('/')
			outfile.write('/')
		elif(gray[i][j] < 168):
			print('\\')
			outfile.write('\\')
		elif(gray[i][j] < 172):
			print('|')
			outfile.write('|')
		elif(gray[i][j] < 176):
			print('(')
			outfile.write('(')
		elif(gray[i][j] < 180):
			print(')')
			outfile.write(')')
		elif(gray[i][j] < 184):
			print('1')
			outfile.write('1')
		elif(gray[i][j] < 188):
			print('{')
			outfile.write('{')
		elif(gray[i][j] < 192):
			print('}')
			outfile.write('}')
		elif(gray[i][j] < 196):
			print('[')
			outfile.write('[')
		elif(gray[i][j] < 200):
			print(']')
			outfile.write(']')
		elif(gray[i][j] < 204):
			print('?')
			outfile.write('?')
		elif(gray[i][j] < 208):
			print('-')
			outfile.write('-')
		elif(gray[i][j] < 212):
			print('_')
			outfile.write('_')
		elif(gray[i][j] < 216):
			print('+')
			outfile.write('+')
		elif(gray[i][j] < 220):
			print('~')
			outfile.write('~')
		elif(gray[i][j] < 224):
			print('<')
			outfile.write('<')
		elif(gray[i][j] < 228):
			print('>')
			outfile.write('>')
		elif(gray[i][j] < 232):
			print('i')
			outfile.write('i')
		elif(gray[i][j] < 236):
			print('!')
			outfile.write('!')
		elif(gray[i][j] < 240):
			print('l')
			outfile.write('l')
		elif(gray[i][j] < 244):
			print('I')
			outfile.write('I')
		elif(gray[i][j] < 248):
			print(';')
			outfile.write(';')
		elif(gray[i][j] < 252):
			print(':')
			outfile.write(':')
		elif(gray[i][j] < 256):
			print(',')
			outfile.write(',')
	
		

		#print("Numerical Value: " + str(gray[j][i]))'''

plt.show()