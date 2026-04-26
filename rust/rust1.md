[the tool link of rust and java](the%20tool%20link%20of%20rust%20and%20java.md)


### rust工具链
1. 在本地使用
- rustup: 所有工具下载
```
常用命令
rustup update
rustup self uninstall

rustc --version
rust doc //本地文件浏览
```

2. 运行rsut程序方法
	1. ```
	   是一个cargo项目
	   通过`cargo new`创建，文件夹里面有`Cargo.toml`和`src/main.rs`，
	   项目目录下运行`cargo run`即可。
	   ```
	2. ```
	   独立的rsut文件，
	   rustc test.rs # 编译生成test.exe
	   ./test.exe
	   ```


###### 内存安全 
>[!以下三种行为会发生数据竞争]
>两个或多个指针同时访问同一数据；
>至少有一个指针用于写入数据；
>没有使用任何机制来同步对数据的访问。


	#### 在线练习
1. [关于 practice.rs - Rust By Practice( Rust 练习实践 )](https://practice-rust-zh.beatai.org/)
>[!本地运行]+
>我们使用 [mdbook](https://rust-lang.github.io/mdBook/) 构建在线练习题，你也可以下载到本地运行：
>`$ git clone https://github.com/sunface/rust-by-practice $ cargo install mdbook $ cd rust-by-practice && mdbook serve zh-CN/`
>在本地win 10或者linux服务器上运行时，应当使用 -n 参数指定mdbook服务所监听的IP地址（-p 参数指定服务监听的端口，不指定则为默认的3000），以win 10本地运行为例：
>`$ mdbook serve -p 8888 -n 127.0.0.1 zh-CN/`
>可以换成` mdbook serve zh-CN/`
>然后可以在vscode中，`ctrl+shift+p`输入simple browser:show,`http://127.0.0.1:your_post`来查看





	


# rust基本语法
1. [rust数据类型](rust数据类型.md)
2. [rust_tips](rust_tips.md)
3. 