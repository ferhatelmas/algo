package main

import "fmt"

type Stack struct {
	top  *Element
	size int
}

type Element struct {
	value interface{}
	next  *Element
}

func (s *Stack) Len() int {
	return s.size
}

func (s *Stack) Push(value interface{}) {
	s.top = &Element{value, s.top}
	s.size++
}

func (s *Stack) Pop() (value interface{}) {
	if s.size > 0 {
		value, s.top = s.top.value, s.top.next
		s.size--
		return
	}
	return nil
}

func main() {
	var r string
	fmt.Scan(&r)
	s := Stack{}
	for i := 0; i < len(r); i++ {
		if s.Len() == 0 {
			s.Push(r[i])
		} else {
			p := s.Pop()
			if p.(uint8) != r[i] {
				s.Push(p)
				s.Push(r[i])
			}
		}
	}
	res := make([]uint8, s.Len())
	for i := s.Len() - 1; i > -1; i-- {
		res[i] = s.Pop().(uint8)
	}

	fmt.Println(string(res))
}
