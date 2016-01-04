package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)

	if n == 1 {
		fmt.Println("14")
	} else if n == 2 {
		fmt.Println("155")
	} else {
		fmt.Print("1575")
		for i := 3; i < n; i++ {
			fmt.Print("0")
		}
	}
}
