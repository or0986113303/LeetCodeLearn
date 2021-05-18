package main

import (
	"fmt"
)

func remove_element(src []int, target int) int {
	for index := 0; index < len(src); {
		if src[index] == target {
			src = append(src[:index], src[index+1:]...)
			index--
		}
		index++
	}
	return len(src)
}

func main() {
	fmt.Println("hello")
	nums := []int{3, 2, 2, 3}
	val := 3
	result := remove_element(nums, val)
	fmt.Println(result)
}
