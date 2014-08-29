package main

import (
	"fmt"
	"bufio"
	"os"
	"strings"
	"strconv"
	"sort"
)

func main() {
	s, _ := bufio.NewReader(os.Stdin).ReadString(0)
	var (
		ns []int
		n int
		c = 0
	)
	for i, v := range strings.Fields(s) {
		t, _ := strconv.Atoi(v)
		if i == 0 {
		   	n = t
			ns = make([]int, n)
		} else if i <= n {
			ns[i-1] = t
			if i == n {
				sort.Ints(ns)
			}
		} else if i > n+1 && binSearch(ns, t) > -1 {
			c += 1
		}
	}
	fmt.Println(c)
}

func binSearch(ls []int, k int) int {
	s, e := 0, len(ls) - 1
	for s <= e {
		m := (s + e) / 2
		if ls[m] == k {
			return m
		} else if ls[m] < k {
			s = m + 1
		} else {
			e = m - 1
		}
	}
	return -1
}

