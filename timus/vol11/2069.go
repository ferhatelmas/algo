package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func read(n int, s *bufio.Scanner) []int {
	ns := make([]int, n)
	for i := range ns {
		s.Scan()
		ns[i], _ = strconv.Atoi(s.Text())
	}
	return ns
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func do(cmp func(a, b int) int, ns ...int) int {
	m := ns[0]
	for _, n := range ns[1:] {
		m = cmp(m, n)
	}
	return m
}

func main() {
	s := bufio.NewScanner(os.Stdin)
	s.Scan()
	parts := strings.Split(s.Text(), " ")
	v, _ := strconv.Atoi(parts[0])
	h, _ := strconv.Atoi(parts[1])

	vs, hs := read(v, s), read(h, s)
	fmt.Println(
		do(
			max,
			do(min, hs[0], vs[len(vs)-1]),
			do(min, vs[0], hs[len(hs)-1]),
			do(min, hs[0], hs[len(hs)-1], do(max, vs...)),
			do(min, vs[0], vs[len(vs)-1], do(max, hs...)),
		),
	)
}
