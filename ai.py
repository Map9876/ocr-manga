import subprocess 


# 定义命令行指令列表 
lines = [
    "mkdir out",
    "git clone https://github.com/zsyOAOA/InvSR.git",
    "pip install torch==2.4.0 torchvision==0.19.0 torchaudio==2.4.0 --index-url https://download.pytorch.org/whl/cu121",  
    "pip install -U xformers==0.0.27.post2  --index-url https://download.pytorch.org/whl/cu121",  
    "pip install -e \".[torch]\"", 
    "pip install -r requirements.txt",  
    "python inference_invsr.py  -i path -o out --num_steps 1" 
] 
 
for line in lines: 
    try: 
        subprocess.run(line,  shell=True, check=True) 
    except subprocess.CalledProcessError as e: 
        print(f"执行命令 {line} 时出错: {e}")
