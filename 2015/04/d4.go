package main

import (
	"crypto/md5"
	"encoding/hex"
	"fmt"
	"strconv"
	"strings"
)

func main() {
	// input data
	data := "your_input_here"

	// Part A
	part_a_result := solver(data, 0, "00000")
	fmt.Println("Part A:", part_a_result)

	// Part B
	part_b_result := solver(data, part_a_result, "000000")
	fmt.Println("Part B:", part_b_result)
}

func solver(data string, start int, goal string) int {
	solved := false
	i := start // Part B can start where Part A left off

	for !solved {
		tmp_data := []byte(data + strconv.Itoa(i))
		tmp_md5 := md5.Sum(tmp_data)
		tmp_md5_str := hex.EncodeToString(tmp_md5[:])

		if strings.HasPrefix(tmp_md5_str, goal) {
			solved = true // redundant, I know
			return i
		}

		i++
	}

	return 0
}
