package main

import (
	"fmt"
	"math"
)

type node struct {
	a, b int
}

func (n node) res() float64 {
	return float64(n.a) + float64(n.b)*math.Sqrt(2)
}

func (n node) min(m node) node {
	if n.res() < m.res() {
		return n
	}
	return m
}

func (n node) add(m node) node {
	return node{n.a + m.a, n.b + m.b}
}

func main() {
	var n, m, k int
	var dp [2][1001]node
	fmt.Scan(&n)
	fmt.Scan(&m)
	fmt.Scan(&k)
	nodes := make(map[node]bool, k)
	for i := 0; i < k; i++ {
		var x node
		fmt.Scan(&x.a, &x.b)
		nodes[x] = true
	}
	for i := 0; i <= m; i++ {
		dp[0][i] = node{i, 0}
	}

	for i := 1; i <= n; i++ {
		x := i & 1
		dp[x][0] = node{i, 0}
		for j := 1; j <= m; j++ {
			dp[x][j] = node{1, 0}.add(dp[x^1][j].min(dp[x][j-1]))

			if nodes[node{i, j}] {
				dp[x][j] = dp[x][j].min(dp[x^1][j-1].add(node{0, 1}))
			}
		}
	}
	fmt.Printf("%.0f\n", 100*dp[n&1][m].res())
}
