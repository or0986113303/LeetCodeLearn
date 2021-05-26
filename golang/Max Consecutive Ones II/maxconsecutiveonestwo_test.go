package maxconsecutiveonestwo

import "testing"

func TestMaxconsecutiveonestwo(t *testing.T) {
	type args struct {
		src []int
	}
	tests := []struct {
		name       string
		args       args
		wantResult int
	}{
		{
			name:       "Normal test result equal 4",
			args:       args{[]int{1, 0, 1, 1, 0, 1}},
			wantResult: 4,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if gotResult := Maxconsecutiveonestwo(tt.args.src); gotResult != tt.wantResult {
				t.Errorf("Maxconsecutiveonestwo() = %v, want %v", gotResult, tt.wantResult)
			}
		})
	}
}
