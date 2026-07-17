#访问修改像素值
import cv2

# 读取图像
img = cv2.imread('/Users/qw/Downloads/bird.jpg')

# 访问像素值
pixel_value = img[100, 150]  # 访问 (150, 100) 位置的像素值
print(pixel_value)
# 修改像素值
img[100, 150] = [255, 255, 255]  # 将 (150, 100) 位置的像素值设置为白色