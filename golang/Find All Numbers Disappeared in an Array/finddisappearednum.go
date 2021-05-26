package finddisappearednum

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

func mergesort(src []int) []int {
	if len(src) <= 1 {
		return src
	}

	middle := len(src) / 2

	left := src[:middle]
	right := src[middle:]

	return merge(mergesort(left), mergesort(right))
}

func Finddisappearednum(src []int) (result []int) {

	tmp := make([]int, len(src))
	result = make([]int, 0)
	sortedsrc := mergesort(src)

	for _, part := range sortedsrc {
		tmp[part-1]++
	}

	for index, part := range tmp {
		if part == 0 {
			result = append(result, index+1)
		}
	}

	return result
}
