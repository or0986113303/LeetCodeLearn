package main

import (
	"fmt"
)

func duplicate_zeros(src []int) {
	for index := 0; index < len(src); index++ {
		if src[index] == 0 && index+1 < len(src) {
			src = append(src[:index+1], src[index:len(src)-1]...)
			index++
		}
	}
	return
}

func main() {
	fmt.Println("hello")
	src := []int{1, 0, 2, 3, 0, 4, 5, 0}
	duplicate_zeros(src)
}
