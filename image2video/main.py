import cv2  
import os  
  
# 图片文件夹路径  
img_folder_path = 'path/to/image/folder'  
# 视频输出路径和文件名  
video_output_path = 'path/to/output/video.mp4'  
# 视频帧率  
fps = 30  
  
# 读取所有图片文件名  
img_files = sorted(os.listdir(img_folder_path))  
  
# 获取第一张图片的大小作为视频大小  
img = cv2.imread(os.path.join(img_folder_path, img_files[0]))  
height, width, channels = img.shape  
  
# 创建视频编码器对象  
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  
video_writer = cv2.VideoWriter(video_output_path, fourcc, fps, (width, height))  
  
# 将每张图片添加到视频中  
for img_file in img_files:  
    img_path = os.path.join(img_folder_path, img_file)  
    img = cv2.imread(img_path)  
    video_writer.write(img)  
  
# 释放视频编码器对象  
video_writer.release()