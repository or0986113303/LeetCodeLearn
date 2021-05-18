package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func Test_squares_of_a_sorted_array(t *testing.T) {
	src := []int{-7, -3, 2, 3, 11}
	benckresult := []int{4, 9, 9, 49, 121}
	result := squares_of_a_sorted_array(src)
	assert.Equal(t, benckresult, result)
}
