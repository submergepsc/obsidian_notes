- [x] [model](model.md)
0b,0x,0o,没有080前缀0,
complex使用j
raw,printf(r"\n")输出\n
包含一个元素的元组a=(23,),b=(39) 表示一个int,()表示空元组,
{}是空字典,set()创建空集合
Python 3.7 起字典保持插入顺序。
print2中可以用print "hello",print不是函数,是语句,python3必须()
```python
my_dirt={}
my_dirt['one']="111"
my_dirt['two']=2222
print(type(my_dirt['two']))
tinydict={'name':123,'abc':90,'fjd':90}
print(tinydict.keys())
print(tinydict.values())
```
dict:
```shell
>>> dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
{'Runoob': 1, 'Google': 2, 'Taobao': 3}
>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}
>>> dict(Runoob=1, Google=2, Taobao=3)
{'Runoob': 1, 'Google': 2, 'Taobao': 3}
```
clear(),keys(),values()
bytes:
x = bytes("hello", encoding="utf-8")
```python
x=b"hello"
print(x[0:2])
print(x[0])
y=x[2:]
print(y )
```
``
```python
#海象运算符"（Walrus Operator
# python3.8
if (n:=10)>5:
	print("ok")
```
```run-python
a=0b00011111
b=0b11101000
print(bin(a&b))
print(bin(a|b))
print(bin(a^b))
print(bin(~a))
c=10
print(bin(c))
print(~c)
print(bin(~c))
```
del :删除某些变量
# 注释
docstring文档字符,通过__doc__变量或者help()查看
或者使用inspect模块获取文档
```python
import inspect
def add(a, b):
    """返回两数之和"""
    return a + b
# 使用 inspect.getdoc() 获取文档
print(inspect.getdoc(add))  # 输出: 返回两数之和
```
# nubmer
int(),float(),complex(10.2),complex(19,2)
元组中只包含一个元素时，需要在元素后面添加逗号 , ，否则括号会被当作运算符使用：
# dict
key可以用number,tuple,str,但是不能是list
循环只有一句可以写道同一行
break退出不会执行esle(while和for)
# with
```python
class ContextManager:
    def __enter__(self):
        print("调用 __enter__()")
        print("返回资源对象")
        return "resource"
    def __exit__(self, exc_type, exc_value, traceback):
        print("调用 __exit__()")
        print("清理资源")
        if exc_type:
            print("发生异常:", exc_type, exc_value)
        return False
print("开始 with 块")
with ContextManager() as resource:
    print("执行代码块")
    print("resource =", resource)
print("继续执行后续代码")
```
# function参数
```python
#!/usr/bin/python3
# 可写函数说明
def printinfo( arg1, *vartuple ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   print (vartuple)
# 调用printinfo 函数
printinfo( 70, 60, 50 )
```
\*会收集多余位置的参数,生成一个元组
\*\*会手机多余位置的参数,生成一个字典
```python
#!/usr/bin/python3
# 可写函数说明
def printinfo( arg1, **vardict ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   print (vardict)
# 调用printinfo 函数
printinfo(1, a=2,b=3)
```
如果单独出现星号 *，则星号\*后的参数必须用关键字传入：
# 输入输出
```python
 #method1
for i in range(1,11):
	print(repr(i).rjust(2),repr(i*i).rjust(3),end=' ')
	print(repr(i*i*i).rjust(4)) 
for x in  range(1,11):
	print("{0:2d} {1:3d} {2:4d}".format(x,x*x,x**3))
```
# lambda
lambda
```python
#!/usr/bin/python3
sum=lambda a, b: a+b
print(sum(10,100))
```
$\lambda$
## 强制位置参数
Python3.8 新增了一个函数形参语法 / 用来指明函数形参必须使用指定位置参数，不能使用关键字参数的形式。
在以下的例子中，形参 a 和 b 必须使用指定位置参数，c 或 d 可以是位置形参或关键字形参，而 e 和 f 要求为关键字形参:
```python
def f(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)
f(10, 20, 30, d=40, e=50, f=60)
	```
