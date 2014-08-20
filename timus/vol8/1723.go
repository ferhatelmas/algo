package main

import "fmt"

func main() {
	var m = make(map[string]int)
	var s string
	fmt.Scan(&s)
	l := len(s)
	for i := 0; i < l; i++{
		for j := i+1; j <= l; j++ {
			if v, ok := m[s[i:j]]; ok {
				m[s[i:j]] = v + 1
			} else {
				m[s[i:j]] = 1
			}
		}
	}

	c := 0
	l = 0
	for k, v := range m {
		if v > c || (v == c && len(k) > l) {
			s = k
			l = len(s)
			c = v
		}
	}
	fmt.Println(s)
}

