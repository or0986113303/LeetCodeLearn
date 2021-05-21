package sortarraybyparity

import (
	"reflect"
	"testing"
)

func TestSort_array_by_parity(t *testing.T) {
	type args struct {
		src []int
	}
	tests := []struct {
		name       string
		args       args
		wantResult []int
	}{
		{
			name:       "Basic pass test",
			args:       args{[]int{3, 1, 2, 4}},
			wantResult: []int{2, 4, 3, 1},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if gotResult := Sort_array_by_parity(tt.args.src); !reflect.DeepEqual(gotResult, tt.wantResult) {
				t.Errorf("Sort_array_by_parity() = %v, want %v", gotResult, tt.wantResult)
			}
		})
	}
}
