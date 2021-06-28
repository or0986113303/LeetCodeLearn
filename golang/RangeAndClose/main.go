package main

import "fmt"

func fabonaci(len int, ch chan int) {
	tmpx, tmpy := 0, 1

	for index := 0; index < len; index++ {
		ch <- tmpx
		tmpx, tmpy = tmpy, tmpx+tmpy
	}

	close(ch)
}

func main() {
	chtmp := make(chan int, 10)
	fabonaci(cap(chtmp), chtmp)

	for part := range chtmp {
		fmt.Printf("nm : %d\n", part)
	}
}
