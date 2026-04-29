# 文件操作 - OI Wiki

- Source: https://oi-wiki.org/lang/file-op/

# 文件操作

## 文件的概念

文件是根据特定的目的而收集在一起的有关数据的集合．C/C++ 把每一个文件都看成是一个有序的字节流，每个文件都是以 **文件结束标志** （EOF）结束，如果要操作某个文件，程序应该首先打开该文件，每当一个文件被打开后（请记得关闭打开的文件），该文件就和一个流关联起来，这里的流实际上是一个字节序列．

C/C++ 将文件分为文本文件和二进制文件．文本文件就是简单的文本文件（重点），另外二进制文件就是特殊格式的文件或者可执行代码文件等．

## 文件的操作步骤

1、打开文件，将文件指针指向文件，决定打开文件类型；  
2、对文件进行读、写操作（比赛中主要用到的操作，其他一些操作暂时不写）；  
3、在使用完文件后，关闭文件．

## `freopen` 函数

### 函数简介

函数用于将指定输入输出流以指定方式重定向到文件，包含于头文件 `stdio.h (cstdio)` 中，该函数可以在不改变代码原貌的情况下改变输入输出环境，但使用时应当保证流是可靠的．

函数主要有三种方式：读、写和附加．

### 命令格式

```text 1 ``` |  ```text FILE * freopen ( const char * filename , const char * mode , FILE * stream ); ```   
---|---  
  
### 参数说明

  * `filename`: 要打开的文件名
  * `mode`: 文件打开的模式，表示文件访问的权限
  * `stream`: 文件指针，通常使用标准文件流 (`stdin/stdout`) 或标准错误输出流 (`stderr`)
  * 返回值：文件指针，指向被打开文件

### 文件打开格式（选读）

  * `r`：以只读方式打开文件，文件必须存在，只允许读入数据 **（常用）**
  * `r+`：以读/写方式打开文件，文件必须存在，允许读/写数据
  * `rb`：以只读方式打开二进制文件，文件必须存在，只允许读入数据
  * `rb+`：以读/写方式打开二进制文件，文件必须存在，允许读/写数据
  * `rt+`：以读/写方式打开文本文件，允许读/写数据
  * `w`：以只写方式打开文件，文件不存在会新建文件，否则清空内容，只允许写入数据 **（常用）**
  * `w+`：以读/写方式打开文件，文件不存在将新建文件，否则清空内容，允许读/写数据
  * `wb`：以只写方式打开二进制文件，文件不存在将会新建文件，否则清空内容，只允许写入数据
  * `wb+`：以读/写方式打开二进制文件，文件不存在将新建文件，否则清空内容，允许读/写数据
  * `a`：以只写方式打开文件，文件不存在将新建文件，写入数据将被附加在文件末尾（保留 EOF 符）
  * `a+`：以读/写方式打开文件，文件不存在将新建文件，写入数据将被附加在文件末尾（不保留 EOF 符）
  * `at+`：以读/写方式打开文本文件，写入数据将被附加在文件末尾
  * `ab+`：以读/写方式打开二进制文件，写入数据将被附加在文件末尾

### 使用方法

读入文件内容：

```text 1 2 ``` |  ```text freopen ( "data.in" , "r" , stdin ); // data.in 就是读取的文件名，要和可执行文件放在同一目录下 ```   
---|---  
  
输出到文件：

```text 1 2 ``` |  ```text freopen ( "data.out" , "w" , stdout ); // data.out 就是输出文件的文件名，和可执行文件在同一目录下 ```   
---|---  
  
关闭标准输入/输出流

```text 1 2 ``` |  ```text fclose ( stdin ); fclose ( stdout ); ```   
---|---  
  
注

`printf/scanf/cin/cout` 等函数默认使用 `stdin/stdout`，将 `stdin/stdout` 重定向后，这些函数将输入/输出到被定向的文件

### 模板

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 ``` |  ```text #include <cstdio> #include <iostream> int main ( void ) { freopen ( "data.in" , "r" , stdin ); freopen ( "data.out" , "w" , stdout ); /* 中间的代码不需要改变，直接使用 cin 和 cout 即可 */ fclose ( stdin ); fclose ( stdout ); return 0 ; } ```   
---|---  
  
## `fopen` 函数（选读）

函数大致与 `freopen` 相同，函数将打开指定文件并返回打开文件的指针

### 函数原型

```text 1 ``` |  ```text FILE * fopen ( const char * path , const char * mode ) ```   
---|---  
  
各项参数含义同 `freopen`

### 可用读写函数（基本）

  * `fread/fwrite`
  * `fgetc/fputc`
  * `fscanf/fprintf`
  * `fgets/fputs`

### 使用方式

```text 1 2 3 4 5 6 7 8 ``` |  ```text FILE * in , * out ; // 定义文件指针 in = fopen ( "data.in" , "r" ); out = fopen ( "data.out" , "w" ); /* do what you want to do */ fclose ( in ); fclose ( out ); ```   
---|---  
  
## C++ 的 `ifstream/ofstream` 文件输入输出流

### 使用方法

读入文件内容：

```text 1 2 ``` |  ```text ifstream fin ( "data.in" ); // data.in 就是读取文件的相对位置或绝对位置 ```   
---|---  
  
输出到文件：

```text 1 2 ``` |  ```text ofstream fout ( "data.out" ); // data.out 就是输出文件的相对位置或绝对位置 ```   
---|---  
  
关闭标准输入/输出流

```text 1 2 ``` |  ```text fin . close (); fout . close (); ```   
---|---  
  
### 模板

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``` |  ```text #include <fstream> using namespace std ; // 两个类型都在 std 命名空间里 ifstream fin ( "data.in" ); ofstream fout ( "data.out" ); int main ( void ) { /* 中间的代码改变 cin 为 fin ，cout 为 fout 即可 */ fin . close (); fout . close (); return 0 ; } ```   
---|---  
  
## 参考资料

  1. 信息学奥赛一本通

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/lang/file-op.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/lang/file-op.md "edit.link.title")  
>  __本页面贡献者：[Ir1d](https://github.com/Ir1d), [cqnuljs](https://github.com/cqnuljs), [akakw1](https://github.com/akakw1), [StudyingFather](https://github.com/StudyingFather), [Chrogeek](https://github.com/Chrogeek), [henrytbtrue](https://github.com/henrytbtrue), [Planet6174](https://github.com/Planet6174), [Tiphereth-A](https://github.com/Tiphereth-A), [Bardisk](https://github.com/Bardisk), [c-forrest](https://github.com/c-forrest), [Charlie-zzy](https://github.com/Charlie-zzy), [Enter-tainer](https://github.com/Enter-tainer), [GekkaSaori](https://github.com/GekkaSaori), [ksyx](https://github.com/ksyx), [MingqiHuang](mailto:hmq011212@163.com), [MingqiHuang](https://github.com/MingqiHuang), [TianKong-y](https://github.com/TianKong-y), [VaneHsiung](https://github.com/VaneHsiung), [Xeonacid](https://github.com/Xeonacid)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
