package main

import (
	"fmt"
	"sort"
	"bufio"
	"os"
	"strconv"
	"strings"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	text, _ := in.ReadString(0)
	ns := make([]int, 0)
	for i, v := range strings.Fields(text) {
		if i > 0 {
			j, _ := strconv.Atoi(v)
			ns = append(ns, j)
		}
	}
	for _, v := range do(do(ns)) {
		fmt.Println(v)
	}
}

func do(ns []int) []int {
	res, l := make([]int, 0), len(ns)

	if l > 0 {
		sort.Ints(ns)
		res = append(res, l)
		for i, j := 1, 0; i < ns[l-1]; i++ {
			for j < l && ns[j] <= i {
				j += 1
			}
			res = append(res, l-j)
		}
	}

	return res
}
