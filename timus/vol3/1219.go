package main

import (
	"bufio"
	"fmt"
	"math/rand"
	"os"
)

func main() {
	out := bufio.NewWriter(os.Stdout)
	for i := 0; i < 1000000; i++ {
		fmt.Fprintf(out, "%c", rand.Intn(26)+'a')
	}
	out.Flush()
}
