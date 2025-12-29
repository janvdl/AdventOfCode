package main

import (
	"fmt"
	"os"
)

func main() {
	data, err := os.ReadFile("input.txt")
	if err != nil {
		panic(err)
	}

	floor := 0
	basement := false
	for idx, char := range data {
		if char == '(' {
			floor++
		} else {
			floor--
		}

		if floor == -1 && !basement {
			fmt.Println("Part B:", idx+1)
			basement = true
		}
	}

	fmt.Println("Part A:", floor)
}
