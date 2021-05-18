package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func test_main(t *testing.T) {
	src := "test"
	result := hello(src)
	assert.Equal(t, src, result)
}

func Test_max_consecutive_ones(t *testing.T) {
	src := [6]int{1, 0, 1, 1, 0, 1}
	bemchresult := 2
	result := max_consecutive_ones(src[:])
	assert.Equal(t, bemchresult, result)
}
