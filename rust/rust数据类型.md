# vector
- let arr=[1,2,3]
- let arr=[2;32]
	- **tips**: [value; number of the value]
- let v2=**vec!**[1,2,3]
- let x=v2[2]
	- **tips**: ```
	```
	向量可以像数组一样使用门来访问元素。
在 Rust中不能用i32/i64等类型的值作为下标访问元素。
必须使用 usize 类型的值，因为 usize 保证和指针是一样长度的。其他类型要显式转换成usize:
let i: i8 = 2;
let y = v2[i as usize];
	```

>[!example:]-
>let i:i8=2;
let ve=vec![1,2,3];
let y=ve[i as usize]
# string 
![ 900x400](assets/Pasted%20image%2020260320210042.png)

