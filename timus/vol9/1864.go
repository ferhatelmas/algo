package main

import "fmt"

func main() {
	var n int
	var mid, s float64
	fmt.Scan(&n)
	ns := make([]float64, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&ns[i])
		mid += ns[i]
	}
	mid /= float64(n + 1)
	for i := 0; i < n; i++ {
		ns[i] -= mid
	}
	for _, i := range ns {
		if i > 0 {
			s += i
		}
	}
	for _, i := range ns {
		if i > 0 {
			fmt.Printf("%d ", int(float64(i)*100/float64(s)+0.000001))
		} else {
			fmt.Print("0 ")
		}
	}
}
