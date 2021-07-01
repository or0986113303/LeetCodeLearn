package main

import (
	"fmt"
	selfservice "selfservice/programs"

	"github.com/kardianos/service"
)

var (
	serviceName        = "SimpleService"
	serviceDescription = "This service is a simple test for learning"
)

func main() {

	serviceConfig := &service.Config{
		Name:        serviceName,
		DisplayName: serviceName,
		Description: serviceDescription,
	}

	prg := &selfservice.Program{}
	s, err := service.New(prg, serviceConfig)
	if err != nil {
		fmt.Println("Cannot create the service: " + err.Error())
	}
	err = s.Run()
	if err != nil {
		fmt.Println("Cannot start the service: " + err.Error())
	}
}
