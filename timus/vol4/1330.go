package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func conv(s string) int {
	n, _ := strconv.Atoi(s)
	return n
}

func one(s *bufio.Scanner) int {
	s.Scan()
	return conv(s.Text())
}

func two(s *bufio.Scanner) (int, int) {
	s.Scan()
	parts := strings.Split(s.Text(), " ")
	return conv(parts[0]), conv(parts[1])
}

func main() {
	s := bufio.NewScanner(os.Stdin)
	n := one(s)
	ns := make([]int, n)
	ns[0] = one(s)
	for i := 1; i < n; i++ {
		ns[i] = one(s) + ns[i-1]
	}

	n = one(s)
	for i := 0; i < n; i++ {
		t1, t2 := two(s)
		if t1 == 1 {
			fmt.Println(ns[t2-1])
		} else {
			fmt.Println(ns[t2-1] - ns[t1-2])
		}
	}
}
