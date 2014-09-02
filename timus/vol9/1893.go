package main

import (
	"fmt"
	"regexp"
	"strconv"
)

func main() {
	var s string
	fmt.Scanf("%s\n", &s)
	seat := regexp.MustCompile(`^(\d+)([A-Z])$`).FindAllStringSubmatch(s, 2)[0]
	r, _ := strconv.Atoi(seat[1])
	if r >= 1 && r <= 2 {
		switch seat[2] {
		case "A", "D": fmt.Println("window")
		default: fmt.Println("aisle")
		}
	} else if r >= 3 && r <= 20 {
		switch seat[2] {
		case "A", "F": fmt.Println("window")
		default: fmt.Println("aisle")
		}
	} else {
		switch seat[2] {
		case "A", "K": fmt.Println("window")
		case "C", "D", "G", "H": fmt.Println("aisle")
		default: fmt.Println("neither")
		}
	}
}
