package main

import (
	"fmt"
	"sort"
	"strconv"
)

type score struct {
	n string
	t int
}

func main() {
	var n int
	var t string
	fmt.Scan(&n)
	scores := make([]*score, n, n)
	for i := 0; i < n; i++ {
		s := &score{}
		fmt.Scan(&s.n)
		fmt.Scan(&t)
		h, _ := strconv.Atoi(t[:2])
		m, _ := strconv.Atoi(t[3:5])
		k, _ := strconv.Atoi(t[6:])
		s.t = 600*h + 10*m + k
		scores[i] = s
	}

	var res []string
	for i := 0; i < n; i++ {
		leader := true
		for j := 0; j < n; j++ {
			if scores[j].t < scores[i].t && scores[j].t+300*j < scores[i].t+300*i {
				leader = false
				break
			}
		}
		if leader {
			res = append(res, scores[i].n)
		}
	}
	sort.Strings(res)
	fmt.Println(len(res))
	for _, v := range res {
		fmt.Println(v)
	}
}
