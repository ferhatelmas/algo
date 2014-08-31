package main

import "fmt"

func main() {
	var n, m int
	fmt.Scanf("%d %d", &n, &m)
	if n%2 == 1 && m%2 == 1  {
		fmt.Println("[second]=:]")
	} else {
		fmt.Println("[:=[first]")
	}
}
