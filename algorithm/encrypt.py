from PIL import Image
from random import randint
import numpy
from .helper import *

def encryptionImage(pathfile):
	im = Image.open(pathfile)
	pix = im.load()

	m = im.size[0]  # row || width of image
	n = im.size[1]  # col || height of image

	# Obtaining the RGB matrices
	r = []
	g = []
	b = []
	for i in range(m):  # row
		r.append([])
		g.append([])
		b.append([])
		for j in range(n):  # col
			rgbPerPixel = pix[i, j]  # อ่านค่าสีรูปภาพ RGB(r,g,b) จำนวน row*col
			r[i].append(rgbPerPixel[0])
			g[i].append(rgbPerPixel[1])
			b[i].append(rgbPerPixel[2])

	# Vectors Kr and Kc
	alpha = 8
	Kr = [randint(0, pow(2, alpha) - 1) for i in
		  range(m)]  # สุ่มเลขจำนวนเต็ม จำนวนตามsizeความกว้าง โดยตัวเลขจะอยู่ระหว่าง 0-255 เป็น keys ของ row
	Kc = [randint(0, pow(2, alpha) - 1) for i in
		  range(n)]  # สุ่มเลขจำนวนเต็ม จำนวนตามsizeความศูง โดยตัวเลขจะอยู่ระหว่าง 0-255 เป็น Key ของ column
	ITER_MAX = 1  # จำนวนการทำซ้ำ

	print('Vector Kr : ', Kr)
	print('Vector Kc : ', Kc)

	f = open('keys.txt', 'w+')
	f.write('Vector Kr : \n')
	for a in Kr:
		f.write(str(a) + '\n')
	f.write('Vector Kc : \n')
	for a in Kc:
		f.write(str(a) + '\n')
	f.write('ITER_MAX : \n')
	f.write(str(ITER_MAX) + '\n')

	for iterations in range(ITER_MAX):
		# For each row
		for i in range(m):
			rTotalSum = sum(r[i])
			gTotalSum = sum(g[i])
			bTotalSum = sum(b[i])
			rModulus = rTotalSum % 2
			gModulus = gTotalSum % 2
			bModulus = bTotalSum % 2
			if (rModulus == 0):  # roll -> right ถ้าหารลงตัว หมุนแถว r[i] ไปทางขวา ตามจำนวน kr[i] ครั้ง
				r[i] = numpy.roll(r[i], Kr[i])
			else:  # roll -> left ถ้าหารไม่ลงตัว หมุนแถว r[i] ไปทางซ้าย ตามจำนวน kr[i] ครั้ง
				r[i] = numpy.roll(r[i], -Kr[i])
			if (gModulus == 0):
				g[i] = numpy.roll(g[i], Kr[i])
			else:
				g[i] = numpy.roll(g[i], -Kr[i])
			if (bModulus == 0):
				b[i] = numpy.roll(b[i], Kr[i])
			else:
				b[i] = numpy.roll(b[i], -Kr[i])
		# For each column
		for i in range(n):
			rTotalSum = 0
			gTotalSum = 0
			bTotalSum = 0
			for j in range(m):
				rTotalSum += r[j][i]
				gTotalSum += g[j][i]
				bTotalSum += b[j][i]
			rModulus = rTotalSum % 2
			gModulus = gTotalSum % 2
			bModulus = bTotalSum % 2
			if (rModulus == 0):
				upshift(r, i, Kc[i])  # roll -> up
			else:
				downshift(r, i, Kc[i])  # roll -> down
			if (gModulus == 0):
				upshift(g, i, Kc[i])
			else:
				downshift(g, i, Kc[i])
			if (bModulus == 0):
				upshift(b, i, Kc[i])
			else:
				downshift(b, i, Kc[i])
		# For each row
		for i in range(m):
			for j in range(n):
				if (i % 2 == 1):
					# XOR
					r[i][j] = r[i][j] ^ Kc[j]
					g[i][j] = g[i][j] ^ Kc[j]
					b[i][j] = b[i][j] ^ Kc[j]
				else:
					# reverse and XOR
					r[i][j] = r[i][j] ^ rotate180(Kc[j])
					g[i][j] = g[i][j] ^ rotate180(Kc[j])
					b[i][j] = b[i][j] ^ rotate180(Kc[j])
		# For each column
		for j in range(n):
			for i in range(m):
				if (j % 2 == 0):
					# XOR
					r[i][j] = r[i][j] ^ Kr[i]
					g[i][j] = g[i][j] ^ Kr[i]
					b[i][j] = b[i][j] ^ Kr[i]
				else:
					# reverse and XOR
					r[i][j] = r[i][j] ^ rotate180(Kr[i])
					g[i][j] = g[i][j] ^ rotate180(Kr[i])
					b[i][j] = b[i][j] ^ rotate180(Kr[i])

	for i in range(m):
		for j in range(n):
			# Replace color
			pix[i, j] = (r[i][j], g[i][j], b[i][j])

	im.save(pathfile.split('.')[0] + '.png')
	print("Encryption Success!!!")
	return pathfile.split('.')[0] + '.png'


