# AdventOfCode
My non-AI solutions to [Advent of Code](https://adventofcode.com) problems, sorted by year and day.

## Progress

| Year | Days solved | Stars | Languages | Notes |
|------|-------------|-------|-----------|-------|
| 2015 | 1–11 | 22 | Python, Go, C# | Days 1–4 also done in Go, day 1 in C# |
| 2016 | 1–15 | 30 | Python | In progress |
| 2017 | 1–20, 22–25 | 46 | Python | Day 21 and part 2 of day 23 unsolved |
| 2018–2023 | – | – | – | Not started yet |
| 2024 | 1–18 | 34 | Python | Part 2 of days 16 and 17 incomplete |
| 2025 | 1–12 | 24 ⭐ | Python | Complete! (2025 had 12 days) |

## Layout

```
YYYY/
  DD/
    dNa.py   # part 1
    dNb.py   # part 2
```

A few days have extra files:

- `dN.go`: a Go solution covering both parts (2015 days 1–4)
- `helpers.py`, `knot_hash.py`, etc.: code shared between the two parts
- `*_alt.py`: an alternative approach to the same part
- `*_incomplete.py`: an attempt that doesn't produce the right answer (yet)

## Running a solution

Puzzle inputs are **not** included in this repo. They're copyrighted by Eric Wastl, so `*.txt` is gitignored. To run a solution, log in to Advent of Code, download your own input, and save it in that day's folder.

Most scripts open their input using a path relative to the repo root (e.g. `2017/07/input_a.txt`), so run them from the root:

```sh
python3 2017/07/d7a.py
```

2024 days 1–15 and the Go solutions use a bare filename (e.g. `input_a.txt`), so run those from inside the day's folder instead. Check the `open(...)` call at the top of each script for the exact filename it expects. Common ones are `input.txt`, `input_a.txt` and `input_sample.txt`.

## About

When I first got into AoC in 2024, I had been out of pure CS for more than a decade. It rekindled a love for programming in me, and I hastily tried to find solutions to the problems in the early mornings and late evenings, i.e., before and after work. As such, the code is a bit messy. However, I took pride in not leveraging AI/LLM help for the solutions and instead would go back to Wikipedia or an algorithms textbook to try and find a solution. Usually, I just needed to rummage around in my head for an algorithm I learnt about in university in the mid 2000s. :) 

Addendum to the above: recently, I have made use of LLMs to bounce ideas off of and ask for hints if I get stuck. I can learn new techniques and this does not equate to simply chucking the entire problem into Claude to solve. Also, Claude keeps the README up to date.