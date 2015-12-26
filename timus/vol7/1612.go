package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
)

var r = regexp.MustCompile(`[\.,\-\:!\?]`)

func main() {
	s := bufio.NewScanner(os.Stdin)
	s.Split(bufio.ScanWords)
	var tram, trolleybus int
	for s.Scan() {
		for _, w := range r.Split(s.Text(), -1) {
			if w == "tram" {
				tram++
			} else if w == "trolleybus" {
				trolleybus++
			}
		}
	}
	if tram > trolleybus {
		fmt.Println("Tram driver")
	} else if trolleybus > tram {
		fmt.Println("Trolleybus driver")
	} else {
		fmt.Println("Bus driver")
	}
}
