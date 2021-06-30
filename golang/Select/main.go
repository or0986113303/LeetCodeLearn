package main

import (
	"fmt"
	"time"
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
		time.Sleep(10 * time.Millisecond)
	}
}

func timertest(quit chan int) {
	TimerOne := time.Tick(5 * time.Millisecond)
	TimeTwo := time.After(50 * time.Millisecond)
	for {
		select {
		case <-TimerOne:
			fmt.Println("Took 5 ms")
		case <-TimeTwo:
			fmt.Println("After 50 ms")
		case <-quit:
			return
		default:
			fmt.Println("main loop")
		}
		time.Sleep(1 * time.Millisecond)
	}
}

func main() {
	ch := make(chan int)
	quit := make(chan int, 2)

	go flow(10, ch, quit)
	// go timertest(quit)
	fabonaci(ch, quit)

	// time.Sleep(1000 * time.Millisecond)
	// quit <- 0
	defer close(ch)
	defer close(quit)

}
