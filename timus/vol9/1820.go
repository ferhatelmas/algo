package main

import "fmt"

func main() {
	var n, k int
	fmt.Scanf("%d %d", &n, &k)
	if k > n {
		fmt.Println(2)
	} else {
		n *= 2
		c := n / k
		if n%k > 0 {
			c += 1
		}
		fmt.Println(c)
	}
}

