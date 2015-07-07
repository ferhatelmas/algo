package main

import "fmt"

func main() {
	var n, a, b int
	var op string
	fmt.Scan(&n)

	stacks := map[int][]int{}
	for i := 0; i < n; i++ {
		fmt.Scan(&op)
		if op == "PUSH" {
			fmt.Scan(&a)
			fmt.Scan(&b)
			if m, ok := stacks[a]; ok {
				stacks[a] = append(m, b)
			} else {
				stacks[a] = []int{b}
			}
		} else {
			fmt.Scan(&a)
			m := stacks[a]
			stacks[a] = m[:len(m)-1]
			fmt.Println(m[len(m)-1])
		}
	}
}
