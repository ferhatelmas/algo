package main

import "fmt"

func main() {
	var j int
	fmt.Scan(&j)
	if j <= 0 {
		fmt.Println(-(j * (j-1) / 2) + 1)
	} else {
		fmt.Println((j * (j+1) / 2))
	}
}
