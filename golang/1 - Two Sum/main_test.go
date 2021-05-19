package main

import (
	"reflect"
	"testing"
)

func TestTwo_sum(t *testing.T) {
	type args struct {
		src    []int
		target int
	}
	tests := []struct {
		name string
		args args
		want []int
	}{
		{
			name: "Normal test",
			args: args{
				src:    []int{2, 7, 11, 15},
				target: 9,
			},
			want: []int{0, 1},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := Two_sum(tt.args.src, tt.args.target); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("Two_sum() = %v, want %v", got, tt.want)
			}
		})
	}
}
