package replace

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

func findmax(src []int) int {
	result := mergesort(src)
	return result[len(result)-1]
}

func Replace_elements_with_greatest_element_on_right_side(src []int) (result []int) {
	/*
		if len(src) == 1 {
			src[0] = -1
			result = src
			return result
		}

		for index := 0; index < len(src)-1; index++ {
			maxnumber := findmax(src[index+1:])
			src[index] = maxnumber
		}

		src[len(src)-1] = -1
		result = src
		return result
	*/
	if len(src) == 1 {
		src[0] = -1
		result = src
		return result
	}
	max := 0
	for index := len(src) - 1; index >= 0; index-- {
		tmp := max
		if src[index] > max {
			max = src[index]
		}
		src[index] = tmp
	}

	src[len(src)-1] = -1
	result = src
	return result
}
