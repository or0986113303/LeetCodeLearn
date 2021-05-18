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

func binarySearch(src []int, target int) bool {

	low := 0
	high := len(src) - 1

	for low <= high {
		median := (low + high) / 2

		if src[median] < target {
			low = median + 1
		} else {
			high = median - 1
		}
	}

	if low == len(src) || src[low] != target {
		return false
	}

	return true
}

func check_if_n_and_its_double_exist(src []int) (result bool) {
	sortedsrc := mergesort(src)
	fmt.Println(sortedsrc)
	for index := 0; index < len(sortedsrc); {
		part := sortedsrc[index]
		if sortedsrc[index] != 0 {
			if binarySearch(sortedsrc, part*2) {
				result = true
				return result
			}
		} else {
			tmp := append(sortedsrc[:index], sortedsrc[index+1:]...)
			index--
			if binarySearch(tmp, part) {
				result = true
				return result
			}
		}
		index++
	}
	result = false
	return result
}

func main() {
	fmt.Println("hello")
}
