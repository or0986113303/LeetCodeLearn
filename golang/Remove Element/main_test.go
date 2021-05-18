package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func Test_remove_element(t *testing.T) {
	nums := []int{3, 2, 2, 3}
	val := 3
	result := remove_element(nums, val)
	assert.Equal(t, 2, result)
}
