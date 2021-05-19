package main

import "testing"

func TestValid_mountain_array(t *testing.T) {
	type args struct {
		src []int
	}
	tests := []struct {
		name       string
		args       args
		wantResult bool
	}{
		{
			name:       "normal pass test",
			args:       args{[]int{0, 3, 2, 1}},
			wantResult: true,
		},
		{
			name:       "low length source fail test",
			args:       args{[]int{2, 1}},
			wantResult: false,
		},
		{
			name:       "normal fail test",
			args:       args{[]int{3, 5, 5}},
			wantResult: false,
		},
		{
			name:       "peek at tail fail test",
			args:       args{[]int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}},
			wantResult: false,
		},
		{
			name:       "peek at head fail test",
			args:       args{[]int{9, 8, 7, 6, 5, 4, 3, 2, 1, 0}},
			wantResult: false,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if gotResult := Valid_mountain_array(tt.args.src); gotResult != tt.wantResult {
				t.Errorf("Valid_mountain_array() = %v, want %v", gotResult, tt.wantResult)
			}
		})
	}
}
