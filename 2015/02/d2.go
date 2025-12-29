package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	total_wrapping_paper := 0
	total_ribbon := 0
	data, err := os.ReadFile("input.txt")

	if err != nil {
		panic(err)
	}

	lines := strings.Split(string(data), "\n")
	for _, line := range lines {
		dims := strings.Split(line, "x")

		l, _ := strconv.Atoi(dims[0])
		w, _ := strconv.Atoi(dims[1])
		h, _ := strconv.Atoi(dims[2])

		side1 := 2 * l * w
		side2 := 2 * w * h
		side3 := 2 * h * l

		wrapping_paper := side1 + side2 + side3 + (min(side1, side2, side3) / 2)
		total_wrapping_paper += wrapping_paper

		ribbon := (l * w * h) + (2 * (l + w + h - max(l, w, h)))
		total_ribbon += ribbon
	}

	fmt.Println("Part A:", total_wrapping_paper)
	fmt.Println("Part B:", total_ribbon)
}
