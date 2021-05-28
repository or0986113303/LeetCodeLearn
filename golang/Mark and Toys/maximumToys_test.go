package maximumToys

import "testing"

func TestMaximumToys(t *testing.T) {
	type args struct {
		prices []int32
		k      int32
	}
	tests := []struct {
		name string
		args args
		want int32
	}{
		{
			name: "Normal test",
			args: args{
				prices: []int32{1, 12, 5, 111, 200, 1000, 10},
				k:      50,
			},
			want: 4,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := MaximumToys(tt.args.prices, tt.args.k); got != tt.want {
				t.Errorf("MaximumToys() = %v, want %v", got, tt.want)
			}
		})
	}
}
