# C++ OpenCV

- Source: https://www.runoob.com/cplusplus/cpp-opencv.html

OpenCV（Open Source Computer Vision Library）是一个开源的计算机视觉和机器学习软件库，它由一系列 C 函数和少量 C++ 类构成，同时提供了 Python、Java 和 MATLAB 等语言的接口。

OpenCV 的设计目标是提供一套通用的计算机视觉库，帮助开发者快速构建复杂的视觉应用。


OpenCV 最初由 Intel 开发，后来由 Willow Garage 和 Itseez 支持，现在由 OpenCV.org 维护。

OpenCV 广泛应用于图像处理、视频分析、物体检测、人脸识别、机器学习等领域。


### OpenCV 的核心功能

OpenCV 的核心功能包括：


- **图像处理**：如图像滤波、几何变换、颜色空间转换、边缘检测等。
- **视频处理**：如视频捕获、背景减除、光流计算等。
- **特征检测与描述**：如 SIFT、SURF、ORB 等算法。
- **目标检测与跟踪**：如 Haar 级联检测、HOG 检测、深度学习模型等。
- **相机标定与 3D 重建**：如相机标定、立体视觉、点云处理等。
- **机器学习**：如 KNN、SVM、决策树等传统机器学习算法。
- **深度学习**：支持加载和运行 TensorFlow、PyTorch、Caffe 等框架的模型。


### OpenCV 的模块结构

OpenCV 的功能被组织成多个模块，每个模块专注于不同的任务。以下是主要模块的简介：


| 模块名称 | 功能描述 |
| --- | --- |
| Core | 提供基本数据结构和函数，如图像存储、矩阵操作、文件 I/O 等。 |
| Imgproc | 图像处理功能，包括滤波、几何变换、颜色空间转换、边缘检测、形态学操作等。 |
| Highgui | 图像和视频的显示、窗口管理、用户交互（如鼠标事件、滑动条）。 |
| Video | 视频处理功能，包括视频捕获、背景减除、光流计算等。 |
| Calib3d | 相机标定、3D 重建、姿态估计等。 |
| Features2d | 特征检测与描述，包括关键点检测、特征匹配等。 |
| Objdetect | 目标检测功能，如 Haar 级联检测、HOG 检测等。 |
| DNN | 深度学习模型的加载和推理，支持 TensorFlow、PyTorch、Caffe 等框架。 |
| ML | 机器学习算法，如 KNN、SVM、决策树等。 |
| Flann | 快速近似最近邻搜索（FLANN），用于特征匹配和高维数据搜索。 |
| Photo | 图像修复、去噪、HDR 成像等。 |
| Stitching | 图像拼接功能，用于创建全景图。 |
| Shape | 形状分析和匹配。 |
| Tracking | 目标跟踪算法，如 MIL、KCF、GOTURN 等。 |


---


## OpenCV 的主要模块


OpenCV 库由多个模块组成，每个模块专注于不同的功能。以下是 OpenCV 中的一些主要模块：


### 1. Core 模块


Core 模块是 OpenCV 的核心模块，包含了最基本的数据结构和函数。它定义了 OpenCV 中最常用的数据类型，如 `Mat`（矩阵）、`Point`、`Rect` 等。Core 模块还提供了基本的数学运算、内存管理、文件 I/O 等功能。


- **Mat 类**：`Mat` 是 OpenCV 中最常用的数据结构，用于存储图像和矩阵数据。它是一个多维数组，可以表示灰度图像、彩色图像、3D 矩阵等。
- **基本操作**：Core 模块提供了矩阵的加减乘除、转置、求逆等基本操作。


### 2. Imgproc 模块


Imgproc 模块是图像处理模块，提供了大量的图像处理函数。这些函数可以用于图像的滤波、几何变换、颜色空间转换、直方图计算等。


- **图像滤波**：包括均值滤波、高斯滤波、中值滤波等，用于去除图像中的噪声。
- **几何变换**：如图像的缩放、旋转、仿射变换等。
- **边缘检测**：如 Canny 边缘检测、Sobel 算子等。
- **直方图均衡化**：用于增强图像的对比度。