```python
arr=list(range(10))
print(list(filter(lambda x:x%2==0,arr)))
```
### reduce
```python
from functools import reduce
numbers = [1, 2, 3, 4, 5]
# 使用 reduce() 和 lambda 函数计算乘积
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 输出：120
```
# 装饰器
```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("执行前")
        func(*args, **kwargs)
        print("执行后")
    return wrapper
@my_decorator
def greet(name):
    print(f"Hello, {name}!")
greet("Alice")
```
@my_decorator等价于执行say_hello=my_decoreator(say_hello)
带参数的装饰器
```python
def repeat(num_times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return decorator
@repeat(3)
def say_hello():
    print("Hello!")
say_hello()
```
```python
def repeat(times):
	def decorator(func):
		def wrapper(*args,**kwargs):
			for _ in range(times): 
				func(*args,**kwargs)
		return wrapper
	return decorator
@repeat(3)
def hello():
	print("hello")
hello()
```
# 类
类的self
```python
class MyClass:
	def __init__(self,value):
		self.value=value
	def display(self):
		print(self.value)
obj=MyClass(42)
obj.display ()
```
类的方法+继承+多继承
```python
class people:
	name=''
	age=0
	weight=0
	def __init__(self,n,a,w):
		self.name=n
		self.age=a
		self.weight=w
	def speak(self):
		print("%s says my age is :%d."%(self.name,self.age)) 
class student(people):
	grade=0
	def __init__(self,n,a,w,g):
		people.__init__(self,n,a,w)
		self.grade=g
	def speak(self):
		print("%s says my age is:%d,got %d grade."%(self.name,self.age,self.grade))
s=student("mike",10,100,90)
s.speak()
class speaker:
	topic=''
	name=''
	def __init__(self,n,t):
		self.name=n
		self.topic=t
	def speak(self):
		print("I am %s, a speaker ,the topic is %s"%(self.name,self.topic))
# 多继承,相同的方法,逐个搜索使用最先匹配的
class sample(speaker,student):
	def __init__(self,n,a,w,g,t):
		student.__init__(self,n,a,w,g)
		speaker.__init__(self,n,t)
sa=sample("mike",10,200,90,"hello")
sa.speak()
```
方法重写:
```python
#!/usr/bin/python3
class Parent:        # 定义父类
   def myMethod(self):
      print ('调用父类方法')
class Child(Parent): # 定义子类
   def myMethod(self):
      print ('调用子类方法')
c = Child()          # 子类实例
c.myMethod()         # 子类调用重写方法
super(Child,c).myMethod() #用子类对象调用父类已被覆盖的方法super是内置函数
```
#### 类的私有属性(数据和方法)都是__开头.
| 方法            | 单词含义解释                    | 功能简述                                                  |
| ------------- | ------------------------- | ----------------------------------------------------- |
| `__init__`    | **initialize**（初始化）       | 构造函数，创建对象时调用                                          |
| `__del__`     | **delete**（删除）            | 析构函数，释放对象时调用                                          |
| `__repr__`    | **representation**（表示/呈现） | 打印或返回对象的官方字符串表示                                       |
| `__setitem__` | **set item**（设置项）         | 按索引给容器元素赋值                                            |
| `__getitem__` | **get item**（获取项）         | 按索引获取容器元素                                             |
| `__len__`     | **length**（长度）            | 返回对象的长度                                               |
| `__cmp__`     | **compare**（比较）           | 对象之间的比较运算（Python 2 用法，Python 3 用 `__lt__`、`__eq__` 等） |
| `__call__`    | **call**（调用）              | 让对象像函数一样被调用                                           |
| `__add__`     | **add**（加）                | 加法运算符重载（`+`）                                          |
| `__sub__`     | **subtract**（减）           | 减法运算符重载（`-`）                                          |
| `__mul__`     | **multiply**（乘）           | 乘法运算符重载（`*`）                                          |
| `__truediv__` | **true divide**（真除法）      | 除法运算符重载（`/`，浮点除法）                                     |
| `__mod__`     | **modulus**（取模）           | 求余运算符重载（`%`）                                          |
| `__pow__`     | **power**（幂/乘方）           | 乘方运算符重载（`**`）                                         |
| `__str__`     |                           |                                                       |
|               |                           |                                                       |

#### 运算符重载
```python
class vector:
	def __init__(self,a,b):
		self.a=a
		self.b=b
	def __add__(self,other):
		return vector(self.a+other.a,self.b+other.b)
	def __sub__(self,other):
		return vector(self.a-other.a,self.b-other.b)
	def __mul__(self,other):
		return vector(self.a*other.a-self.b*other.b,self.a*other.b+self.b*other.a)
	def __str__(self):
		return ("value is %d+%dj"%(self.a,self.b))
v1=vector(1,2)
v2=vector(3,4) 
for i in [v1+v2,v1-v2,v1*v2]:
	print(i)
```
# 异常和错误
try,except,else,final
```python
try:
    runoob()
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print('这句话，无论异常是否发生都会执行。')
```
raise:
```python
try:  
    raise NameError('HiThere')  # 模拟一个异常。  
except NameError:  
    print('An exception flew by!')  
    raise
    raise
```