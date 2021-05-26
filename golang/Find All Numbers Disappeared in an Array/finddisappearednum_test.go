package finddisappearednum

import (
	"reflect"
	"testing"
)

func TestFinddisappearednum(t *testing.T) {
	type args struct {
		src []int
	}
	tests := []struct {
		name       string
		args       args
		wantResult []int
	}{
		{
			name:       "Normal test lose two numbers",
			args:       args{[]int{4, 3, 2, 7, 8, 2, 3, 1}},
			wantResult: []int{5, 6},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if gotResult := Finddisappearednum(tt.args.src); !reflect.DeepEqual(gotResult, tt.wantResult) {
				t.Errorf("Finddisappearednum() = %v, want %v", gotResult, tt.wantResult)
			}
		})
	}
}
