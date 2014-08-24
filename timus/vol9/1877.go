package main

import "fmt"

func main() {
	var l1, l2 int
	fmt.Scanf("%d\n%d", &l1, &l2)
	if l1%2 == 0 || l2%2 == 1 {
		fmt.Println("yes")
	} else {
		fmt.Println("no")
	}
}
