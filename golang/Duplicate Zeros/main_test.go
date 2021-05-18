package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func Test_duplicate_zeros(t *testing.T) {
	src := []int{1, 0, 2, 3, 0, 4, 5, 0}
	bencksrc := []int{1, 0, 0, 2, 3, 0, 0, 4}
	duplicate_zeros(src)
	assert.Equal(t, bencksrc, src)
}
