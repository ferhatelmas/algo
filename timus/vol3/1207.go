package main

import (
	"fmt"
	"sort"
)

type point struct {
	id   int
	x, y int64
}

type points []point

func (ps points) Len() int      { return len(ps) }
func (ps points) Swap(i, j int) { ps[i], ps[j] = ps[j], ps[i] }

type extPoints struct {
	points
	pivot point
}

func (ps extPoints) Less(i, j int) bool {
	a, b := ps.points[i], ps.points[j]
	return (a.x-ps.pivot.x)*(b.y-ps.pivot.y)-(b.x-ps.pivot.x)*(a.y-ps.pivot.y) > 0
}

func median(ps []point) {
	for i, p := range ps {
		if p.y < ps[0].y || (p.y == ps[0].y && p.x < ps[0].x) {
			ps[0], ps[i] = p, ps[0]
		}
	}
	sort.Sort(extPoints{points: ps[1:], pivot: ps[0]})
}

func main() {
	var n int
	fmt.Scan(&n)
	ps := make([]point, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&ps[i].x)
		fmt.Scan(&ps[i].y)
		ps[i].id = i + 1
	}
	median(ps)
	fmt.Printf("%d %d\n", ps[0].id, ps[n/2].id)
}
