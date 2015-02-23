package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	if (12-n)*45 <= 240 {
		fmt.Println("YES")
	} else {
		fmt.Println("NO")
	}
}
