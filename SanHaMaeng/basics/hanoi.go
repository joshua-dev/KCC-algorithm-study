package basics

import "fmt"

// Move prints way to move disks of Hanoi tower
func Move(n, from, to, via int) {
	if n <= 0 {
		return
	}
	Move(n-1, from, via, to)
	fmt.Printf("%d -> %d\n", from, to)
	Move(n-1, via, to, from)
}

// Hanoi shows result of moving disks of Hanoi tower
func Hanoi(n int) {
	fmt.Printf("Number of disks: %d\n", n)
	Move(n, 1, 2, 3)
}
