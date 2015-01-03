package main

import "fmt"

func aFun(n, pos int) {
	fmt.Printf("sin(%d", pos)
	if pos < n {
		if pos%2 == 1 {
			fmt.Print("-")
		} else {
			fmt.Print("+")
		}
		aFun(n, pos+1)
	}
	fmt.Print(")")
}

func sFun(n, pos int) {
	if pos < n {
		fmt.Print("(")
		sFun(n, pos+1)
		fmt.Print(")")
	}
	aFun(n+1-pos, 1)
	fmt.Printf("+%d", pos)
}

func main() {
	var n int
	fmt.Scan(&n)
	sFun(n, 1)
}
