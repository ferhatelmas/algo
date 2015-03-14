package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var n int
	var t, m string
	fmt.Scan(&n)
	n /= 2
	c := map[string]int{}
	s := bufio.NewScanner(os.Stdin)
	s.Split(bufio.ScanLines)
	for s.Scan() {
		t = s.Text()
		c[t]++
		if c[t] > n {
			m = t
		}
	}
	fmt.Println(m)
}
