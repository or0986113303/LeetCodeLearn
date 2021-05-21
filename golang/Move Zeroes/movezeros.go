package movezeros

func Movezeros(src []int) (result []int) {
	if len(src) <= 1 {
		result = src
		return result
	}

	for index := 0; index < len(src); {
		if src[index] == 0 {
			result = append(result, 0)
			src = append(src[:index], src[index+1:]...)
			index--
		}
		index++
	}
	src = append(src, result...)

	result = src
	return result
}
