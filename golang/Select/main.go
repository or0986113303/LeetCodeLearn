package main

import (
	"fmt"
)

func flow(len int, ch chan int, quit chan int) {

	for index := 0; index < len; index++ {
		fmt.Printf("ch : %d\n", <-ch)
	}
	quit <- 0
}

func fabonaci(ch, quit chan int) {
	x, y := 0, 1

	for {
		select {
		case ch <- x:
			x, y = y, x+y
		case <-quit:
			fmt.Println("Quit")
			return
		}
	}
}

func main() {
	ch := make(chan int)
	quit := make(chan int)

	go flow(10, ch, quit)
	fabonaci(ch, quit)

	close(ch)
	close(quit)
}
