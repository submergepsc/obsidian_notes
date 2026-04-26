准备环境:
```bash
alias testcmd ='echo alias'
testcmd(){
echo function;}
```
上面的内容根本无法测试,因为**alias是在读取代码的时候就替换的!**

bash运行:
```bash
	echo -e '#!/bin/bash\necho binary' > ~/textcmd
	chmod +x ~/.testcmd
	export PATH="$HOME:$PATH"
```
1. 目前执行,输出`alias`
alias> function > builtin>path
2. 去掉alias,输出`function`
```bash
unalias testcmd 
testcmd 
```
3. 去掉function,输出`binary`
```bash
unset -f testcmd 
testcmd
```
	