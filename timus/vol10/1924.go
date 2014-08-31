package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	if ((n + 1) / 2) % 2 == 1 {
		fmt.Println("grimy")
	} else {
		fmt.Println("black")
	}
}
