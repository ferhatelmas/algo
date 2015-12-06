package main

import (
	"fmt"
	"math"
	"sort"
)

type ss []int64

func (s ss) Len() int           { return len(s) }
func (s ss) Less(i, j int) bool { return s[i] < s[j] }
func (s ss) Swap(i, j int)      { s[i], s[j] = s[j], s[i] }

func min(s ss) int64 {
	sort.Sort(s)
	var m int64 = math.MaxInt64
	for i := len(s) - 1; i > 0; i-- {
		k := s[i] - s[i-1]
		if k < m {
			m = k
		}
	}
	return m
}

func main() {
	ns := ss(make([]int64, 3))
	for i := 0; i < 3; i++ {
		fmt.Scan(&ns[i])
	}
	for i := 0; ; i++ {
		k := min(ns)
		if k == 0 {
			fmt.Println(i + 1)
			break
		}
		ns = append(ns, k)
	}
}
