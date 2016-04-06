package main

import "fmt"

func main() {
	var k, r int
	fmt.Scan(&k)
	for i := 1; i <= k/i; i++ {
		if k%i == 0 {
			if i >= 3 {
				r = i - 1
				break
			}
			if k/i >= 3 {
				r = k/i - 1
			}
		}
	}
	fmt.Println(r)
}
