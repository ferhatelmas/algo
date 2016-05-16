package main

import "fmt"

const mod = 1000000009

var (
	ns    [10010][100]int
	prime [1000]bool
)

func isPrime(x int) bool {
	for i := 2; i*i <= x; i++ {
		if x%i == 0 {
			return false
		}
	}
	return true
}

func main() {
	var n, ans int
	fmt.Scan(&n)
	for i := 100; i < 1000; i++ {
		if prime[i] = isPrime(i); prime[i] {
			ns[3][i%100]++
		}
	}
	for i := 4; i <= n; i++ {
		for j := 11; j < 100; j += 2 {
			for k := 1; k < 10; k += 2 {
				x := j*10 + k
				if prime[x] {
					ns[i][x%100] = (ns[i][x%100] + ns[i-1][j]) % mod
				}
			}
		}
	}
	for i := 0; i < 100; i++ {
		ans = (ans + ns[n][i]) % mod
	}
	fmt.Println(ans)
}
