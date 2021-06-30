package main

import (
	"fmt"
	"sync"
	"time"
)

func wgtest(id int, wg *sync.WaitGroup) {

	defer wg.Done()

	fmt.Printf("Start workd id : %d\n", id)
	time.Sleep(100 * time.Millisecond)
	fmt.Printf("Stop workd id : %d\n", id)
}

func main() {
	fmt.Println("Hello world")

	var wg sync.WaitGroup
	for index := 0; index < 10; index++ {
		wg.Add(1)
		go wgtest(index, &wg)
	}

	wg.Wait()
	fmt.Println("Done")
}
