# -*- coding: utf-8 -*-
# 主程序，加载显示界面，载入识别模型等
import sys
import cv2

from ui import mainwindow
from camera import Video
from configure import config

from PyQt4.QtGui import QApplication

def main():
    
    model = cv2.createLBPHFaceRecognizer() #载入人脸识别模型
    model.load(config.TRAINING_FILE)
    
    video = Video.Video(0)  #接受摄像头视频流
    video.setFrameSize(640, 480)  #设置画面大小
    video.setFPS(30) #设置视频帧率
    
    QtApp = QApplication(sys.argv)
    
    mainWindow = mainwindow.Ui_MainWindow()
    mainWindow.setModel(model)
    mainWindow.showFullScreen()
    mainWindow.setVideo(video)
    mainWindow.raise_()
    
    QtApp.exec_()

if __name__ == '__main__':
    main()
