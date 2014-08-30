package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	ln, _ := bufio.NewReader(os.Stdin).ReadString(0)
	max, maxI, curr := 0, 2, 0
	ns := make([]int, 0)
	for _, v := range strings.Fields(ln) {
		n, _ := strconv.Atoi(v)
		ns = append(ns, n)
	}
	for i, v := range ns {
		if i == 0 {
			continue
		}
		if i < 3 {
			curr += v
		} else if i == 3 {
		   	curr += v
			max = curr
		} else {
			curr += v - ns[i-3]
			if curr > max {
				max = curr
				maxI = i - 1
			}
		}
	}
	fmt.Println(max, maxI)
}
