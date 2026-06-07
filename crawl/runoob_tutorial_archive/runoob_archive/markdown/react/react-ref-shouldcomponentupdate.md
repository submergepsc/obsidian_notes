# React shouldComponentUpdate() 方法

- Source: https://www.runoob.com/react/react-ref-shouldcomponentupdate.html

[![React 组件生命周期](https://www.runoob.com/images/up.gif) React 组件生命周期](https://www.runoob.com/react-component-life-cycle.html)


shouldComponentUpdate() 方法格式如下：


```
shouldComponentUpdate(nextProps, nextState)
```


shouldComponentUpdate() 方法会返回一个布尔值，指定 React 是否应该继续渲染，默认值是 **true**， 即 **state** 每次发生变化组件都会重新渲染。


shouldComponentUpdate() 的返回值用于判断 React 组件的输出是否受当前 state 或 props 更改的影响，当 props 或 state 发生变化时，shouldComponentUpdate() 会在渲染执行之前被调用。


以下实例演示了 shouldComponentUpdate() 方法返回 false 时执行的操作（点击按钮无法修改）：


## 实例


```javascript
class Header extends React.Component {
  constructor(props) {
    super(props);
    this.state = {favoritesite: "runoob"};
  }
  shouldComponentUpdate() {
    return false;
  }
  changeSite = () => {
    this.setState({favoritesite: "google"});
  }
  render() {
    return (
      <div>
      <h1>我喜欢的网站是 {this.state.favoritesite}</h1>
      <button type="button" onClick={this.changeSite}>修改</button>
      </div>
    );
  }
}
```


** [尝试一下 »](https://www.runoob.com/try/try.php?filename=try_react_life_cycle7)


以下实例演示了 shouldComponentUpdate() 方法返回 true 时执行的操作（点击按钮可以修改）：


## 实例


```javascript
class Header extends React.Component {
  constructor(props) {
    super(props);
    this.state = {favoritesite: "runoob"};
  }
  shouldComponentUpdate() {
    return true;
  }
  changeSite = () => {
    this.setState({favoritesite: "google"});
  }
  render() {
    return (
      <div>
      <h1>我喜欢的网站是 {this.state.favoritesite}</h1>
      <button type="button" onClick={this.changeSite}>修改</button>
      </div>
    );
  }
}
```


 [尝试一下 »](https://www.runoob.com/try/try.php?filename=try_react_life_cycle8)


[![React 组件生命周期](https://www.runoob.com/images/up.gif) React 组件生命周期](https://www.runoob.com/react-component-life-cycle.html)








	  AI 思考中...





			** [React componentDidMount() 方法](https://www.runoob.com/react-ref-componentdidmount.html)
			[React getSnapshotBeforeUpdate() 方法](https://www.runoob.com/react-ref-getsnapshotbeforeupdate.html) **













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