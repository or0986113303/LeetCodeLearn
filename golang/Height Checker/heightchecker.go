package heightchecker

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

func Heightchecker(src []int) (result int) {
	sortedsrc := mergesort(src)
	result = 0

	for index, part := range src {
		if part != sortedsrc[index] {
			result++
		}
	}

	return result
}
