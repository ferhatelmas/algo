package main

import (
	"bufio"
	"bytes"
	"fmt"
	"os"
	"sort"
	"strconv"
)

type Team struct {
	id string
	score int
	index int
}
type Teams []Team

func main() {
	s := bufio.NewScanner(os.Stdin)
	s.Split(bufio.SplitFunc(bufio.ScanWords))
	s.Scan(); s.Text()
	n, _ := strconv.Atoi(s.Text())
	ns := make([]Team, n)
	for i := 0; i < n; i++ {
		s.Scan()
		id := s.Text()
		s.Scan()
		score, _ := strconv.Atoi(s.Text())
		ns[i] = Team{id, score, i}
	}

	sort.Sort(sort.Reverse(Teams(ns)))
	var b bytes.Buffer
	for _, v := range ns {
		b.WriteString(fmt.Sprintf("%s %d\n", v.id, v.score))
	}
	b.WriteTo(os.Stdout)
}

func (ts Teams) Len() int { return len(ts) }
func (ts Teams) Swap(i, j int) { ts[i], ts[j] = ts[j], ts[i] }
func (ts Teams) Less(i, j int) bool {
	s := ts[i].score - ts[j].score
	if s < 0 {
		return true
	} else if s > 0 {
		return false
	} else {
		return ts[i].index - ts[j].index > 0
	}
}
