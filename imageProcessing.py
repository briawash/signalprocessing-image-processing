"""
Brianca Washington
1001132562
"""
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
import numpy as  np
#import ndimage as nd
from PIL import Image
from scipy import ndimage

def applyfilter(image,v,num):
	mvgavg=np.array([.1,.1,.1,.1,.1,.1,.1,1,.1,.1])
	results=[]
	for line in range(len(image)):
		r=np.convolve(image[line,:],mvgavg)
		results.append(r)
	plt.figure(num)
	plt.title(v+'lowpass')
	plt.imshow(results,'gray')

def applyfilter2(image,v,num):
	mvgavg=np.array([1,-1])
	results=[]
	for line in range(len(image)):
		r=np.convolve(image[line,:],mvgavg)
		results.append(r)
	plt.figure(num)
	plt.title(v+'high pass')

"""
PART ONE BLUR:
 Lowpass and Highpass filter

"""


h=[.1,.1,.1,.1,.1,.1,.1,.1,.1,.1]
h2=[1,-1]
filenames= ["boat.512.tiff","man-5.3.01.tiff", "tank-7.1.07.tiff","clock-5.1.12.tiff"]

i=1

for x in filenames:
	# Open the file as an array
	im=mpimg.imread(x)
	imgplot= plt.imshow(im,'gray')
	plt.title (x +" Original")
	applyfilter(im,x,i)
	applyfilter2(im,x,i)
	i=i+1
	plt.show()






"""
PART D: Gray Noise

"""
N=10
#read in the file as an array 
#read in the picture as an array

imname="darinGrayNoise.jpg"

image= mpimg.imread(imname)
row, col= np.shape(image)

imgplot= plt.imshow(image,'gray')
plt.title (imname +" Original")
plt.show()


# pass the lowpass filter
"""

imgplot= plt.imshow(newimage, 'gray')
plt.title (imname +" Fixed with Lowpass Filter")
plt.show()"""


# pass the median filter
newimage = ndimage.median_filter(image, 5)

imgplot= plt.imshow(newimage, 'gray')
plt.title (imname +" Fixed with Median Filter")
plt.show()


