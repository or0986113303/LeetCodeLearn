package main

import (
	"concurrentqueue/library"
	"fmt"
	"sync"
)

func main() {
	que := library.NewQueue(1)
	ch := make(chan int, 1)
	var wg sync.WaitGroup
	wg.Add(2)
	go func() {
		for index := 0; index < 10; index++ {
			que.Push(index)
		}
		wg.Done()
		ch <- 1
	}()

	go func() {
		<-ch
		for index := 0; index < len(que.Items); {
			fmt.Println(que.Pop())
		}
		wg.Done()
		defer close(ch)
	}()
	wg.Wait()
	fmt.Println("Finish")
}
