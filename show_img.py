
import torch
import torchio as tio
import matplotlib.pyplot as plt
import numpy as np
import cv2
from skimage import feature

T = 19
D = 5

img = tio.ScalarImage('patient003/patient003_4d.nii.gz')

t_img = img.data


#####
fft_img = torch.fft.fft(t_img, axis=0)
filtred = fft_img
filtred[:1, :, :, :] = 0.0
filtred[3:, :, :, :] = 0.0

timg2 = torch.abs(torch.fft.fft(filtred, axis=0))

mask = np.array(timg2[T, :, :, D])
mask = np.uint8(2*mask/np.max(mask)*255)
kernel = np.ones((19, 19), np.uint8) 
mask = cv2.dilate(mask, kernel, 1)
mask = cv2.blur(mask,(21, 21))
print(np.max(mask))

img_m = np.array(t_img[T, :, :, D], dtype=np.float64)
img_m = np.uint8(img_m/np.max(img_m)*np.float64(mask))
img_m = cv2.medianBlur(img_m,5)

circles = cv2.HoughCircles(img_m, cv2.HOUGH_GRADIENT, 1, 20,
                            param1=60,param2=30,minRadius=1,maxRadius=0)

#####
def to_rgb(gray):
  return cv2.cvtColor(gray,cv2.COLOR_GRAY2RGB)

cimg = np.array(t_img[T, :, :, D])
cimg = np.uint8(cimg/np.max(cimg)*255)
cimg = to_rgb(cimg)
if circles is not None:
 print("circles !")
 circles = np.uint16(np.around(circles))
 for i in circles[0,:]:
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),1)
    cv2.circle(cimg,(i[0],i[1]),1,(255,0,0),2)

f, (ax1, ax2) = plt.subplots(1, 2)
ax1.imshow(cimg, vmin = 0, vmax=255)
ax2.imshow(img_m, cmap="grey", vmin = 0, vmax=255)

plt.show()



