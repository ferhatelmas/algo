package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	s := bufio.NewScanner(os.Stdin)
	s.Split(bufio.ScanLines)
	m := map[string]bool{}
	c := 0
	for s.Scan() {
		ln := s.Text()
		if m[ln] {
			c += 1
		}
		m[ln] = true
	}
	fmt.Println(c)
}
