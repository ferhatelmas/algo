package main

import "fmt"

func main() {
	var n int
	fmt.Scanf("%d", &n)
	var s string
	switch {
		case n < 5: s = "few"
		case n < 10: s = "several"
		case n < 20: s = "pack"
		case n < 50: s = "lots"
		case n < 100: s = "horde"
		case n < 250: s = "throng"
		case n < 500: s = "swarm"
		case n < 1000: s = "zounds"
		default: s = "legion"
	}
	fmt.Println(s)
}
