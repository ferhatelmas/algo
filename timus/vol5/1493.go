package main

import (
	"fmt"
	"strconv"
)

func main() {
	var s string
	fmt.Scan(&s)
	k, _ := strconv.Atoi(s)
	if diff(k+1) == 0 || diff(k-1) == 0 {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}

func diff(a int) int {
	s := strconv.Itoa(a)
	if len(s) < 4 {
		return sum(s)
	}
	i := len(s) - 3
	return sum(s[:i]) - sum(s[i:])
}

func sum(s string) (sum int) {
	sum = 0
	for _, c := range s {
		sum += int(c - '0')
	}
	return
}

