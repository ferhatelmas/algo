package main

import "fmt"

var ns = []string{
	"abc",
	"acb",
	"bac",
	"bca",
	"cab",
	"cba",
}

func main() {
	var n, j int
	fmt.Scan(&n)
	if n*6 > 100000 {
		fmt.Println("TOO LONG")
	} else if n == 1 {
		fmt.Printf("a\nb\nc\n")
	} else {
		for i := 0; i < 6; i++ {
			s := ns[i]
			for j = 0; j+len(s) <= n; j += 3 {
				fmt.Print(s)
			}
			if j < n {
				fmt.Print(s[0 : n-j])
			}
			fmt.Println()
		}
	}
}
