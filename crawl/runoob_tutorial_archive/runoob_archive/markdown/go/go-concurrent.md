# Go 并发

- Source: https://www.runoob.com/go/go-concurrent.html

并发是指程序同时执行多个任务的能力。


Go 语言支持并发，通过 goroutines 和 channels 提供了一种简洁且高效的方式来实现并发。


**Goroutines：**

- Go 中的并发执行单位，类似于轻量级的线程。
- Goroutine 的调度由 Go 运行时管理，用户无需手动分配线程。
- 使用 `go` 关键字启动 Goroutine。
- Goroutine 是非阻塞的，可以高效地运行成千上万个 Goroutine。


**Channel：**

- Go 中用于在 Goroutine 之间通信的机制。
- 支持同步和数据共享，避免了显式的锁机制。
- 使用 `chan` 关键字创建，通过 `







	  AI 思考中...





			** [Go 语言开发工具](https://www.runoob.com/go-ide.html)
			[Go fmt.Sprintf 格式化字符串](https://www.runoob.com/go-fmt-sprintf.html) **