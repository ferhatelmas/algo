package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	var n, k, s int
	var ns []int
	sc := bufio.NewScanner(os.Stdin)
	for sc.Scan() {
		n, _ := strconv.Atoi(sc.Text())
		ns = append(ns, n)
		if n == -1 {
			k++
		}
	}
	ns, n = ns[1:], len(ns)-1
	cs := make([]int, n)
	copy(cs, ns)
	for i := 0; i < n; i++ {
		if ns[i] == -1 {
			s--
			fmt.Println(cs[s])
			k--
		} else if ns[i] == 0 {
			if s < k {
				t, d := k, false
				if 2*s <= t {
					t, d = 2*s, true
				}
				for j := 0; j < t && (!d || j < s); j++ {
					l := s - j - 1
					if j >= s {
						l += t
					}
					cs[t-j-1] = cs[l]
				}
				s = t
			}
		} else {
			cs[s] = ns[i]
			s++
		}
	}
}
