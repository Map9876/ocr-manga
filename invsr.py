import subprocess 



# 定义命令行指令列表 
lines = [
    "mkdir InvSR",
    "git clone https://github.com/zsyOAOA/InvSR.git",
    "pip install torch==2.4.0 torchvision==0.19.0 torchaudio==2.4.0 --index-url https://download.pytorch.org/whl/cu121",  
    "pip install -U xformers==0.0.27.post2  --index-url https://download.pytorch.org/whl/cu121",  
    "pip install -e \".[torch]\"", 
    "pip install -r requirements.txt",  
]


url = "https://pic-image.yesky.com/uploadImages/newPic/2023/214/05/KN68FQ4NIFCS.png" 
response = requests.get(url) 
 
if response.status_code  == 200:
    with open("InvSR/test.jpg",  "wb") as file:
        file.write(response.content)


for line in lines: 
    try: 
        subprocess.run(line,  shell=True, check=True) 
    except subprocess.CalledProcessError as e: 
        print(f"执行命令 {line} 时出错: {e}")

run =[
    "python InvSR/inference_invsr.py InvSR/test.jpg -i  -o InvSR/output.jpg --num_steps 1" 
]
subprocess.run(run,  shell=True, check=True)
