package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func Test_find_numbers_with_even_number_of_digits(t *testing.T) {
	src := []int{12, 345, 2, 6, 7896}
	result := find_numbers_with_even_number_of_digits(src)
	benckresult := 2
	assert.Equal(t, result, benckresult)
}