### 3. Highgui 模块


Highgui 模块提供了图形用户界面（GUI）功能，允许开发者创建窗口、显示图像、处理鼠标和键盘事件等。


- **图像显示**：使用 `imshow` 函数可以在窗口中显示图像。
- **视频捕获**：使用 `VideoCapture` 类可以从摄像头或视频文件中捕获视频帧。
- **事件处理**：可以处理鼠标点击、键盘输入等事件。


### 4. Video 模块


Video 模块专注于视频分析，提供了视频捕获、背景减除、光流计算等功能。


- **视频捕获**：使用 `VideoCapture` 类可以从摄像头或视频文件中读取视频帧。
- **背景减除**：用于从视频中提取前景物体。
- **光流计算**：用于估计图像中物体的运动。


### 5. Calib3d 模块


Calib3d 模块提供了相机校准、3D 重建、立体视觉等功能。它主要用于处理与相机相关的几何问题。


- **相机校准**：用于估计相机的内参和外参。
- **3D 重建**：从多张图像中重建三维场景。
- **立体视觉**：用于计算深度图。


### 6. Features2d 模块


Features2d 模块提供了特征检测和描述符提取的功能。它包含了多种特征检测算法，如 SIFT、SURF、ORB 等。


- **特征检测**：检测图像中的关键点。
- **描述符提取**：为每个关键点生成描述符，用于匹配不同图像中的特征。


### 7. Objdetect 模块


Objdetect 模块提供了物体检测的功能，特别是基于 Haar 特征和 LBP 特征的级联分类器。


- **人脸检测**：使用 Haar 特征和级联分类器检测图像中的人脸。
- **物体检测**：可以检测其他类型的物体，如眼睛、车辆等。


### 8. ML 模块


ML 模块是机器学习模块，提供了多种机器学习算法，如支持向量机（SVM）、K 近邻（KNN）、决策树等。


- **分类**：使用 SVM、KNN 等算法进行分类。
- **回归**：使用线性回归等算法进行回归分析。
- **聚类**：使用 K-means 等算法进行聚类分析。


### 9. DNN 模块


DNN 模块是深度学习模块，提供了加载和运行深度学习模型的功能。它支持多种深度学习框架，如 TensorFlow、Caffe、ONNX 等。


- **模型加载**：可以加载预训练的深度学习模型。
- **推理**：使用加载的模型进行图像分类、目标检测等任务。

---


## OpenCV 的安装与配置


在使用 OpenCV 之前，需要先安装并配置好开发环境。
以下是安装 OpenCV 的基本步骤：

### 3.1 安装 OpenCV


在 Linux 系统上，可以使用包管理器安装 OpenCV：


```
sudo apt-get install libopencv-dev
```


在 Windows 系统上，可以从 OpenCV 官网下载预编译的库，或者使用 vcpkg 进行安装。


### 配置开发环境


在 C++ 项目中使用 OpenCV 时，需要在编译时链接 OpenCV 库。

以下是一个简单的 CMake 配置示例：


```
cmake_minimum_required(VERSION 3.10)
project(OpenCVExample)

find_package(OpenCV REQUIRED)

add_executable(OpenCVExample main.cpp)

target_link_libraries(OpenCVExample ${OpenCV_LIBS})
```


## 一个简单的 OpenCV 示例


以下是一个使用 OpenCV 读取并显示图像的简单示例：


## 实例


```cpp
#include <opencv2/opencv.hpp>
#include <iostream>

int main() {
    // 读取图像
    cv::Mat image = cv::imread("example.jpg");

    // 检查图像是否成功加载
    if (image.empty()) {
        std::cout << "无法加载图像！" << std::endl;
        return -1;
    }

    // 创建窗口并显示图像
    cv::namedWindow("Example", cv::WINDOW_AUTOSIZE);
    cv::imshow("Example", image);

    // 等待按键
    cv::waitKey(0);

    return 0;
}
```


