package thirdmaxnum

import "testing"

func TestThirdMaxNum(t *testing.T) {
	type args struct {
		src []int
	}
	tests := []struct {
		name       string
		args       args
		wantResult int
	}{
		{
			name:       "Normal test result equal one",
			args:       args{[]int{2, 2, 3, 1}},
			wantResult: 1,
		},
		{
			name:       "Normal test result equal two",
			args:       args{[]int{1, 2}},
			wantResult: 2,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if gotResult := ThirdMaxNum(tt.args.src); gotResult != tt.wantResult {
				t.Errorf("ThirdMaxNum() = %v, want %v", gotResult, tt.wantResult)
			}
		})
	}
}
