package main

import "fmt"

func main() {
	var n, s, k int
	var satisfactory bool
	fmt.Scan(&n)
	for i := 0; i < n; i++ {
		fmt.Scan(&k)
		if k <= 3 {
			satisfactory = true
		}
		s += k
	}
	if satisfactory {
		fmt.Println("None")
	} else if n*5 == s {
		fmt.Println("Named")
	} else if float64(s)/float64(n) >= 4.5 {
		fmt.Println("High")
	} else {
		fmt.Println("Common")
	}
}
