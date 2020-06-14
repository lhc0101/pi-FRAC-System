## ！该项目已停止维护！

# facerec-python

## 基于树莓派、OpenCV及Python语言的人脸识别门禁系统

### 简介

  使用OpenCV for Python图像识别库，运行在树莓派RASPBIAN JESSIE Linux系统平台上，搭配树莓派官方摄像头模块。
  
### 运行要求
  1. OpenCV 2.4.9 for Python
  2. Python 2.7
  3. v4l2
  4. PyQt4
  
### 安装要求

  ```bash
  sudo apt-get install build-essential cmake pkg-config python-dev libgtk2.0-dev libgtk2.0 zlib1g-dev libpng-dev libjpeg-dev libtiff-dev libjasper-dev libavcodec-dev swig unzip
  ```

  1. 启用v4l2
  ```bash
  sudo nano /etc/modules
  # 增加一行记录
  bcm2835-v4l2
  # 重启后可以找到/dev/video0
  
  # 编译v4l2-util
  apt-get install autoconf gettext libtool libjpeg8 libjpeg8-dev
  git clone git://git.linuxtv.org/v4l-utils.git
  cd v4l-utils/
  sudo ./bootstrap.sh
  ./configure
  make
  sudo make install
  ```
 
  2. 编译OpenCV 2.4.9
 
  ```bash
  wget https://jaist.dl.sourceforge.net/project/opencvlibrary/opencv-unix/2.4.9/opencv-2.4.9.zip
  unzip opencv-2.4.9.zip
  cd opencv-2.4.9/
  cmake -DCMAKE_BUILD_TYPE=RELEASE -DCMAKE_INSTALL_PREFIX=/usr/local -DBUILD_PERF_TESTS=OFF -DBUILD_opencv_gpu=OFF -DBUILD_opencv_ocl=OFF
  
  # 要使OpenCV开启对v4l2的支持 cmake之后要有以下输出
  # V4L/V4L2:                    Using libv4l (ver 1.13.0)
  
  sudo make
  sudo make install
  ```
  
  3. 安装PyQt4
  ```bash
  sudo apt-get install python-qt4
  ```
  
  4. 运行
  ```bash
  python main.py
  ```
  
### 注意
  
  该示例运行的屏幕分辨率为竖屏480 x 800，可以修改 /boot/config.txt 的以下配置
  
  [config.txt配置说明](https://www.raspberrypi.org/documentation/configuration/config-txt.md)
  ```bash
  hdmi_cvt=800 480 60 6
  hdmi_group=2
  hdmi_mode=87
  # 设置屏幕旋转角度
  display_rotate=3
  ```

### 补充说明：

上面是老项目的说明，有点繁琐~

我太懒了 ，突击突击一周搞出来的玩意，不想详细说说

首先，代码老的，是基于老项目改的，应朋友要求改了下。
原来的代码有个bug，只能录入人脸不能超过10个，修改了下。
增加邮件通知功能
增加二次密码认证功能

条件苛刻，只能树莓派3B 高版本也不行，树莓派系统版本错了也有问题。

摄像头，usb 免驱的就能用，还不用 v4l2-util 编译安装

注意屏幕分辨率的问题，尝试改一改就应该能解决乱七八糟的问题

如果遇到摄像头获取不到图像，那应该是某个环境变量的问题，网上有教程。

关于镜像，自己琢磨下换到国内的源，还要注意你换的源版本对不对，老镜像有两个版本的哈！

### 补充演示视频、系统镜像链接

链接：https://pan.baidu.com/s/187kV-HLwCW5MCMVoZgXORw 
提取码：bx7j

链接：https://pan.baidu.com/s/19jcx1sK_tnNn27qRsOfqPw 
提取码：w5qe 

### 补充安装说明

```
树莓派3B
Jessie 2017-4-10版本

软件/库版本：
python==2.7.9
opencv==2.4.9

注意
该程序运行的屏幕分辨率为竖屏480 x 800，需要修改 /boot/config.txt 的以下配置
hdmi_cvt=800 480 60 6
hdmi_group=2
hdmi_mode=87
# 设置屏幕旋转角度
display_rotate=3


安装要求：
请将源码文件raspbianfacerecog.zip放置在pi@raspberrypi:~根目录下（与Desktop一起）
unzip raspbianfacerecog.zip

第一步
#安装依赖库
sudo apt-get install build-essential cmake pkg-config python-dev libgtk2.0-dev libgtk2.0 zlib1g-dev libpng-dev libjpeg-dev libtiff-dev libjasper-dev libavcodec-dev swig unzip

第二步
sudo nano /etc/modules
# 增加下面这行
bcm2835-v4l2
#保存后退出

第三步
# 安装依赖库
apt-get install autoconf gettext libtool libjpeg8 libjpeg8-dev
#下载
git clone git://git.linuxtv.org/v4l-utils.git
#授予权限给文档
chmod 777 v4l-utils/
#打开文件夹
cd v4l-utils/
#安装
sudo ./bootstrap.sh 
#编译1
sudo ./configure
#编译2
sudo make
#安装
sudo make install

第四步
#安装OpenCV 2.4.9，下载
wget https://jaist.dl.sourceforge.net/project/opencvlibrary/opencv-unix/2.4.9/opencv-2.4.9.zip
#解压缩
unzip opencv-2.4.9.zip
#打开目录
cd opencv-2.4.9/
#编译
sudo cmake -DCMAKE_BUILD_TYPE=RELEASE -DCMAKE_INSTALL_PREFIX=/usr/local -DBUILD_PERF_TESTS=OFF -DBUILD_opencv_gpu=OFF -DBUILD_opencv_ocl=OFF
#编译
sudo make
#安装
sudo make install

第五步
#安装PyQt4
sudo apt-get install python-qt4

第六步
#打开源码所在文件夹
cd raspbianfacerecog
#运行
sudo python main.py

```

