package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func Test_remove_duplicates_from_sorted_array(t *testing.T) {
	src := []int{0, 0, 1, 1, 1, 2, 2, 3, 3, 4}
	benchmakrlength := 5
	benchmarkresult := []int{0, 1, 2, 3, 4}
	length, result := remove_duplicates_from_sorted_array(src)
	assert.Equal(t, benchmakrlength, length)
	assert.Equal(t, benchmarkresult, result)
}
