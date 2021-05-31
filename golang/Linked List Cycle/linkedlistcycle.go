package linkedlistcycle

type ListNode struct {
	Val  int
	Next *ListNode
}

func Linkedlistcycle(head *ListNode) (result bool) {
	result = false
	if head == nil {
		return result
	}

	slow := head.Next
	if slow == nil {
		return result
	}

	fast := slow.Next

	for fast != nil && slow != nil {
		if fast == slow {
			result = true
			return result
		}

		slow = slow.Next

		fast = fast.Next
		if fast != nil {
			fast = fast.Next
		}
	}

	return result
}
