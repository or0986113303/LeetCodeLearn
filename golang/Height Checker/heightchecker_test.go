package heightchecker

import "testing"

func TestHeightchecker(t *testing.T) {
	type args struct {
		src []int
	}
	tests := []struct {
		name       string
		args       args
		wantResult int
	}{
		{
			name:       "Basic test output is three",
			args:       args{[]int{1, 1, 4, 2, 1, 3}},
			wantResult: 3,
		},
		{
			name:       "Basic test output is five",
			args:       args{[]int{5, 1, 2, 3, 4}},
			wantResult: 5,
		},
		{
			name:       "Basic test output is zero",
			args:       args{[]int{1, 2, 3, 4, 5}},
			wantResult: 0,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if gotResult := Heightchecker(tt.args.src); gotResult != tt.wantResult {
				t.Errorf("Heightchecker() = %v, want %v", gotResult, tt.wantResult)
			}
		})
	}
}
