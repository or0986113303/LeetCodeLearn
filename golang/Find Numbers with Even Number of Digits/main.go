package main

import (
	"fmt"
	"strconv"
)

func find_numbers_with_even_number_of_digits(src []int) (result int) {
	if src == nil {
		result = 0
		return result
	}
	count := 0
	for _, parts := range src {
		tmp := strconv.Itoa(parts)
		if len(tmp)%2 == 0 {
			count++
		}
	}
	result = count
	return result
}

func main() {
	nums := []int{12, 345, 2, 6, 7896}
	result := find_numbers_with_even_number_of_digits(nums)
	fmt.Println(result)
}
