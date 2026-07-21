#图像处理基础
#1.导入Opencv库
import cv2

#2.读取图像
#首先声明图像路径再读取路径中的图像
img_path = "/Users/qw/Downloads/bird.jpg"
img = cv2.imread(img_path)

#3.判断图像是否存在
if img is None:
    print("img is None")
    exit()

#展示图像
'''
cv2.imshow("Display",img)
#等待按键按下，0表示一直等待
key = cv2.waitKey(0)


#判断是哪个案件按下，进行不同的处理
if key == ord('s'):
    output_path = "/Users/qw/Python/Opencv/IMAGE/a bird.jpg"
    cv2.imwrite(output_path,img)
    print("img has saved")
else:
    print("未定义按钮，程序退出")
'''

# 访问像素值
'''
pixel_value = img[100, 150]  # 访问 (150, 100) 位置的像素值
print(pixel_value)#以BGR格式输出
# 修改像素值
img[100, 150] = [255, 255, 255]  # 将 (150, 100) 位置的像素值设置为白色
print(pixel_value)
'''

# 获取 ROI
roi = img[50:150, 50:150]  # 获取 (50,50) 到 (150,150) 的区域
# 修改 ROI
img[50:150, 50:150] = [0, 255, 0]  # 将 ROI 区域设置为绿色

#展示图像
cv2.imshow("Display",img)
#等待按键按下，0表示一直等待
key = cv2.waitKey(0)
#判断是哪个案件按下，进行不同的处理
if key == ord('s'):
    output_path = "/Users/qw/Python/Opencv/IMAGE/a bird.jpg"
    cv2.imwrite(output_path,img)
    print("img has saved")
else:
    print("未定义按钮，程序退出")
cv2.destroyAllWindows()