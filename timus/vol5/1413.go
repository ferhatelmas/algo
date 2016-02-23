package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

func main() {
	var x1, x2, y1, y2 float64
	r := bufio.NewReader(os.Stdin)
	for c, err := r.ReadByte(); err == nil && c != '0'; c, err = r.ReadByte() {
		switch c {
		case '1':
			x2--
			y2--
		case '2':
			y1--
		case '3':
			x2++
			y2--
		case '4':
			x1--
		case '6':
			x1++
		case '7':
			x2--
			y2++
		case '8':
			y1++
		case '9':
			x2++
			y2++
		}
	}
	m := math.Sqrt(2) / 2
	fmt.Printf("%.10f %.10f", x1+x2*m, y1+y2*m)
}
