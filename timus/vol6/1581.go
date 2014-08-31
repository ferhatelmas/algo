package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	s, _ := bufio.NewReader(os.Stdin).ReadString(0)
	c, n := 0, 0
	res := make([]string, 0)
	for i, vv := range strings.Fields(s) {
		v, _ := strconv.Atoi(vv)
		if i > 0 {
			if v == c {
				n += 1
			} else {
				res = append(append(res, strconv.Itoa(n)), strconv.Itoa(c))
				c = v
				n = 1
			}
		}
	}
	res = append(append(res, strconv.Itoa(n)), strconv.Itoa(c))
	fmt.Println(strings.Join(res[2:], " "))
}
