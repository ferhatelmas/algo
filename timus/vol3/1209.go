package main

import (
	"bytes"
	"fmt"
	"math"
)

func main() {
	var	(
		n int
		k int64
		buf bytes.Buffer
	)
	fmt.Scan(&n)
	for i := 0; i < n; i++ {
		fmt.Scan(&k)
		j := 1 + 8 * (k - 1)
		l := int64(math.Sqrt(float64(j)))
		if j == l * l {
			buf.WriteString("1")
		} else {
			buf.WriteString("0")
		}
		buf.WriteString(" ")
	}
	fmt.Println(buf.String())
}

