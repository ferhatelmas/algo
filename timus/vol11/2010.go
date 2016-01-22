package main

import "fmt"

var n, r, c int

type point struct{ x, y int }

var kingDiffs = []point{{1, 0}, {-1, 0}, {0, 1}, {0, -1}, {1, 1}, {-1, 1}, {1, -1}, {-1, -1}}
var knightDiffs = []point{{-2, 1}, {-2, -1}, {2, 1}, {2, -1}, {1, -2}, {-1, -2}, {1, 2}, {-1, 2}}

func count(diffs []point) int {
	var sum int
	for _, m := range diffs {
		if r+m.x > 0 && r+m.x <= n && c+m.y > 0 && c+m.y <= n {
			sum++
		}
	}
	return sum
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func king() int   { return count(kingDiffs) }
func knight() int { return count(knightDiffs) }
func bishop() int { return min(r-1, n-c) + min(r-1, c-1) + min(n-r, n-c) + min(n-r, c-1) }
func rook() int   { return 2 * (n - 1) }
func queen() int  { return bishop() + rook() }

func main() {
	fmt.Scan(&n)
	fmt.Scan(&r)
	fmt.Scan(&c)

	fmt.Printf("King: %d\n", king())
	fmt.Printf("Knight: %d\n", knight())
	fmt.Printf("Bishop: %d\n", bishop())
	fmt.Printf("Rook: %d\n", rook())
	fmt.Printf("Queen: %d\n", queen())
}
