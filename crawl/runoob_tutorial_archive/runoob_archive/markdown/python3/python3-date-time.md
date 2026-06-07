# Python3 日期和时间

- Source: https://www.runoob.com/python3/python3-date-time.html

Python 程序能用很多方式处理日期和时间，转换日期格式是一个常见的功能。


Python 提供了一个 time 和 calendar 模块可以用于格式化日期和时间。


时间间隔是以秒为单位的浮点小数。


每个时间戳都以自从 1970 年 1 月 1 日午夜（历元）经过了多长时间来表示。


Python 的 time 模块下有很多函数可以转换常见日期格式。如函数 time.time() 用于获取当前时间戳, 如下实例: ## 实例
```python
#!/usr/bin/python3

import time  # 引入time模块

ticks = time.time()
print ("当前时间戳为:", ticks)
```
 以上实例输出结果：


```
当前时间戳为: 1459996086.7115328
```


时间戳单位最适于做日期运算。但是1970年之前的日期就无法以此表示了。太遥远的日期也不行，UNIX和Windows只支持到2038年。


---


## 什么是时间元组？


很多Python函数用一个元组装起来的9组数字处理时间:


| 序号 | 字段 | 值 |
| --- | --- | --- |
| 0 | 4位数年 | 2008 |
| 1 | 月 | 1 到 12 |
| 2 | 日 | 1到31 |
| 3 | 小时 | 0到23 |
| 4 | 分钟 | 0到59 |
| 5 | 秒 | 0到61 (60或61 是闰秒) |
| 6 | 一周的第几日 | 0到6 (0是周一) |
| 7 | 一年的第几日 | 1到366 (儒略历) |
| 8 | 夏令时 | -1, 0, 1, -1是决定是否为夏令时的标识 |


上述也就是 struct_time 元组。这种结构具有如下属性：


| 序号 | 属性 | 值 |
| --- | --- | --- |
| 0 | tm_year | 2008 |
| 1 | tm_mon | 1 到 12 |
| 2 | tm_mday | 1 到 31 |
| 3 | tm_hour | 0 到 23 |
| 4 | tm_min | 0 到 59 |
| 5 | tm_sec | 0 到 61 (60或61 是闰秒) |
| 6 | tm_wday | 0 到 6 (0是周一) |
| 7 | tm_yday | 一年中的第几天，1 到 366 |
| 8 | tm_isdst | 是否为夏令时，值有：1(夏令时)、0(不是夏令时)、-1(未知)，默认 -1 |


---


## 获取当前时间


从返回浮点数的时间戳方式向时间元组转换，只要将浮点数传递给如localtime之类的函数。


```
#!/usr/bin/python3

import time

localtime = time.localtime(time.time())
print ("本地时间为 :", localtime)
```


以上实例输出结果：


```
本地时间为 : time.struct_time(tm_year=2016, tm_mon=4, tm_mday=7, tm_hour=10, tm_min=28, tm_sec=49, tm_wday=3, tm_yday=98, tm_isdst=0)
```


---


## 获取格式化的时间


你可以根据需求选取各种格式，但是最简单的获取可读的时间模式的函数是asctime():


```
#!/usr/bin/python3

import time

localtime = time.asctime( time.localtime(time.time()) )
print ("本地时间为 :", localtime)
```


以上实例输出结果：


```
本地时间为 : Thu Apr  7 10:29:13 2016
```


---


## 格式化日期


我们可以使用 time 模块的 strftime 方法来格式化日期：


```
time.strftime(format[, t])
```


## 实例


```python
#!/usr/bin/python3

import time

# 格式化成2016-03-20 11:45:39形式
print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成Sat Mar 28 22:24:24 2016形式
print (time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print (time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))
```


以上实例输出结果：


```
2016-04-07 10:29:46
Thu Apr 07 10:29:46 2016
1459175064.0
```


python中时间日期格式化符号：


- %y 两位数的年份表示（00-99）
- %Y 四位数的年份表示（000-9999）
- %m 月份（01-12）
- %d 月内中的一天（0-31）
- %H 24小时制小时数（0-23）
- %I 12小时制小时数（01-12）
- %M 分钟数（00=59）
- %S 秒（00-59）
- %a 本地简化星期名称
- %A 本地完整星期名称
- %b 本地简化的月份名称
- %B 本地完整的月份名称
- %c 本地相应的日期表示和时间表示
- %j 年内的一天（001-366）
- %p 本地A.M.或P.M.的等价符
- %U 一年中的星期数（00-53）星期天为星期的开始
- %w 星期（0-6），星期天为星期的开始
- %W 一年中的星期数（00-53）星期一为星期的开始
- %x 本地相应的日期表示
- %X 本地相应的时间表示
- %Z 当前时区的名称
- %% %号本身


---


## 获取某月日历


Calendar 模块有很广泛的方法用来处理年历和月历，例如打印某月的月历：


## 实例


```python
#!/usr/bin/python3

import calendar

cal = calendar.month(2016, 1)
print ("以下输出2016年1月份的日历:")
print (cal)
```


以上实例输出结果：


```
以下输出2016年1月份的日历:
    January 2016
Mo Tu We Th Fr Sa Su
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30 31
```


---


## Time 模块


Time 模块包含了以下内置函数，既有时间处理的，也有转换时间格式的：


