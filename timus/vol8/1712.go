package main

import "fmt"

func read() [][]rune {
	var res [][]rune
	var s string
	for i := 0; i < 4; i++ {
		fmt.Scan(&s)
		res = append(res, []rune(s))
	}
	return res
}

func main() {
	x, m := read(), read()
	x2 := make([][]rune, 4, 4)

	var res []rune
	for i := 0; i < 4; i++ {
		x2[i] = make([]rune, 4, 4)
		copy(x2[i], x[i])
	}
	for k := 0; k < 4; k++ {
		for i := 0; i < 4; i++ {
			for j := 0; j < 4; j++ {
				if x[i][j] == 'X' {
					res = append(res, m[i][j])
				}
			}
		}
		for i := 0; i < 4; i++ {
			for j := 0; j < 4; j++ {
				x2[j][3-i] = x[i][j]
			}
		}

		for i := 0; i < 4; i++ {
			for j := 0; j < 4; j++ {
				x[i][j] = x2[i][j]
			}
		}
	}

	fmt.Println(string(res))
}
