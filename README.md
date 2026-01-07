# ˗ˏˋ ♡ ˎˊ˗ Sudoku Solver (Backtracking Algorithm) ˗ˏˋ ♡ ˎˊ˗

This project is a Python-based Sudoku solver that uses a **recursive backtracking algorithm** to fill in a 9×9 Sudoku board while respecting standard Sudoku constraints.

The program identifies empty cells, tests valid number placements, and backtracks when a placement leads to an invalid state until the puzzle is solved.

---

## 𝜗𝜚 ࣪˖ Features
- Solves standard 9×9 Sudoku puzzles
- Uses recursion and backtracking
- Validates row, column, and 3×3 subgrid constraints
- Prints both the original and solved board in a readable format

---

##  𝜗𝜚 ࣪˖ How It Works
1. The solver searches for the next empty cell (`0`) on the board.
2. It attempts to place numbers 1–9 in that position.
3. Each placement is checked for validity using Sudoku rules.
4. If a placement leads to a dead end, the algorithm backtracks and tries a new number.
5. The process repeats until the board is solved.

---

## 𝜗𝜚 ࣪˖ Tutorial Credit
This project was inspired by the following tutorial:

- *Sudoku Solver Using Backtracking*  
  https://www.youtube.com/watch?v=jM80SmTQT1k

The code has been **independently implemented, reorganized, and fully commented** to demonstrate personal understanding of the algorithm.

---

## 𝜗𝜚 ࣪˖ Author
**Aneya Ward**

- Adapted and documented independently  
- Intended for personal learning, portfolio use, and resume inclusion

---

## 𝜗𝜚 ࣪˖ Usage
Run the Python file to view the original Sudoku board and its solved output:

```bash
sudoku_solver_remastered.py
