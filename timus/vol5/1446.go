package main

import (
	"fmt"
	"bufio"
	"os"
)

func main() {
	houses := []string{"Slytherin", "Hufflepuff", "Gryffindor", "Ravenclaw"}

	m := make(map[string][]string)
	for _, house := range houses {
		m[house] = make([]string, 0, 1000)
	}
	s := bufio.NewScanner(os.Stdin)
	s.Scan()
	for s.Scan() {
		student := s.Text()
		s.Scan()
		house := s.Text()
		m[house] = append(m[house], student)
	}

	for i, house := range houses {
		fmt.Printf("%s:\n", house)
		for _, student := range m[house] {
			fmt.Println(student)
		}
		if i < len(houses) - 1 {
			fmt.Println()
		}
	}
}