以上代码中，我们使用 `imread` 函数读取图像，使用 `imshow` 函数显示图像，并使用 `waitKey` 函数等待用户按键。


---


## OpenCV 相关内容


| 序号 | 内容 |
| --- | --- |
| 1 | C++ OpenCV 安装 |
| 2 | C++ OpenCV 基础操作 |
| 3 | C++ Opencv 图像处理 |
| 4 | C++ OpenCV 基本模块 |
| 5 | C++ OpenCV 特征检测与描述 |
| 6 | C++ Opencv 高级图像处理 |
| 7 | C++ OpenCV 视频处理 |
| 8 | C++ OpenCV 机器学习与深度学习 |
| 9 | C++ OpenCV 项目实战 |








	  AI 思考中...





			** [C++ 导入标准库](https://www.runoob.com/cppo-import-header-file.html)
			[C++  push_back 函数](https://www.runoob.com/cpp-libs-vector-push_back.html) **













### 点我分享笔记







				**
取消






					*


					* 分享笔记






- 昵称昵称 (必填)
- 邮箱邮箱 (必填)
- 引用地址引用地址






































**在线实例**

      : ·[HTML 实例](https://www.runoob.com/../html/html-examples.html)

      : ·[CSS 实例](https://www.runoob.com/../css/css-examples.html)

      : ·[JavaScript 实例](https://www.runoob.com/../js/js-examples.html)

      : ·[Ajax 实例](https://www.runoob.com/../ajx/ajax-examples.html)

       : ·[jQuery 实例](https://www.runoob.com/../jquery/jquery-examples.html)

      : ·[XML 实例](https://www.runoob.com/../xml/xml-examples.html)

      : ·[Java 实例](https://www.runoob.com/../java/java-examples.html)





**字符集&工具**

      : · [HTML 字符集设置](https://www.runoob.com/../charsets/html-charsets.html)

      : · [HTML ASCII 字符集](https://www.runoob.com/../tags/html-ascii.html)

     : · [JS 混淆/加密](https://www.jyshare.com/front-end/6939/)

      : · [PNG/JPEG 图片压缩](https://www.jyshare.com/front-end/6232/)

      : · [HTML 拾色器](https://www.runoob.com/../tags/html-colorpicker.html)

      : · [JSON 格式化工具](https://www.jyshare.com/front-end/53)

      : · [随机数生成器](https://www.jyshare.com/front-end/6680/)




**最新更新**

                  : · [VS Code 创建与...](https://www.runoob.com/../skills/vs-code-skill.html)

                      : · [Skills 脚本扩展](https://www.runoob.com/../skills/skills-scripts.html)

                      : · [Skills 描述](https://www.runoob.com/../skills/skills-description.html)

                      : · [SKILL.md 文件](https://www.runoob.com/../skills/skill-md-file.html)

                      : · [使用现有 Skills](https://www.runoob.com/../skills/use-existing-skills.html)

                      : · [Skills 工作原理](https://www.runoob.com/../skills/how-skills-work.html)

                      : · [第一个 Skill](https://www.runoob.com/../skills/skills-first.html)




**站点信息**

      : · [意见反馈](https://www.runoob.com/../cdn-cgi/l/email-protection/index.html)

      : · [免责声明](https://www.runoob.com/../disclaimer/index.html)

      : · [关于我们](https://www.runoob.com/../aboutus/index.html)

      : · [文章归档](https://www.runoob.com/../archives/index.html)







         关注微信**



      ![](https://www.runoob.com/wp-content/themes/runoob/assets/images/qrcode.png)






     Copyright © 2013-2026    **[菜鸟教程](https://www.runoob.com/../index/index.html)**
    **[runoob.com](https://www.runoob.com/../index/index.html)** All Rights Reserved. 备案号：[闽ICP备15012807号-1](https://beian.miit.gov.cn/)



    **
    **
    **