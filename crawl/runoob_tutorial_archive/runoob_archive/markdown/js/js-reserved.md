# JavaScript 保留关键字

- Source: https://www.runoob.com/js/js-reserved.html

---


在 JavaScript 中，一些标识符是保留关键字，不能用作变量名或函数名。


---


## JavaScript 标准


所有的现代浏览器完全支持 ECMAScript 3（ES3，JavaScript 的第三版，从 1999 年开始）。


ECMAScript 4（ES4）未通过。


ECMAScript 5（ES5，2009 年发布）。


ECMAScript 6（ES6，2015 年发布），是 JavaScript 最新的官方版本。


随着时间的推移，我们开始看到，所有的现代浏览器已经完全支持 ES6。


---


## JavaScript 保留关键字


Javascript 的保留关键字不可以用作变量、标签或者函数名。有些保留关键字是作为 Javascript 以后扩展使用。


| abstract | arguments | boolean | break | byte |
| --- | --- | --- | --- | --- |
| case | catch | char | class* | const |
| continue | debugger | default | delete | do |
| double | else | enum* | eval | export* |
| extends* | false | final | finally | float |
| for | function | goto | if | implements |
| import* | in | instanceof | int | interface |
| let | long | native | new | null |
| package | private | protected | public | return |
| short | static | super* | switch | synchronized |
| this | throw | throws | transient | true |
| try | typeof | var | void | volatile |
| while | with | yield |  |  |


* 标记的关键字是 ECMAScript5 中新添加的。


---


## JavaScript 对象、属性和方法


您也应该避免使用 JavaScript 内置的对象、属性和方法的名称作为 Javascript 的变量或函数名：


| Array | Date | eval | function | hasOwnProperty |
| --- | --- | --- | --- | --- |
| Infinity | isFinite | isNaN | isPrototypeOf | length |
| Math | NaN | name | Number | Object |
| prototype | String | toString | undefined | valueOf |


---


## Java 保留关键字


JavaScript 经常与 Java 一起使用。您应该避免使用一些 Java 对象和属性作为 JavaScript 标识符：


| getClass | java | JavaArray | javaClass | JavaObject | JavaPackage |
| --- | --- | --- | --- | --- | --- |


---


## Window 保留关键字


JavaScript 可以在 HTML 外部使用。它可在许多其他应用程序中作为编程语言使用。


在 HTML 中，您必须（为了可移植性，您也应该这么做）避免使用 HTML 和 Window 对象和属性的名称作为 Javascript 的变量及函数名：


| alert | all | anchor | anchors | area |
| --- | --- | --- | --- | --- |
| assign | blur | button | checkbox | clearInterval |
| clearTimeout | clientInformation | close | closed | confirm |
| constructor | crypto | decodeURI | decodeURIComponent | defaultStatus |
| document | element | elements | embed | embeds |
| encodeURI | encodeURIComponent | escape | event | fileUpload |
| focus | form | forms | frame | innerHeight |
| innerWidth | layer | layers | link | location |
| mimeTypes | navigate | navigator | frames | frameRate |
| hidden | history | image | images | offscreenBuffering |
| open | opener | option | outerHeight | outerWidth |
| packages | pageXOffset | pageYOffset | parent | parseFloat |
| parseInt | password | pkcs11 | plugin | prompt |
| propertyIsEnum | radio | reset | screenX | screenY |
| scroll | secure | select | self | setInterval |
| setTimeout | status | submit | taint | text |
| textarea | top | unescape | untaint | window |


---


## HTML 事件句柄


除此之外，您还应该避免使用 HTML 事件句柄的名称作为 Javascript 的变量及函数名。


实例：


| onblur | onclick | onerror | onfocus |
| --- | --- | --- | --- |
| onkeydown | onkeypress | onkeyup | onmouseover |










	  AI 思考中...





			** [JavaScript 总结](https://www.runoob.com/js-summary.html)
			[JavaScript HTML DOM EventListener](https://www.runoob.com/js-htmldom-eventlistener.html) **