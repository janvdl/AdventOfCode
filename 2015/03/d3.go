package main

import (
	"fmt"
	"os"
)

type coord struct {
	x int
	y int
}

func main() {
	// read input
	data, err := os.ReadFile("input.txt")
	if err != nil {
		panic(err)
	}

	// part A
	a := part_a(data)
	fmt.Println("Part A:", a)

	// part B
	b := part_b(data)
	fmt.Println("Part B:", b)
}

func part_a(data []byte) int {
	// dictionary to keep track of points
	var houses = make(map[coord]int)
	houses[coord{x: 0, y: 0}] = 1

	// keep track of current position
	var x, y int = 0, 0

	// evaluate all lines and increment counts per coord
	for _, c := range data {
		switch c {
		case '^':
			y--
		case 'v':
			y++
		case '<':
			x--
		case '>':
			x++
		}

		// make point at santa's current position
		point := coord{x: x, y: y}

		// set/increment value for house at point
		_, ok := houses[point]
		if ok {
			houses[point] += 1
		} else {
			houses[point] = 1
		}
	}

	// get total number of houses with at least one present
	var result_a int = 0
	for range houses {
		result_a += 1
	}

	return result_a
}

func part_b(data []byte) int {
	// dictionary to keep track of points
	var houses = make(map[coord]int)
	houses[coord{x: 0, y: 0}] = 1

	// keep track of current position
	var sx, sy, rx, ry int = 0, 0, 0, 0

	// keep track of santa vs robo-santa
	var is_santa bool = true

	// evaluate all lines and increment counts per coord
	for _, c := range data {
		switch c {
		case '^':
			if is_santa {
				sy--
			} else {
				ry--
			}
		case 'v':
			if is_santa {
				sy++
			} else {
				ry++
			}
		case '<':
			if is_santa {
				sx--
			} else {
				rx--
			}
		case '>':
			if is_santa {
				sx++
			} else {
				rx++
			}
		}

		// make point for either santa or robo-santa
		point := coord{x: 0, y: 0}
		if is_santa {
			point.x, point.y = sx, sy
		} else {
			point.x, point.y = rx, ry
		}

		// set/increment value for house at point
		_, ok := houses[point]
		if ok {
			houses[point] += 1
		} else {
			houses[point] = 1
		}

		// toggle from santa to robo-santa and vice versa
		is_santa = !is_santa
	}

	// get total number of houses with at least one present
	var result_b int = 0
	for range houses {
		result_b += 1
	}

	return result_b
}
