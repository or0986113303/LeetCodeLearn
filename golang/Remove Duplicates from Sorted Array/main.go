package main

import (
	"fmt"
)

func remove_duplicates_from_sorted_array(src []int) (length int, result []int) {

	target := -9999999999999
	for index := 0; index < len(src); {
		if target == -9999999999999 {
			target = src[index]
		} else {
			if target == src[index] {
				src = append(src[:index], src[index+1:]...)
				index--
			}
			target = src[index]
		}
		index++
	}
	result = src
	length = len(result)
	return length, result
}

func main() {
	fmt.Println("hello")
}
