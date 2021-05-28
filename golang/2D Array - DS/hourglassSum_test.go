package hourglassSum

import "testing"

func TestHourglassSum(t *testing.T) {
	type args struct {
		arr [][]int32
	}
	tests := []struct {
		name string
		args args
		want int32
	}{
		{
			name: "Basic test and result equal to 19",
			args: args{[][]int32{
				{1, 1, 1, 0, 0, 0},
				{0, 1, 0, 0, 0, 0},
				{1, 1, 1, 0, 0, 0},
				{0, 0, 2, 4, 4, 0},
				{0, 0, 0, 2, 0, 0},
				{0, 0, 1, 2, 4, 0},
			}},
			want: 19,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := HourglassSum(tt.args.arr); got != tt.want {
				t.Errorf("HourglassSum() = %v, want %v", got, tt.want)
			}
		})
	}
}
