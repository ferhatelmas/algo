package main

import "fmt"

const name = "Sandro"

func ascii(a byte) (byte, bool) {
	if a >= 'a' && a <= 'z' {
		return a - 'a', true
	}
	return a - 'A', false
}

func diff(a, b byte) int {
	i, ca := ascii(a)
	j, cb := ascii(b)
	if ca == cb && i == j {
		return 0
	} else if ca != cb && i != j {
		return 10
	}
	return 5
}

func cost(s string) int {
	var sum int
	for i := 0; i < len(name); i++ {
		sum += diff(s[i], name[i])
	}
	return sum
}

func main() {
	var s string
	fmt.Scan(&s)
	min := 60
	for i, l := 6, len(s); i <= l; i++ {
		c := cost(s[i-6 : i])
		if c < min {
			min = c
		}
	}
	fmt.Println(min)
}
