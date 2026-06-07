# OpenCV 教程

- Source: https://www.runoob.com/opencv/opencv-tutorial.html

![](https://www.runoob.com/wp-content/uploads/2025/01/open-cv.png)


OpenCV（Open Source Computer Vision Library）是一个开源的计算机视觉和机器学习软件库。

OpenCV 由一系列 C 函数和少量 C++ 类构成，同时提供了 Python、Java、MATLAB 等语言的接口。

OpenCV 提供了大量的计算机视觉算法和图像处理工具，广泛应用于图像和视频的处理、分析以及机器学习领域。

OpenCV 的设计目标是提供一套简单易用的计算机视觉基础库，帮助开发人员快速构建复杂的视觉应用。


---

## 学习本教程前你需要了解


OpenCV 支持多种编程语言，但 Python 和 C++ 是最常用的两种，Python 语法简单易学，适合初学者。


在开学习 OpenCV 教程之前，我们需要具备基本的 Python 基础，如果你对 Python 还不了解，可以阅读我们的教程：


- [Python 3.x 教程](https://www.runoob.com/../python3/python3-tutorial.html)
- [Numpy 教程](https://www.runoob.com/../numpy/numpy-tutorial.html)


---

## 历史发展

OpenCV 项目最早由英特尔公司于 1999 年启动，致力于 CPU 密集型的任务，是一个包括如光线追踪和 3D 显示的计划的一部分。


- 1999 年，OpenCV 项目由 Intel 研究院启动，旨在促进计算机视觉的研究和应用。
- 2000 年，OpenCV 第一个版本发布。
- 2006 年，OpenCV 1.0 版本发布。
- 2009 年，OpenCV 2.0 版本发布，增加了对 Python 的支持。
- 2015 年，OpenCV 3.0 版本发布，增加了对深度学习的支持。
- 2018 年，OpenCV 4.0 版本发布，进一步优化了性能和功能。


---

## 实例

OpenCV 读取并显示一张图像:


## 实例


```python
# 导入 OpenCV 库，并使用别名 cv 代替 cv2
import cv2 as cv

# 将 "path/to/image" 替换为实际的图像路径，例如 "cat.jpg" 或 "C:/images/dog.png"
img = cv.imread("path/to/image")

# 如果图像路径错误或文件不存在，cv.imread() 会返回 None
if img is None:
    # 打印错误信息
    print("Error: Could not load image.")
    # 退出程序
    exit()

# "Display window" 是显示窗口的名称，可以自定义
# img 是要显示的图像数据
cv.imshow("Display window", img)

# 等待按键输入
# 参数 0 表示无限等待，直到用户按下任意键
# 返回值 k 是用户按下的键的 ASCII 码值
k = cv.waitKey(0)

# 检查用户是否按下 Esc 键（ASCII 码为 27）
if k == 27:
    # 关闭所有 OpenCV 窗口
    cv.destroyAllWindows()
```


---

## 相关链接

- OpenCV 官网 [https://opencv.org/](https://opencv.org/)
- OpenCV 源代码：[https://github.com/opencv/opencv](https://github.com/opencv/opencv)
- OpenCV 文档：[https://docs.opencv.org/](https://docs.opencv.org/)








	  AI 思考中...






			[OpenCV 简介](https://www.runoob.com/opencv-intro.html) **













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