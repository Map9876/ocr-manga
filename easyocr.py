import subprocess 
import requests


# 定义命令行指令列表 
lines = [
    "mkdir easyocr",
    "pip install easyocr",  
]

#https://www.didimh.com/comic/a40a1cf120/1011525.html
url = "https://res2.tupian.run/res1_gf/a40a1cf120/185283/0_m5.webp" 
response = requests.get(url) 
 
if response.status_code  == 200:
    with open("ocr.jpg",  "wb") as file:
        file.write(response.content)


for line in lines: 
    try: 
        subprocess.run(line,  shell=True, check=True) 
    except subprocess.CalledProcessError as e: 
        print(f"执行命令 {line} 时出错: {e}")

import easyocr
import cv2

# 创建 OCR Reader, 使用简体中文和英文模型，并启用 GPU 加速
reader = easyocr.Reader(['ch_sim', 'en'], gpu=True)

# 读取图像
image_path = 'ocr.jpg'  # 替换为你的图像文件路径
image = cv2.imread(image_path)

# 执行 OCR
result = reader.readtext(image)

# 遍历结果并打印
for (bbox, text, prob) in result:
    (tl, tr, br, bl) = bbox
    tl = (int(tl[0]), int(tl[1]))
    tr = (int(tr[0]), int(tr[1]))
    br = (int(br[0]), int(br[1]))
    bl = (int(bl[0]), int(bl[1]))
    print(f"文本: {text}, 置信度: {prob}")
    cv2.rectangle(image, tl, br, (0, 255, 0), 2)
    cv2.putText(image, text, tl, cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

# 保存带有文本框的图像
output_image_path = 'output_with_text.png'
cv2.imwrite(output_image_path, image)
