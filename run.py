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
print(TTS().list_models())

print("开始初始化模型:", datetime.now())

# tts_models/multilingual/multi-dataset/xtts_v2是模型标识
#tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

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
url = "https://github.com/zhaominyiz/IzayoyiMikukoStudio/raw/refs/heads/master/%E4%B8%8E%E5%90%9B%E7%9A%84%E5%A4%8F%E6%97%A5%E4%B9%8B%E6%A2%A6%20.mp3" 
response = requests.get(url) 
 
if response.status_code  == 200:
    with open("sample.wav",  "wb") as file:
        file.write(response.content)      

# 从文件中读取文本
with open('demo.txt','r',encoding='utf-8') as source_file:
    content = source_file.read()

tts.tts_to_file(text="A short story is a piece of prose fiction. It can typically be read in a single sitting and focuses on a self-contained incident or series of linked incidents, with the intent of evoking a single effect or mood.", 
                speaker_wav="sample.wav", 
                language="zh", 
                file_path="output.wav")
