package replace

import (
	"reflect"
	"testing"
)

func TestReplace_elements_with_greatest_element_on_right_side(t *testing.T) {
	type args struct {
		src []int
	}
	tests := []struct {
		name       string
		args       args
		wantResult []int
	}{
		{
			name:       "Normal pass test",
			args:       args{[]int{17, 18, 5, 4, 6, 1}},
			wantResult: []int{18, 6, 6, 6, 1, -1},
		},
		{
			name:       "One length source",
			args:       args{[]int{400}},
			wantResult: []int{-1},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if gotResult := Replace_elements_with_greatest_element_on_right_side(tt.args.src); !reflect.DeepEqual(gotResult, tt.wantResult) {
				t.Errorf("Replace_elements_with_greatest_element_on_right_side() = %v, want %v", gotResult, tt.wantResult)
			}
		})
	}
}
