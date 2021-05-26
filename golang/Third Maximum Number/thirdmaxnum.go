package thirdmaxnum

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

func mergesort(src []int) (result []int) {

	if len(src) < 2 {
		result = src
		return result
	}

	middle := len(src) / 2
	left := src[:middle]
	right := src[middle:]
	return merge(mergesort(left), mergesort(right))
}

func ThirdMaxNum(src []int) (result int) {
	sortedsrc := mergesort(src)
	candidate := make([]int, 0)
	conditionlength := 3
	for _, part := range sortedsrc {
		candlength := len(candidate)
		if candlength == 0 {
			candidate = append(candidate, part)
		} else {
			if part > candidate[candlength-1] {
				if candlength < conditionlength {
					candidate = append(candidate, part)
				} else {
					candidate = append(candidate, part)
					candidate = candidate[1:]
				}
			}
		}
	}

	if len(candidate) != 3 {
		result = candidate[len(candidate)-1]
	} else {
		result = candidate[0]
	}

	return result
}
