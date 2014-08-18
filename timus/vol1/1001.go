package main
import (
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
	"io/ioutil"
)

func main() {
	text, _ := ioutil.ReadAll(os.Stdin)
	a := strings.Fields(string(text))
	for i := len(a)-1; i > -1; i-- {
		j, _ := strconv.ParseFloat(a[i], 64)
		fmt.Printf("%.4f\n", math.Sqrt(j))
	}
}
