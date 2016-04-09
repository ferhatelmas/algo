package main

import "fmt"

const limit = 10000

func main() {
	var n int
	fmt.Scan(&n)

	a, u := make([]int, limit), make([]int, limit)
	for i := 0; i < limit; i++ {
		u[i] = -1
		if i < n {
			fmt.Scan(&a[i])
		}
	}

	var sum int
	u[0] = 0

	for i := 0; i < n; i++ {
		sum += a[i]
		k := sum % n
		if u[k] != -1 {
			fmt.Println(i - u[k] + 1)
			for j := u[k]; j <= i; j++ {
				fmt.Println(a[j])
			}
			break
		} else {
			u[k] = i + 1
		}
	}
}
