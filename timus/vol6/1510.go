package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var n, v int
	var t, m string
	fmt.Scan(&n)
	v = n / 2
	c := map[string]int{}
	s := bufio.NewScanner(os.Stdin)
	s.Split(bufio.ScanLines)
	for s.Scan() {
		t = s.Text()
		c[t]++
		if c[t] > v {
			m = t
		}
	}
	fmt.Println(m)
}
