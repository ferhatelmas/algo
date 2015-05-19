package main

import "fmt"

func reverse(s string) string {
	n, r := len(s), []rune(s)
	for i := 0; i < n/2; i++ {
		r[i], r[n-1-i] = r[n-1-i], r[i]
	}
	return string(r)
}

func isPalindrome(s string, k int) bool {
	l, r := k, len(s)-1
	for l < r {
		if s[l] != s[r] {
			return false
		}
		l++
		r--
	}
	return true
}

func main() {
	var s string
	for {
		_, err := fmt.Scan(&s)
		if err != nil {
			break
		}
		n := len(s)
		for i := 1; i <= n; i++ {
			if isPalindrome(s, i) {
				fmt.Printf("%s%s\n", s, reverse(s[:i]))
				break
			}
		}
	}
}
