package main
import (
    "fmt"
    "time"
)
func longTask(signal chan int) {
    // 不带参数的 for
    // 相当于 while 循环
    for {
       fmt.Println("longTask is running")
       // 接收 signal 通道传值
       v := <-signal
       // 如果接收值为 1，停止循环
       if v == 1 {
          break
       }
       time.Sleep(1 * time.Second)
    }
    fmt.Println("longTask is finihsed")
}
func main() {
    // 声明通道
    sig := make(chan int)
    // 异步调用 longTask
    go longTask(sig)
    // 等待 1 秒钟
    time.Sleep(10 * time.Second)
    // 向通道 sig 传值
    sig <- 1
    // 然后 longTask 会接收 sig 传值，终止循环
    time.Sleep(1 * time.Second)
}