package main

import (
	"fmt"
)

func two_sum(src []int, target int) []int {
	if src == nil {
		return nil
	}

	hashmap := make(map[int]int)
	//hashmap = make(map[int]int)

	for parts, index := range src {
		idx, ok := hashmap[target-index]
		if ok {
			return []int{idx, parts}
		}
		hashmap[index] = parts
	}

	return nil
}

func main() {
	fmt.Println("hello")
	src := []int{2, 7, 11, 15}
	target := 9
	result := two_sum(src, target)
	fmt.Println(result)
}
