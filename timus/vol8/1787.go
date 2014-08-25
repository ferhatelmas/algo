package main

import (
	"fmt"
	"bufio"
	"os"
	"strconv"
)

func main() {
	s := bufio.NewScanner(os.Stdin)
	s.Split(bufio.SplitFunc(bufio.ScanWords))
	c, i, k := 0, 0, 0
	for s.Scan() {
		i++
		v, _ := strconv.Atoi(s.Text())
		if i == 1 {
			k = v
		} else if i > 2 {
			c += v - k
			if c < 0 {
				c = 0
			}
		}
	}
	fmt.Println(c)
}
