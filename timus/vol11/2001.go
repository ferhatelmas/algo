package main

import (
	"fmt"
	"bufio"
	"os"
	"strconv"
)

func main() {
	n := make([]int, 0)
	s := bufio.NewScanner(os.Stdin)
	s.Split(bufio.SplitFunc(bufio.ScanWords))
	for s.Scan() {
		k, _ := strconv.Atoi(s.Text())
		n = append(n, k)
	}
	fmt.Println(n[0] - n[4], n[1] - n[3])
}
