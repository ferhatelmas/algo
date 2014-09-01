package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	var n int
	fmt.Scan(&n)
	ns := make([][]string, n)
	for i := 0; i < n; i++ {
		ns[i] = make([]string, n)
	}
	c := 1
	for k := n-1; k > -1; k-- {
		for i, j := 0, k; i < n && j < n; i++ {
			ns[i][j] = strconv.Itoa(c)
			c += 1
			j += 1
		}
	}
	for k := 1; k < n; k++ {
		for i, j := k, 0; i < n && j < n; i++ {
			ns[i][j] = strconv.Itoa(c)
			c += 1
			j += 1
		}
	}
	for _, row := range ns {
		fmt.Println(strings.Join(row, " "))
	}
}
