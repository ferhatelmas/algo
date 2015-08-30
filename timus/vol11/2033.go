package main

import "fmt"

type stat struct {
	count, price int
}

func main() {
	stats := make(map[string]*stat, 6)
	var name string
	var p int
	for i := 0; i < 6; i++ {
		fmt.Scan(&name)
		fmt.Scan(&name)
		if s, ok := stats[name]; !ok {
			s = &stat{count: 1}
			fmt.Scan(&s.price)
			stats[name] = s
		} else {
			fmt.Scan(&p)
			s.count++
			if p < s.price {
				s.price = p
			}
		}
	}
	name = ""
	var maxCount, minPrice int
	for n, s := range stats {
		if name == "" || s.count > maxCount || (s.count == maxCount && s.price < minPrice) {
			name = n
			minPrice = s.price
			maxCount = s.count
		}
	}
	fmt.Println(name)
}
