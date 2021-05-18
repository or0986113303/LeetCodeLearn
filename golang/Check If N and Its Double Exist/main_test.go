package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func Test_check_if_n_and_its_double_exist(t *testing.T) {
	src := []int{0, 0}
	benchmark := true
	result := check_if_n_and_its_double_exist(src)
	assert.Equal(t, benchmark, result)
}
