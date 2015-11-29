package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

type interval struct {
	s, e int
}

type intervals []interval

func (in intervals) Len() int           { return len(in) }
func (in intervals) Swap(i, j int)      { in[i], in[j] = in[j], in[i] }
func (in intervals) Less(i, j int) bool { return in[i].e < in[j].e }

var t [100000]interval

func main() {
	var n int
	s := bufio.NewScanner(os.Stdin)
	s.Split(bufio.ScanWords)
	i, j := -1, 0
	for s.Scan() {
		k, _ := strconv.Atoi(s.Text())
		if i == -1 {
			n = k
		} else if i%2 == 0 {
			t[j].s = k
		} else {
			t[j].e = k
			j++
		}
		i++
	}
	sort.Sort(intervals(t[:n]))
	var l, r int
	for i := 0; i < n; i++ {
		if t[i].s > l {
			l = t[i].e
			r++
		}
	}
	fmt.Println(r)
}
