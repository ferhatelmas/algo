package main

import "fmt"

func main() {
	n := 164000
	sieve := make([]bool, n, n)
	primes := []int{1}
	for i := 2; i < n; i++ {
		if !sieve[i] {
			primes = append(primes, i)
			for j := 2 * i; j < n; j += i {
				sieve[j] = true
			}
		}
	}
	var k int
	for fmt.Scan(&n); n > 0; n-- {
		fmt.Scan(&k)
		fmt.Println(primes[k])
	}
}
