package main

import "fmt"

func main() {
	var s string
	fmt.Scan(&s)
	r := make([]uint8, len(s))
	for i := range s {
		if i == 0 {
			r = append(r, (26+s[i]-102)%26+97)
		} else {
			r = append(r, (26+s[i]-s[i-1])%26+97)
		}
	}
	fmt.Println(string(r))
}
