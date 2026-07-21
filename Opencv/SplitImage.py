import cv2
import numpy as np
img_path = "/Users/qw/Downloads/bird.jpg"
img = cv2.imread(img_path)
#判断图像是否存在
def ifPD():
  if img is None:
    print("img is None")
    exit()
# 分离通道灰色
#利用cv2.split()函数分离通道，返回三个通道的图像
def split_demo1():
  cv2.imshow("Bird",img)
  b,g,r = cv2.split(img)
  cv2.imshow("blue",b)
  cv2.imshow("green",g)
  cv2.imshow("red",r)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
#分离通道彩色BGR
#利用np.zeros_like()函数创建一个与原图像大小相同的全零数组，然后将分离的通道赋值给对应的通道位置，最后显示彩色图像
def split_demo2():
  cv2.imshow('butterfly', img)
  b,g,r = cv2.split(img)
  like_img_b = np.zeros_like(img)
  like_img_b[:,:,0] = b
  like_img_g = np.zeros_like(img)
  like_img_g[:,:,1] = g
  like_img_r = np.zeros_like(img)
  like_img_r[:,:,2] = r
  cv2.imshow('blue', like_img_b)
  cv2.imshow('green', like_img_g)
  cv2.imshow('red', like_img_r)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
#通道分离 HSV 单独通道图像显示
#利用cv2.cvtColor()函数将BGR图像转换为HSV图像，然后使用cv2.split()函数分离通道，最后显示HSV图像和分离的通道图像
def split_demo3():
  cv2.imshow('butterfly', img)
  dst = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
  cv2.imshow('butterfly_hsv', dst)
  b,g,r = cv2.split(dst)
  cv2.imshow('butterfly_b', b)
  cv2.imshow('butterfly_g', g)
  cv2.imshow('butterfly_r', r)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
#合并通道
#利用merge()函数将分离的通道重新合并为一张图像，并显示合并后的图像
def merge_demo():
  cv2.imshow('Bird',img)
  b,r,g = cv2.split(img)
  dst = cv2.merge([b,r,g])
  cv2.imshow('merge',dst)
  dst1 = cv2.merge([r,g,b])
  cv2.imshow('merge1',dst1)
  dst2 = cv2.merge([g,b,r])
  cv2.imshow('merge2',dst2)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
#通道复制
#利用cv2.mixChannels()函数将图像的通道进行复制和交换，并显示复制后的图像
def mixchannel_demo():
  cv2.imshow('bird',img)
  #复制图象矩阵
  dst = np.zeros_like(img)
  cv2.mixChannels([img],[dst],fromTo = [0,1,2,2,1,0])
  cv2.imshow('mixChannels',dst)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
#通道阈值
def inrange_demo():
  cv2.imshow('bird',img)
  #将图像转换为HSV颜色空间
  hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
  #设置阈值范围
  lower = np.array([0,0,0])
  upper = np.array([80,255,163])
  #进行阈值处理
  mask = cv2.inRange(hsv,lower,upper)
  cv2.imshow('mask',mask)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
if __name__ == "__main__":
  ifPD()
  inrange_demo()