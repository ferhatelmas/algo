package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	var n int
	fmt.Scan(&n)
	buf := make([]string, n)
	for i := 0; i < n; i++ {
		buf[i] = strconv.Itoa(i)
	}
	fmt.Println(strings.Join(buf, " "))
}

