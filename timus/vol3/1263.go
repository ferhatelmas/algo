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
	var (
		l int
		k  float64
		ns map[int]int
	)
	for i, v := range strings.Fields(s) {
		if i == 0 {
			l, _ = strconv.Atoi(v)
			ns = make(map[int]int, l)
			for j := 1; j <= l; j++ {
				ns[j] = 0;
			}
		} else if i == 1 {
			k, _ = strconv.ParseFloat(v, 64)
		} else {
			n, _ := strconv.Atoi(v)
			if j, ok := ns[n]; ok {
				ns[n] = j + 1
			}
		}
	}
	for i := 1; i <= l; i++ {
		v, _ := ns[i]
		fmt.Printf("%.2f%%\n", 100 * float64(v) / k)
	}
}
