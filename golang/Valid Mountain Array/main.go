package main

import (
	"fmt"
)

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

	for subindex := 0; subindex < len(left); subindex++ {
		result[normalindex] = left[subindex]
		normalindex++
	}

	for subindex := 0; subindex < len(right); subindex++ {
		result[normalindex] = right[subindex]
		normalindex++
	}

	return result
}

func mergesort(src []int) (result []int) {
	if len(src) <= 1 {
		result = src
		return result
	}

	middle := len(src) / 2

	left := src[:middle]
	right := src[middle:]

	return merge(mergesort(left), mergesort(right))
}

func findmax(src []int) (result int) {
	tmp := mergesort(src)
	return tmp[len(tmp)-1]
}

func Valid_mountain_array(src []int) (result bool) {
	if len(src) < 3 {
		result = false
		return result
	}
	max := findmax(src)
	fmt.Println(max)

	alreadymax := false

	for index := 0; index < len(src)-1; index++ {
		if src[index] == max {
			alreadymax = true
		}
		if alreadymax {
			if src[index] > src[index+1] {
				if max != src[0] {
					result = true
				} else {
					result = false
					break
				}
			} else {
				result = false
				break
			}
		} else {
			if src[index] < src[index+1] {
				if max != src[len(src)-1] {
					result = true
				} else {
					result = false
					break
				}
			} else {
				result = false
				break
			}
		}
	}
	return result
}

func main() {
	fmt.Println("hello")
}
