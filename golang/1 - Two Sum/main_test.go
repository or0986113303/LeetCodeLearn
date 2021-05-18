package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func Test_two_sum(t *testing.T) {
	src := []int{2, 7, 11, 15}
	target := 9
	benckmark := []int{0, 1}
	result := two_sum(src, target)
	assert.Equal(t, benckmark, result)
}
