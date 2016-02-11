package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func num(s string) int {
	n, _ := strconv.Atoi(s)
	return n
}

func main() {
	var n int
	ns := make([]int, 1000000)
	s := bufio.NewScanner(os.Stdin)
	for i := -1; s.Scan(); i++ {
		if i == -1 {
			n = num(s.Text())
			continue
		} else {
			ss := strings.Split(s.Text(), " ")
			ns[i] = num(ss[0]) + num(ss[1])
		}
		for j := i; ns[j] > 9; j-- {
			ns[j-1]++
			ns[j] -= 10
		}
	}
	for i := 0; i < n; i++ {
		fmt.Print(ns[i])
	}
}
