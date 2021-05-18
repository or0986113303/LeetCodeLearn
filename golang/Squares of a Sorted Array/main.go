package main

import (
	"fmt"
	"math"
)

func mergesort(src []int) (result []int) {

	if len(src) <= 1 {
		result = src
		return result
	}

	middle := len(src) / 2

	leftpart := src[:middle]
	rightpart := src[middle:]

	return merge(mergesort(leftpart), mergesort(rightpart))
}

func merge(left, right []int) (result []int) {

	result = make([]int, len(left)+len(right))

	normalindex := 0

	for len(left) > 0 && len(right) > 0 {
		if left[0] < right[0] {
			result[normalindex] = left[0]
			left = left[1:]
		} else {
			result[normalindex] = right[0]
			right = right[1:]
		}
		normalindex++
	}

	for repearindex := 0; repearindex < len(left); repearindex++ {
		result[normalindex] = left[repearindex]
		normalindex++
	}

	for repearindex := 0; repearindex < len(right); repearindex++ {
		result[normalindex] = right[repearindex]
		normalindex++
	}

	return result
}

func squares_of_a_sorted_array(src []int) (result []int) {
	for index, parts := range src {
		src[index] = int(math.Pow(float64(parts), 2))
	}
	result = mergesort(src)
	return result
}

func main() {
	fmt.Println("hello")
	src := []int{-7, -3, 2, 3, 11}
	result := squares_of_a_sorted_array(src)
	fmt.Println(result)
}
