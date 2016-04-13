package main

import "fmt"

type node struct {
	ls      []int
	visited bool
}

func dfs(ns []node, p int) bool {
	ns[p].visited = true
	for _, i := range ns[p].ls {
		if !ns[i].visited && !dfs(ns, i) {
			return true
		}
	}
	return false
}

func main() {
	var n, k, x, y int
	fmt.Scan(&n)
	fmt.Scan(&k)
	ns := make([]node, 1001)
	for i := 1; i < n; i++ {
		fmt.Scan(&x)
		fmt.Scan(&y)
		ns[x].ls = append(ns[x].ls, y)
		ns[y].ls = append(ns[y].ls, x)
	}
	ns[k].visited = true
	min := 1001
	for _, i := range ns[k].ls {
		if !dfs(ns, i) {
			if i < min {
				min = i
			}
		}
	}
	if min != 1001 {
		fmt.Printf("First player wins flying to airport %d\n", min)
	} else {
		fmt.Println("First player loses")
	}
}
