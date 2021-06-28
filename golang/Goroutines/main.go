package main

import (
	"fmt"
	"time"
)

func Say(src string) {
	for index := 0; index < 5; index++ {
		fmt.Println(src)
		time.Sleep(100 * time.Millisecond)
	}
}

func main() {
	go Say("Hello")
	Say("World")
}
