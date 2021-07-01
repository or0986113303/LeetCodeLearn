package selfservice

import (
	"fmt"
	"sync"
	"time"

	"github.com/kardianos/service"
)

type Program struct{}

var (
	serviceIsRunning bool
	programIsRunning bool
	waitSync         sync.Mutex
)

func (P *Program) run() {
	fmt.Println("Run service ...")
	for serviceIsRunning {
		fmt.Println("Program is running")
		waitSync.Lock()
		programIsRunning = true
		waitSync.Unlock()
		time.Sleep(1 * time.Second)
		waitSync.Lock()
		programIsRunning = false
		waitSync.Unlock()
	}
}

func (P *Program) Start(s service.Service) error {
	fmt.Println("Start service ...")
	waitSync.Lock()
	serviceIsRunning = true
	waitSync.Unlock()
	go P.run()
	return nil
}

func (P *Program) Stop(s service.Service) error {
	fmt.Println("Stop service ...")

	waitSync.Lock()
	serviceIsRunning = false
	waitSync.Unlock()

	for programIsRunning {
		time.Sleep(1 * time.Second)
	}

	fmt.Println(s.String() + " stopped")

	return nil
}
