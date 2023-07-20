import cv2
import imageio

video_path = '视频文件路径'   # MP4视频文件路径 
gif_path = '保存的动图路径.gif'     # 输出GIF文件路径

cap = cv2.VideoCapture(video_path)   # 打开MP4视频文件 
frames = []   # 存储每一帧的RGB数据

while(cap.isOpened()):            # 循环读取视频的每一帧
    ret, frame = cap.read()  
    
    if ret == True:            
         
         frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # bgr格式转换为rgb格式
         frames.append(frame_rgb)  # 将RGBA格式的当前帧加入frames列表
    else:  
         break                    

cap.release()                       # 释放VideoCapture   

gif = imageio.mimsave(gif_path, frames, 'GIF', duration = 0.1)     
                                               # 将frames列表中的RGBA帧保存为GIF,duration控制帧率
                                          
print("trans complete")
