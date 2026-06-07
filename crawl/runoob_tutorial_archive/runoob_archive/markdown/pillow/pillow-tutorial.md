# Pillow 教程

- Source: https://www.runoob.com/pillow/pillow-tutorial.html

![](https://www.runoob.com/wp-content/uploads/2025/05/pillow-logo-248x250-1.png)

Pillow 是 Python 中处理图像的主要库。


Pillow 是 Python Imaging Library (PIL) 的一个友好分支。


由于原始的 PIL 已经不再维护，Pillow 接替了它的角色并继续活跃开发。


Pillow 提供了广泛的文件格式支持、高效的内部表示以及强大的图像处理功能。


---


## 谁适合阅读本教程？


本教程适合有 Python 基础的开发者学习。


如果您还不了解 Python，可以先学习 [Python 教程](https://www.runoob.com/../python3/python3-tutorial.html)。


---


## 主要特点


- 支持多种图像格式（JPEG, PNG, GIF, BMP, TIFF 等）
- 基本的图像处理操作（旋转、缩放、裁剪等）
- 图像过滤和增强
- 支持图像绘制
- 颜色空间转换


---


## 与其他库的比较


- 相比 OpenCV：Pillow 更专注于图像处理而非计算机视觉，API 更简单
- 相比 Matplotlib：Pillow 更专注于图像处理而非数据可视化
- 相比 scikit-image：Pillow 更基础，更容易上手，适合一般图像处理任务


---


## 第一个 Pillow 实例

安装 Pillow 后，仍然使用 import PIL 或 **from PIL import ...** 来导入模块。


以下实例显示了图片的基本信息：


## 实例


```python
from PIL import Image

# 打开一张图片
img = Image.open("example.jpeg")

# 显示图片
img.show()

# 获取图片信息
print("图片格式:", img.format)  # JPEG, PNG, etc.
print("图片大小:", img.size)    # (width, height)
print("图片模式:", img.mode)   # RGB, L, etc.

# 保存为 PNG 格式
img.save("example.png")
```


运行结果：


```
图片格式: JPEG
图片大小: (987, 987)
图片模式: RGB
```


运行后，图片还会保存为 **example.png**。


---

## 相关内容


- [Pillow 官网](https://python-pillow.github.io/)
- [Pillow 官方文档](https://pillow.readthedocs.io/en/stable/)
- [Pillow GitHub 仓库](https://github.com/python-pillow/Pillow)









	  AI 思考中...






			[Pillow 简介](https://www.runoob.com/pillow-intro.html) **













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