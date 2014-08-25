package main

import (
	"fmt"
	"bufio"
	"os"
)

const (
	s1 = "Emperor Penguin"
	s2 = "Macaroni Penguin"
	s3 = "Little Penguin"
)

func main() {
	n, c1, c2, c3 := 0, 0, 0, 0
	fmt.Scan(&n)
	in := bufio.NewScanner(os.Stdin)
	for in.Scan() {
		switch in.Text() {
		case s1: c1++
		case s2: c2++
		case s3: c3++
		}
	}
	if c1 > c2 && c1 > c3 {
		fmt.Println(s1)
	} else if c2 > c1 && c2 > c3 {
		fmt.Println(s2)
	} else {
		fmt.Println(s3)
	}
}

