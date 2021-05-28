package maximumToys

func merge(left, right []int32) (result []int32) {

	result = make([]int32, len(left)+len(right))

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

func mergesort(src []int32) (result []int32) {

	if len(src) < 2 {
		result = src
		return result
	}

	middle := len(src) / 2
	left := src[:middle]
	right := src[middle:]
	return merge(mergesort(left), mergesort(right))
}

func MaximumToys(prices []int32, k int32) int32 {

	sortedsrc := mergesort(prices)
	sumtmp := int32(0)
	count := int32(0)
	for _, part := range sortedsrc {
		sumtmp += part
		if sumtmp <= k {
			count++
		}
	}

	return count
}
