package main

import "fmt"

func main() {
	var n, r, cnt int64
	var c byte
	for fmt.Scan(&n); n > 0; {
		fmt.Scanf("%c", &c)
		if c == '>' {
			n, cnt = n-1, cnt+1
		} else if c == '<' {
			n, r = n-1, r+cnt
		}
	}
	fmt.Println(r)
}
