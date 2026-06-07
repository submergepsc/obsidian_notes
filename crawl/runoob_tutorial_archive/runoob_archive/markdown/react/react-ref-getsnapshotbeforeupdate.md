# React getSnapshotBeforeUpdate() 方法

- Source: https://www.runoob.com/react/react-ref-getsnapshotbeforeupdate.html

[![React 组件生命周期](https://www.runoob.com/images/up.gif) React 组件生命周期](https://www.runoob.com/react-component-life-cycle.html)


getSnapshotBeforeUpdate() 方法格式如下：


```
getSnapshotBeforeUpdate(prevProps, prevState)
```


getSnapshotBeforeUpdate() 方法在最近一次渲染输出（提交到 DOM 节点）之前调用。


在 getSnapshotBeforeUpdate() 方法中，我们可以访问更新前的 props 和 state。


getSnapshotBeforeUpdate() 方法需要与 componentDidUpdate() 方法一起使用，否则会出现错误。


以下实例使用 **getSnapshotBeforeUpdate()** 方法查看更新前 state 对象的值，实例会在 1 秒延迟后显示更新前与更新后的不同值：


## 实例


```javascript
class Header extends React.Component {
  constructor(props) {
    super(props);
    this.state = {favoritesite: "runoob"};
  }
  componentDidMount() {
    setTimeout(() => {
      this.setState({favoritesite: "google"})
    }, 1000)
  }
  getSnapshotBeforeUpdate(prevProps, prevState) {
    document.getElementById("div1").innerHTML =
    "在更新前喜欢的网站是：" + prevState.favoritesite;
  }
  componentDidUpdate() {
    document.getElementById("div2").innerHTML =
    "更新后喜欢的网站是：" + this.state.favoritesite;
  }
  render() {
    return (
      <div>
        <h1>我喜欢的网站是 {this.state.favoritesite}</h1>
        <div id="div1"></div>
        <div id="div2"></div>
      </div>
    );
  }
}

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<Header />);
```


** [尝试一下 »](https://www.runoob.com/try/try.php?filename=try_react_life_cycle9)


[![React 组件生命周期](https://www.runoob.com/images/up.gif) React 组件生命周期](https://www.runoob.com/react-component-life-cycle.html)








	  AI 思考中...





			** [React shouldComponentUpdate() 方法](https://www.runoob.com/react-ref-shouldcomponentupdate.html)
			[React componentDidUpdate() 方法](https://www.runoob.com/react-ref-componentdidupdate.html) **













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