package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func Test_merge_sorted_array(t *testing.T) {
	nums1 := []int{1, 2, 3, 0, 0, 0}
	m := 3
	nums2 := []int{2, 5, 6}
	n := 3
	benchmark := []int{1, 2, 2, 3, 5, 6}
	result := merge(nums1, m, nums2, n)
	assert.Equal(t, benchmark, result)
}
