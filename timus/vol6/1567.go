package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	m := make(map[rune]int, 0)
	for i, v := range []string{"", "adgjmpsvy. ", "behknqtwz,", "cfilorux!"} {
		if i > 0 {
			for _, e := range v {
				m[e] = i
			}
		}
	}
	s, _ := bufio.NewReader(os.Stdin).ReadString(0)
	c := 0
	for _, e := range s {
		if n, ok := m[e]; ok {
			c += n
		}
	}
	fmt.Println(c)
}
