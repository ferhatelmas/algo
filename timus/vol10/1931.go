package main

import (
	"bufio"
	"os"
	"strings"
	"strconv"
	"fmt"
)

func main() {
	r := bufio.NewReader(os.Stdin)
	text, _ := r.ReadString(0)

	cv, ci, cnt, mv, mi := 0, 0, 0, 0, 0
	for i, v := range strings.Fields(text) {
		if i == 0 {
			continue
		}
		k, _ := strconv.Atoi(v)

		if i == 1 {
			cv = k
		} else {
			cnt++
			if k < cv {
				if cnt > mv {
					mv, mi = cnt, ci
				}
				cv, ci, cnt = k, i-1, 1
			}
		}
	}
	if cnt > mv {
		mi = ci
	}
	fmt.Println(mi + 1)
}
