package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func test_remove_element(t *testing.T) {
	nums := []int{3, 2, 2, 3}
	val := 3
	benckresult := []int{2, 2}
	result := remove_element(nums, val)
	assert.Equal(t, benckresult, nums)
	assert.Equal(t, 2, result)
}
