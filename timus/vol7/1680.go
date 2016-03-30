package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	var n int
	i := -1
	s := bufio.NewScanner(os.Stdin)
	m := map[string]bool{}
	for s.Scan() {
		if i == -1 {
			n, _ = strconv.Atoi(strings.Split(s.Text(), " ")[2])
			i++
		} else if i <= n {
			name := s.Text()
			key := strings.Split(name, " #")[0]
			if !m[key] {
				if i == n {
					fmt.Println(name)
					break
				}
				m[key] = true
				i++
			}
		}
	}
}
