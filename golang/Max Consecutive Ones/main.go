package main

import (
	"fmt"
)

func hello(src string) (result string) {
	fmt.Println(src)
	result = src
	return result
}

func max_consecutive_ones(src []int) (result int) {
	if src == nil {
		return result
	}
	maxcount := 0
	count := 0
	for _, parts := range src {
		if parts != 0 {
			count++
			if count >= maxcount {
				maxcount = count
			}
		} else {
			count = 0
		}
	}
	result = maxcount
	return result
}

func main() {
	hello("hello")
	var nums []int
	result := max_consecutive_ones(nums[:])
	fmt.Println(result)
}
