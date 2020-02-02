// Package basics implements basic contents.package basics.
package basics

import "fmt"

func adder() func(int) int {
	sum := 0
	return func(x int) int {
		sum += x
		return sum
	}
}

func Example_adder() {
	pos, neg := adder(), adder()
	for i := 0; i < 10; i++ {
		fmt.Println(
			i, ":",
			pos(i),
			neg(-2*i),
		)
	}
	// Output:
	// 0 : 0 0
	// 1 : 1 -2
	// 2 : 3 -6
	// 3 : 6 -12
	// 4 : 10 -20
	// 5 : 15 -30
	// 6 : 21 -42
	// 7 : 28 -56
	// 8 : 36 -72
	// 9 : 45 -90
}
