package main

import "fmt"


func square(number int) int {
	return number * number
}


func solve(
	size int,
) (
	answer int,
) {
	if size == 1 {
		answer = 1
		return
	} else {
		answer =
			4*square(2*size - 1) -
			12*(size - 1) +
			solve(size - 1)
		return
	}
}

func main() {
	fmt.Println(solve(501))
}

