package main

import "fmt"

func main() {
	var s string
	var m rune = 1
	ns := make([]rune, 37)

	fmt.Scan(&s)
	for _, n := range s {
		if n <= '9' {
			n = n - '0'
		} else {
			n = n - 'A' + 10
		}
		if n > m {
			m = n
		}
		for i := m + 1; i < 37; i++ {
			ns[i] = (ns[i]*i + n) % (i - 1)
		}
	}
	for i := m + 1; i < 37; i++ {
		if ns[i] == 0 {
			fmt.Println(i)
			return
		}
	}
	fmt.Println("No solution.")
}
