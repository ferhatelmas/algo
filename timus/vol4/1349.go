package main

import "fmt"

func main() {
	var k int
	fmt.Scan(&k)
	if k == 1 {
		fmt.Printf("1 2 3\n")
	} else if k == 2 {
		fmt.Printf("3 4 5\n")
	} else {
		fmt.Println(-1)
	}
}
