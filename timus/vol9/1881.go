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
	var h, w int
	c, ln := 0, 1
	for i, v := range strings.Fields(s) {
		if i == 0 {
			h, _ = strconv.Atoi(v)
		} else if i == 1 {
			w, _ = strconv.Atoi(v)
		} else if i == 2 {
			continue
		} else {
			l := len(v)
			c += l
			if c > w {
				c = l + 1
				ln += 1
			} else {
				c += 1
			}
		}
	}
	p := ln / h
	if ln % h != 0 {
		p += 1
	}
	fmt.Println(p)
}
