package main

import (
	"fmt"
	"os"
)

func getUsername() string {
	username := os.Getenv("USER")
	return username
}

func main() {
	fmt.Printf("Hello %s!\n", getUsername())
}
