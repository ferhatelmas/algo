package main

import (
	"fmt"
	"strconv"
)

func main() {
	var s string
	fmt.Scan(&s)

	ns, l := map[string]bool{}, len(s)
	for i := 1; i < 7; i++ {
		for j := 0; j < l-i+1; j++ {
			ns[s[j:j+i]] = true
		}
	}

	for i := 1; i < 1000000; i++ {
		if !ns[strconv.Itoa(i)] {
			fmt.Println(i)
			break
		}
	}
}
