package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	var n int
	s := bufio.NewScanner(os.Stdin)
	var first bool
	var rows [][]int
	for s.Scan() {
		if !first {
			n, _ = strconv.Atoi(s.Text())
			first = true
			continue
		}
		var row []int
		for _, t := range strings.Split(s.Text(), " ") {
			k, _ := strconv.Atoi(t)
			row = append(row, k)
		}
		rows = append(rows, row)
	}
	sums := make([][]int, n)
	for i := 0; i < n; i++ {
		sums[i] = make([]int, n+1)
	}

	for i := 0; i < n; i++ {
		for j := 1; j <= n; j++ {
			sums[i][j] = sums[i][j-1] + rows[i][j-1]
		}
	}

	var res, dp = rows[0][0], make([]int, n)

	for i := 0; i < n; i++ {
		for j := i; j < n; j++ {
			dp[0] = sums[0][j+1] - sums[0][i]
			res = max(res, dp[0])

			for k := 1; k < n; k++ {
				dp[k] = sums[k][j+1] - sums[k][i] + max(0, dp[k-1])
				res = max(res, dp[k])
			}
		}
	}

	fmt.Println(res)
}
