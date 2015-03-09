package main

import "fmt"

func main() {
	var p, c, s, e, r int
	fmt.Scanf("%d %d %d %d", &p, &c, &s, &e)
	if s < e {
		r = c*2 + (c*2+p)*(e-s-1)
	} else {
		r = p + (c*2+p)*(s-e)
	}
	fmt.Println(r)
}
