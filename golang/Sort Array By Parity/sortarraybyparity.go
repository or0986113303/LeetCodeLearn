package sortarraybyparity

func Sort_array_by_parity(src []int) (result []int) {
	eventmp := make([]int, 0)
	oddtmp := make([]int, 0)

	for _, part := range src {
		if part%2 == 0 {
			eventmp = append(eventmp, part)
		} else {
			oddtmp = append(oddtmp, part)
		}
	}

	result = append(eventmp, oddtmp...)

	return result
}
