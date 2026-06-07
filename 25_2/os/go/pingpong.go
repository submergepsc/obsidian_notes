package main
import (
    "fmt"
    "time"
)
type Ball struct {
    hits int
}
func player(name string, table chan *Ball) {
    for {
       ball := <-table
       ball.hits++
       fmt.Println(name, ball.hits)
       time.Sleep(1 * time.Second)
       table <- ball
    }
}
func main() {
    table := make(chan *Ball)
    go player("ping", table)
    go player("pong", table)
    table <- new(Ball) // 游戏开始，发球
    time.Sleep(10 * time.Second)
    <-table
    close(table) // 游戏结束
}