| 序号 | 函数及描述 | 实例 |
| --- | --- | --- |
| 1 | time.altzone返回格林威治西部的夏令时地区的偏移秒数。如果该地区在格林威治东部会返回负值（如西欧，包括英国）。对夏令时启用地区才能使用。 | 以下实例展示了 altzone()函数的使用方法：
```
>>> import time
>>> print ("time.altzone %d " % time.altzone)
time.altzone -28800
```
 |
| 2 | time.asctime([tupletime])接受时间元组并返回一个可读的形式为"Tue Dec 11 18:07:14 2008"（2008年12月11日 周二18时07分14秒）的24个字符的字符串。 | 以下实例展示了 asctime()函数的使用方法：
```
>>> import time
>>> t = time.localtime()
>>> print ("time.asctime(t): %s " % time.asctime(t))
time.asctime(t): Thu Apr  7 10:36:20 2016
```
 |
| 3 | time.clock()用以浮点数计算的秒数返回当前的CPU时间。用来衡量不同程序的耗时，比time.time()更有用。 | 实例 由于该方法依赖操作系统，在 Python 3.3 以后不被推荐，而在 3.8 版本中被移除，需使用下列两个函数替代。
```
time.perf_counter()  # 返回系统运行时间
time.process_time()  # 返回进程运行时间
```
 |
| 4 | time.ctime([secs])作用相当于asctime(localtime(secs))，未给参数相当于asctime() | 以下实例展示了 ctime()函数的使用方法：
```
>>> import time
>>> print ("time.ctime() : %s" % time.ctime())
time.ctime() : Thu Apr  7 10:51:58 2016
```
 |
| 5 | time.gmtime([secs])接收时间戳（1970纪元后经过的浮点秒数）并返回格林威治天文时间下的时间元组t。注：t.tm_isdst始终为0 | 以下实例展示了 gmtime()函数的使用方法：
```
>>> import time
>>> print ("gmtime :", time.gmtime(1455508609.34375))
gmtime : time.struct_time(tm_year=2016, tm_mon=2, tm_mday=15, tm_hour=3, tm_min=56, tm_sec=49, tm_wday=0, tm_yday=46, tm_isdst=0)
```
 |
| 6 | time.localtime([secs]接收时间戳（1970纪元后经过的浮点秒数）并返回当地时间下的时间元组t（t.tm_isdst可取0或1，取决于当地当时是不是夏令时）。 | 以下实例展示了 localtime()函数的使用方法：
```
>>> import time
>>> print ("localtime(): ", time.localtime(1455508609.34375))
localtime():  time.struct_time(tm_year=2016, tm_mon=2, tm_mday=15, tm_hour=11, tm_min=56, tm_sec=49, tm_wday=0, tm_yday=46, tm_isdst=0)
```
 |
| 7 | time.mktime(tupletime)接受时间元组并返回时间戳（1970纪元后经过的浮点秒数）。 | 实例 |
| 8 | time.sleep(secs)推迟调用线程的运行，secs指秒数。 | 以下实例展示了 sleep()函数的使用方法：
```
#!/usr/bin/python3
import time

print ("Start : %s" % time.ctime())
time.sleep( 5 )
print ("End : %s" % time.ctime())
```
 |
| 9 | time.strftime(fmt[,tupletime])接收以时间元组，并返回以可读字符串表示的当地时间，格式由fmt决定。 | 以下实例展示了 strftime()函数的使用方法：
```
>>> import time
>>> print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
2016-04-07 11:18:05
```
 |
| 10 | time.strptime(str,fmt='%a %b %d %H:%M:%S %Y')根据fmt的格式把一个时间字符串解析为时间元组。 | 以下实例展示了 strptime()函数的使用方法：
```
>>> import time
>>> struct_time = time.strptime("30 Nov 00", "%d %b %y")
>>> print ("返回元组: ", struct_time)
返回元组:  time.struct_time(tm_year=2000, tm_mon=11, tm_mday=30, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=335, tm_isdst=-1)
```
 |
| 11 | time.time( )返回当前时间的时间戳（1970纪元后经过的浮点秒数）。 | 以下实例展示了 time()函数的使用方法：
```
>>> import time
>>> print(time.time())
1459999336.1963577
```
 |
| 12 | time.tzset()根据环境变量TZ重新初始化时间相关设置。 | 实例 |
| 13 | time.perf_counter() 返回计时器的精准时间（系统的运行时间），包含整个系统的睡眠时间。由于返回值的基准点是未定义的，所以，只有连续调用的结果之间的差才是有效的。 | 实例 |
| 14 | time.process_time() 返回当前进程执行 CPU 的时间总和，不包含睡眠时间。由于返回值的基准点是未定义的，所以，只有连续调用的结果之间的差才是有效的。 |  |


Time模块包含了以下2个非常重要的属性：


| 序号 | 属性及描述 |
| --- | --- |
| 1 | time.timezone属性time.timezone是当地时区（未启动夏令时）距离格林威治的偏移秒数（>0，美洲;







	  AI 思考中...





			** [Python3 time tzset()方法](https://www.runoob.com/python3-att-time-tzset-html.html)
			[Python3 time clock()方法](https://www.runoob.com/python3-att-time-clock.html) **