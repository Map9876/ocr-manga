jdj

exec_command = 'pip install numpy torch torchvision sounddevice pypinyin coqui-tts'
import os
global ok
ok = True
os.system(exec_command)
import subprocess

# -*- coding: UTF-8 -*-
import torch
from TTS.api import TTS
import numpy as np
import soundfile as sf
from datetime import datetime
import requests


device = "cuda" if torch.cuda.is_available() else "cpu"

# 列出可用模型
print("可用模型是:")
print(TTS().list_models())

print("开始初始化模型:", datetime.now())

# tts_models/multilingual/multi-dataset/xtts_v2是模型标识
#tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)
print("下是执行的命令行，可用模型↓")
ok = "yes | tts --model_name tts_models/multilingual/multi-dataset/xtts_v2 --list_language_idx"
os.system(ok)
print("上面是执行的命令行，可用模型↑")

p = subprocess.Popen( 
    ['python', '-c', 'from TTS.api  import TTS; tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device); print(tts)'], 
    stdin = subprocess.PIPE, 
    stdout = subprocess.PIPE, 
    stderr = subprocess.PIPE, 
    text = True 
) 
out, err = p.communicate(input='y\n')  
print("初始化模型完成:", datetime.now())

print("初始化模型完成:", datetime.now())
url = "https://github.com/kuemit/txt_book/raw/refs/heads/master/examples/alice_in_wonderland.txt" 
response = requests.get(url) 
 
if response.status_code  == 200:
    with open("demo.txt",  "wb") as file:
        file.write(response.content)
url = "https://hf-mirror.com/coqui/XTTS-v2/resolve/main/samples/zh-cn-sample.wav?download=true" 
response = requests.get(url) 
 
if response.status_code  == 200:
    with open("sample.wav",  "wb") as file:
        file.write(response.content)      

# 从文件中读取文本 

with open('demo.txt','r',encoding='utf-8') as source_file:
    content = source_file.read()
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

tts.tts_to_file(text=content, 
                speaker_wav="sample.wav", 
                language="zh-cn", 
                file_path="output.wav")
