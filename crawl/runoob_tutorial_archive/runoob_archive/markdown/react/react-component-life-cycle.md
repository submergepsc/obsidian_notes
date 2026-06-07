# React 组件生命周期

- Source: https://www.runoob.com/react/react-component-life-cycle.html

在本章节中我们将讨论 React 组件的生命周期。


组件的生命周期可分成三个状态：


- Mounting(挂载)：已插入真实 DOM
- Updating(更新)：正在被重新渲染
- Unmounting(卸载)：已移出真实 DOM


![](https://www.runoob.com/wp-content/uploads/2016/02/ogimage.png)


---


## 挂载


当组件实例被创建并插入 DOM 中时，其生命周期调用顺序如下：


- `[constructor()](https://www.runoob.com/react-ref-constructor.html)`: 在 React 组件挂载之前，会调用它的构造函数。
- `[getDerivedStateFromProps()](https://www.runoob.com/react-ref-getderivedstatefromprops.html)`: 在调用 render 方法之前调用，并且在初始挂载及后续更新时都会被调用。
- `[render()](https://www.runoob.com/react-ref-render.html)`: render() 方法是 class 组件中唯一必须实现的方法。
- `[componentDidMount()](https://www.runoob.com/react-ref-componentdidmount.html)`: 在组件挂载后（插入 DOM 树中）立即调用。


render() 方法是 class 组件中唯一必须实现的方法，其他方法可以根据自己的需要来实现。


这些方法的详细说明，可以参考[官方文档](https://zh-hans.reactjs.org/docs/react-component.html#reference)。


---


## 更新


每当组件的 state 或 props 发生变化时，组件就会更新。


当组件的 props 或 state 发生变化时会触发更新。组件更新的生命周期调用顺序如下：


- `[getDerivedStateFromProps()](https://www.runoob.com/react-ref-getderivedstatefromprops.html)`: 在调用 render 方法之前调用，并且在初始挂载及后续更新时都会被调用。根据 shouldComponentUpdate() 的返回值，判断 React 组件的输出是否受当前 state 或 props 更改的影响。
- `[shouldComponentUpdate()](https://www.runoob.com/react-ref-shouldcomponentupdate.html)`:当 props 或 state 发生变化时，shouldComponentUpdate() 会在渲染执行之前被调用。
- `[render()](https://www.runoob.com/react-ref-render.html)`: render() 方法是 class 组件中唯一必须实现的方法。
- `[getSnapshotBeforeUpdate()](https://www.runoob.com/react-ref-getsnapshotbeforeupdate.html)`: 在最近一次渲染输出（提交到 DOM 节点）之前调用。
- `[componentDidUpdate()](https://www.runoob.com/react-ref-componentdidupdate.html)`: 在更新后会被立即调用。


render() 方法是 class 组件中唯一必须实现的方法，其他方法可以根据自己的需要来实现。


这些方法的详细说明，可以参考[官方文档](https://zh-hans.reactjs.org/docs/react-component.html#reference)。


---


## 卸载


当组件从 DOM 中移除时会调用如下方法：


- `[componentWillUnmount()](https://www.runoob.com/react-ref-componentwillunmount.html)`: 在组件卸载及销毁之前直接调用。


这些方法的详细说明，可以参考[官方文档](https://zh-hans.reactjs.org/docs/react-component.html#reference)。


---

## 实例


以下是一个当前时间的实例，每秒更新：


## 实例


```javascript
class Clock extends React.Component {
  constructor(props) {
    super(props);
    this.state = {date: new Date()};
  }

  componentDidMount() {
    this.timerID = setInterval(
      () => this.tick(),
      1000
    );
  }

  componentWillUnmount() {
    clearInterval(this.timerID);
  }

  tick() {
    this.setState({
      date: new Date()
    });
  }

  render() {
    return (
      <div>
        <h1>Hello, Runoob!</h1>
        <h2>现在时间是：{this.state.date.toLocaleTimeString()}.</h2>
      </div>
    );
  }
}

const root = ReactDOM.createRoot(document.body);
root.render(
  <Clock />
);
```

** [尝试一下 »](https://www.runoob.com/try/try.php?filename=try_react_life_cycle_clock)


以下实例在 Hello 组件加载以后，通过 componentDidMount 方法设置一个定时器，每隔100毫秒重新设置组件的透明度，并重新渲染：


## React 实例


```javascript
class Hello extends React.Component {

  constructor(props) {
      super(props);
      this.state = {opacity: 1.0};
  }

  componentDidMount() {
    this.timer = setInterval(function () {
      var opacity = this.state.opacity;
      opacity -= .05;
      if (opacity < 0.1) {
        opacity = 1.0;
      }
      this.setState({
        opacity: opacity
      });
    }.bind(this), 100);
  }

  render () {
    return (
      <div style={{opacity: this.state.opacity}}>
        Hello {this.props.name}
      </div>
    );
  }
}

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <Hello name="world"/>
);
```


 [尝试一下 »](https://www.runoob.com/try/try.php?filename=try_react_life_cycle)


以下实例初始化 state** ， **setNewnumber** 用于更新 **state**。所有生命周期在 **Content** 组件中。


## React 实例


```javascript
class Button extends React.Component {
  constructor(props) {
    super(props);
    this.state = { data: 0 };
    this.setNewNumber = this.setNewNumber.bind(this);
  }

  setNewNumber() {
    this.setState({ data: this.state.data + 1 });
  }

  render() {
    return (
      <div>
        <button onClick={this.setNewNumber}>INCREMENT</button>
        <Content myNumber={this.state.data} />
      </div>
    );
  }
}

class Content extends React.Component {
  componentDidMount() {
    console.log("Component DID MOUNT!");
  }

  shouldComponentUpdate(newProps, newState) {
    return true;
  }

  componentDidUpdate(prevProps, prevState) {
    console.log("Component DID UPDATE!");
  }

  componentWillUnmount() {
    console.log("Component WILL UNMOUNT!");
  }

  render() {
    return (
      <div>
        <h3>{this.props.myNumber}</h3>
      </div>
    );
  }
}

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <div>
    <Button />
  </div>
);
```


** [尝试一下 »](https://www.runoob.com/try/try.php?filename=try_react_life_cycle2)








	  AI 思考中...





			** [React 组件 API](https://www.runoob.com/react-component-api.html)
			[React AJAX](https://www.runoob.com/react-ajax.html) **













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