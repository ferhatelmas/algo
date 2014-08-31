package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	in := bufio.NewScanner(os.Stdin)
	in.Split(bufio.ScanWords)
	ns := make(map[int]int, 0)
	for i := 0; i < 3; i++ {
		processBlock(in, ns)
	}
	c := 0
	for _, v := range ns {
		if v == 3 {
			c += 1
		}
	}
	fmt.Println(c)
}

func processBlock(in *bufio.Scanner, ns map[int]int) {
	n := next(in, true)
	for ; n > 0 && in.Scan(); n-- {
		k := next(in, false)
		if v, ok := ns[k]; ok {
			ns[k] = v + 1
		} else {
			ns[k] = 1
		}
	}
}

func next(in *bufio.Scanner, shouldScan bool) int {
	if shouldScan {
		in.Scan()
	}
	n, _ := strconv.Atoi(in.Text())
	return n
}
