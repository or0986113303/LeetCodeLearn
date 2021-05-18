package main

import (
	"fmt"
)

func merge(left []int, leftlength int, right []int, rightlength int) (result []int) {
	result = make([]int, leftlength+rightlength)
	left = left[:leftlength]
	right = right[:rightlength]
	index := 0

	for len(left) > 0 && len(right) > 0 {
		if left[0] < right[0] {
			result[index] = left[0]
			left = left[1:]
		} else {
			result[index] = right[0]
			right = right[1:]
		}
		index++
	}

	for subindex := 0; subindex < len(left); subindex++ {
		result[index] = left[subindex]
		index++
	}

	for subindex := 0; subindex < len(right); subindex++ {
		result[index] = right[subindex]
		index++
	}
	return result
}

func merge_sorted_array(src []int) (result []int) {
	return result
}

func main() {
	fmt.Println("hello")
	nums1 := []int{1, 2, 3, 0, 0, 0}
	//m := 3
	nums2 := []int{2, 5, 6}
	//n := 3
	result := merge(nums1, 3, nums2, 3)
	fmt.Println(result)
}
