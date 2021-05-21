package movezeros

import (
	"reflect"
	"testing"
)

func TestMovezeros(t *testing.T) {
	type args struct {
		src []int
	}
	tests := []struct {
		name       string
		args       args
		wantResult []int
	}{
		{
			name:       " basic pass test",
			args:       args{[]int{0, 1, 0, 3, 12}},
			wantResult: []int{1, 3, 12, 0, 0},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if gotResult := Movezeros(tt.args.src); !reflect.DeepEqual(gotResult, tt.wantResult) {
				t.Errorf("Movezeros() = %v, want %v", gotResult, tt.wantResult)
			}
		})
	}
}
