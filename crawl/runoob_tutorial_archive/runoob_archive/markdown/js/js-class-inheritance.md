# JavaScript 类继承

- Source: https://www.runoob.com/js/js-class-inheritance.html

JavaScript 类继承使用 extends 关键字。


继承允许我们依据另一个类来定义一个类，这使得创建和维护一个应用程序变得更容易。


**super()** 方法用于调用父类的构造函数。


当创建一个类时，您不需要重新编写新的数据成员和成员函数，只需指定新建的类继承了一个已有的类的成员即可。这个已有的类称为**基类（父类）**，新建的类称为**派生类（子类）**。


继承代表了 **is a** 关系。例如，哺乳动物是动物，狗是哺乳动物，因此，狗是动物，等等。


![](https://www.runoob.com/wp-content/uploads/2015/05/cpp-inheritance-2020-12-15-1.png)


代码如下：


```javascript
// 基类
class Animal {
    // eat() 函数
    // sleep() 函数
};

//派生类
class Dog extends Animal {
    // bark() 函数
};
```


以下实例创建的类 "Runoob" 继承了 "Site" 类:


## 实例


```javascript
class Site {
  constructor(name) {
    this.sitename = name;
  }
  present() {
    return '我喜欢' + this.sitename;
  }
}

class Runoob extends Site {
  constructor(name, age) {
    super(name);
    this.age = age;
  }
  show() {
    return this.present() + ', 它创建了 ' + this.age + ' 年。';
  }
}

let noob = new Runoob("菜鸟教程", 5);
document.getElementById("demo").innerHTML = noob.show();
```


**
[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryjs_classes_inherit)


**super()** 方法引用父类的构造方法。


通过在构造方法中调用 **super()** 方法，我们调用了父类的构造方法，这样就可以访问父类的属性和方法。


继承对于代码可复用性很有用。


JavaScript 并没有像其他编程语言一样具有传统的类，而是基于原型的继承模型。


ES6 引入了类和 **class** 关键字，但底层机制仍然基于原型继承。


### 使用原型链继承


在下面实例中，Animal 是一个基类，Dog 是一个继承自 Animal 的子类，Dog.prototype 使用 Object.create(Animal.prototype) 来创建一个新对象，它继承了 Animal.prototype 的方法和属性，通过将 Dog.prototype.constructor 设置为 Dog，确保继承链上的构造函数正确。


## 实例


```javascript
function Animal(name) {
  this.name = name;
}

Animal.prototype.eat = function() {
  console.log(this.name + " is eating.");
};

function Dog(name, breed) {
  Animal.call(this, name);
  this.breed = breed;
}

// 建立原型链，让 Dog 继承 Animal
Dog.prototype = Object.create(Animal.prototype);
Dog.prototype.constructor = Dog;

Dog.prototype.bark = function() {
  console.log(this.name + " is barking.");
};

var dog = new Dog("Buddy", "Labrador");
dog.eat();  // 调用从 Animal 继承的方法
dog.bark(); // 调用 Dog 的方法
```


### 使用 ES6 类继承


ES6 引入了 class 关键字，使得定义类和继承更加清晰，extends 关键字用于建立继承关系，super 关键字用于在子类构造函数中调用父类的构造函数。


## 实例


```javascript
class Animal {
  constructor(name) {
    this.name = name;
  }

  eat() {
    console.log(this.name + " is eating.");
  }
}

class Dog extends Animal {
  constructor(name, breed) {
    super(name);
    this.breed = breed;
  }

  bark() {
    console.log(this.name + " is barking.");
  }
}

const dog = new Dog("Buddy", "Labrador");
dog.eat();
dog.bark();
```


不论是使用原型链继承还是 ES6 类继承，都可以实现类似的继承效果，在选择哪种方法时，可以根据个人偏好和项目需求来决定。


---


## getter 和 setter


类中我们可以使用 getter 和 setter 来获取和设置值，getter 和 setter 都需要在严格模式下执行。


getter 和 setter 可以使得我们对属性的操作变的很灵活。


类中添加 getter 和 setter 使用的是 get 和 set 关键字。


以下实例为 sitename 属性创建 getter 和 setter：


## 实例


```javascript
class Runoob {
  constructor(name) {
    this.sitename = name;
  }
  get s_name() {
    return this.sitename;
  }
  set s_name(x) {
    this.sitename = x;
  }
}

let noob = new Runoob("菜鸟教程");

document.getElementById("demo").innerHTML = noob.s_name;
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryjs_classes_getters)


注意：**即使 getter 是一个方法，当你想获取属性值时也不要使用括号。


getter/setter 方法的名称不能与属性的名称相同，在本例中属名为 sitename。


很多开发者在属性名称前使用下划线字符 **_** 将 getter/setter 与实际属性分开：


以下实例使用下划线 **_** 来设置属性，并创建对应的 getter/setter 方法：


## 实例


```javascript
class Runoob {
  constructor(name) {
    this._sitename = name;
  }
  get sitename() {
    return this._sitename;
  }
  set sitename(x) {
    this._sitename = x;
  }
}

let noob = new Runoob("菜鸟教程");

document.getElementById("demo").innerHTML = noob.sitename;
```


**
[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryjs_classes_getters2)


要使用 setter，请使用与设置属性值时相同的语法，虽然 set 是一个方法，但需要不带括号**：


## 实例


```javascript
class Runoob {
  constructor(name) {
    this._sitename = name;
  }
  set sitename(x) {
    this._sitename = x;
  }
  get sitename() {
    return this._sitename;
  }
}

let noob = new Runoob("菜鸟教程");
noob.sitename = "RUNOOB";
document.getElementById("demo").innerHTML = noob.sitename;
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryjs_classes_setter)


## 提升


函数声明和类声明之间的一个重要区别在于, 函数声明会提升，类声明不会。


你首先需要声明你的类，然后再访问它，否则类似以下的代码将抛出 ReferenceError：


## 实例


```javascript
// 这里不能这样使用类，因为还没有声明
// noob = new Runoob("菜鸟教程")
// 报错

class Runoob {
  constructor(name) {
    this.sitename = name;
  }
}

// 这里可以使用类了
let noob = new Runoob("菜鸟教程")
```


使用前没有声明会报错：


![](https://www.runoob.com/wp-content/uploads/2022/01/6A6A2B83-CFA8-4BA0-BB5F-256467CC4702.jpg)


使用前已经声明可以正常执行：


![](https://www.runoob.com/wp-content/uploads/2022/01/83DA43AE-E695-4923-A8CE-0AD92538D6A8.jpg)








	  AI 思考中...





			** [JavaScript 类(class)](https://www.runoob.com/js-class-intro.html)
			[JavaScript 静态方法](https://www.runoob.com/js-class-static.html) **