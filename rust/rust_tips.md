  unwrap()%用来解包，直接从str到数字%和expected()都会发生错误导致系统崩溃，但是前者是系统默认错误，看不懂，后者有遗言。
   下面两句完全等价
   ```rust
   let guess:u32= match "30".trim().parse(){
   Ok(num) => num;
   Err(_) => panic("程序崩溃！")
   }
   ```
   ```rust
   let guess:u32= "30".parse().unwrap();
   
   //tips, 上面的parse()是把字符串转化为了数字，但是相当于一个盒子，需要unwrap解包
   //或者使用Result的枚举值Ok来判定才能使用
   ```


rust中表达式一定返回值，语句使用 *；* 结尾，产生*()* ，这是一个占用内存为0的真实存在的值：**unit value(单位元)**
 