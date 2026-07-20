# 导入 OpenCV 库
import cv2

# 1. 读取图像
# 替换为实际的图像路径，这里是当前目录下的 "bird.jpg"
image_path = "/Users/qw/Downloads/bird.jpg"
image = cv2.imread(image_path)

# 检查图像是否成功读取
if image is None:
    print("错误：无法加载图像，请检查路径是否正确。")
    exit()

# 2. 显示图像
# 创建一个名为 "Display Image" 的窗口，并在其中显示图像
cv2.imshow("Let you fly", image)

# 3. 等待用户按键
# 参数 0 表示无限等待，直到用户按下任意键
key = cv2.waitKey(0)

# 4. 根据用户按键执行操作
if key == ord('s'):  # 如果按下 's' 键
    # 保存图像
    output_path = "One bird.jpg"
    cv2.imwrite(output_path, image)
    print(f"图像已保存为 {output_path}")
elif key == ord('q'):  # 如果按下q键
    print("直接退出程序")
elif key == 27:  # 如果按下 ESC 键
    print("图像未保存，程序退出")
else:
    print("未定义的按键，程序退出")
# 5. 关闭所有窗口
cv2.destroyAllWindows()