# Flutter 图片与资源

- Source: https://www.runoob.com/flutter/flutter-images.html

本节将介绍 Flutter 中图片加载、本地资源管理和网络图片处理。


---


## Image Widget - 图片显示


## 实例：各种图片加载方式


```
// 从网络加载图片
Image.network(
  'https://example.com/image.png',
  width: 200,
  height: 200,
  fit: BoxFit.cover,
)

// 从本地资源加载图片
Image.asset('assets/images/logo.png')

// 从本地文件加载图片
Image.file(File('path/to/image.png'))

// 带加载状态的图片
Image.network(
  'https://example.com/image.png',
  loadingBuilder: (context, child, loadingProgress) {
    if (loadingProgress == null) return child;
    return Center(
      child: CircularProgressIndicator(
        value: loadingProgress.expectedTotalBytes != null
            ? loadingProgress.cumulativeBytesLoaded /
                loadingProgress.expectedTotalBytes!
            : null,
      ),
    );
  },
)

// 带错误处理的图片
Image.network(
  'https://example.com/image.png',
  errorBuilder: (context, error, stackTrace) {
    return const Icon(Icons.error, size: 50);
  },
)
```


## 本地资源管理


在 pubspec.yaml 中配置资源文件夹：


```
flutter:
  assets:
    - assets/images/
    - assets/data.json
```


## 实例：使用本地资源


```
// 使用本地图片
class AssetImageExample extends StatelessWidget {
  const AssetImageExample({super.key});

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        // 使用 Image.asset 加载
        const Image(
          image: AssetImage('assets/images/logo.png'),
          width: 100,
        ),
        // 简写形式
        const Image.asset('assets/images/icon.png', width: 50),
        const SizedBox(height: 20),
        // 使用图片 fit
        Container(
          width: 200,
          height: 100,
          decoration: BoxDecoration(
            image: const DecorationImage(
              image: AssetImage('assets/images/bg.jpg'),
              fit: BoxFit.cover,
            ),
            border: Border.all(color: Colors.grey),
          ),
        ),
      ],
    );
  }
}
```


---


## BoxFit 图像适配


| 值 | 说明 |
| --- | --- |
| fill | 拉伸填满（可能变形） |
| contain | 等比缩放，最大化适应 |
| cover | 等比缩放，完全覆盖 |
| fitWidth | 等比缩放，宽度填满 |
| fitHeight | 等比缩放，高度填满 |
| none | 居中显示原始尺寸 |
| scaleDown | contain 且不超过原始尺寸 |


---


## CachedNetworkImage - 图片缓存


使用 cached_network_image 包实现图片缓存。


### 添加依赖


```
dependencies:
  cached_network_image: ^3.0.0
```


## 实例：CachedNetworkImage


```
import 'package:cached_network_image/cached_network_image.dart';

class CachedImageExample extends StatelessWidget {
  const CachedImageExample({super.key});

  @override
  Widget build(BuildContext context) {
    return CachedNetworkImage(
      imageUrl: 'https://example.com/image.png',
      // 加载中显示
      placeholder: (context, url) => const CircularProgressIndicator(),
      // 错误显示
      errorWidget: (context, url, error) => const Icon(Icons.error),
      // 图片适配
      fit: BoxFit.cover,
      // 宽度高度
      width: 200,
      height: 200,
      // 圆形图片
      imageBuilder: (context, imageProvider) => CircleAvatar(
        backgroundImage: imageProvider,
      ),
    );
  }
}
```


**

对于网络图片，建议使用 CachedNetworkImage，它可以自动缓存图片，提高加载性能。










	  AI 思考中...





			** [Flutter 本地存储](https://www.runoob.com/flutter-storage.html)
			[Flutter 调试与 DevTools](https://www.runoob.com/flutter-devtools.html) **













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