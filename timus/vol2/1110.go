package main

import (
	"fmt"
	"strings"
	"strconv"
)

func main() {
	var n, m, y int
	fmt.Scanf("%d %d %d", &n, &m, &y)
	res := make([]string, 0)
	for i := 1; i < m; i++ {
		k := i
		for j := 1; j < n; j++ {
			k = (k * i) % m
		}
		if k == y {
			res = append(res, strconv.Itoa(i))
		}
	}
	if len(res) == 0 {
		fmt.Println(-1)
	} else {
		fmt.Println(strings.Join(res, " "))
	}
}

