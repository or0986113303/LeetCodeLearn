package library

import "sync"

type Queue struct {
	sync.Mutex
	Items []interface{}
}

func (que *Queue) Push(item interface{}) {
	que.Lock()
	defer que.Unlock()
	que.Items = append(que.Items, item)
}

func (que *Queue) Pop() interface{} {
	que.Lock()
	defer que.Unlock()
	if len(que.Items) == 0 {
		return nil
	}
	item := que.Items[0]
	que.Items = que.Items[1:]
	return item
}

func NewQueue(capacity int) *Queue {
	return &Queue{
		Items: make([]interface{}, 0, capacity),
	}
}
