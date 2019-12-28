package main

import "fmt"

func solution(a, b int) int {
	t := a % 10

	if t == 0 {
		return 10
	}
	if t == 1 || t == 5 || t == 6 {
		return t
	}
	result := 1
	for x := 0; x < b; x++ {
		result *= t
		result %= 10
	}
	return result
}

func main() {
	var T, a, b int
	fmt.Scanln(&T)
	for x := 0; x < T; x++ {
		fmt.Scanln(&a, &b)
		fmt.Println(solution(a, b))
	}
}
