package linkedlistcycle

import "testing"

func TestLinkedlistcycle(t *testing.T) {
	type args struct {
		head *ListNode
	}
	tests := []struct {
		name       string
		args       args
		wantResult bool
	}{
		{
			name:       "Normal test for long input",
			args:       args{&ListNode{Val: 3, Next: &ListNode{Val: 2, Next: &ListNode{Val: 0, Next: &ListNode{Val: 4, Next: nil}}}}},
			wantResult: false,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if gotResult := Linkedlistcycle(tt.args.head); gotResult != tt.wantResult {
				t.Errorf("Linkedlistcycle() = %v, want %v", gotResult, tt.wantResult)
			}
		})
	}
}
