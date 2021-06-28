package main

import "fmt"

func Sum(src []int, ch chan int) {
	sumtmp := 0
	for _, part := range src {
		sumtmp += part
	}
	ch <- sumtmp
}

func main() {
	srctmp := []int{1, 2, 3, 4, 5, 6, 7, 0}
	ch := make(chan int, 2)

	go Sum(srctmp[:3], ch)
	go Sum(srctmp[3:], ch)

	x, y := <-ch, <-ch

	fmt.Println(x, y, x+y)
	close(ch)
}
