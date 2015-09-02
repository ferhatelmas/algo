package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)

	switch n {
	default:
		fmt.Println("Glupenky Pierre")
	case 1:
		fmt.Println("01")
	case 2:
		fmt.Println("11 01")
	case 3:
		fmt.Println("16 06 68")
	case 4:
		fmt.Println("16 06 68 88")
	}
}
