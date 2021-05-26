package maxconsecutiveonestwo

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func Maxconsecutiveonestwo(src []int) (result int) {
	pre, now, add := 0, 0, 0
	result = 0
	for _, part := range src {
		if part == 0 {
			add = 1
			pre, now = now, 0
		} else {
			now++
			result = max(result, pre+now+add)
		}
	}
	result = max(result, pre+now+add)
	return result
}
