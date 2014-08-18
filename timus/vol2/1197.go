package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	for i := 0; i<n; i++ {
		var s string
		fmt.Scan(&s)
		x, y := int(s[0]-'a'+1), int(s[1]-'0')
		c := 0
		for i := -2; i < 3; i++ {
			for j := -2; j < 3; j++ {
				if (i*j == 2 || i*j == -2) && 0 < x-i && x-i < 9 && 0 < y-j && y-j < 9 {
					c += 1
				}
			}
		}
		fmt.Println(c)
	}
}


