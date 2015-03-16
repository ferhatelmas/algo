package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"unicode"
)

func isSeparator(c rune) bool {
	return c == '?' || c == '!' || c == '.'
}

func main() {
	b, r := false, bufio.NewScanner(os.Stdin)
	r.Split(bufio.ScanRunes)
	for r.Scan() {
		s := r.Text()
		if !unicode.IsLetter(rune(s[0])) {
			fmt.Printf("%c", s[0])
		}

		if isSeparator(rune(s[0])) {
			b = false
		}

		if unicode.IsLetter(rune(s[0])) {
			if !b {
				b = true
				s = strings.ToUpper(s)
			} else {
				s = strings.ToLower(s)
			}
			fmt.Print(s)
		}
	}
}
