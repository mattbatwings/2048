import random
import tkinter as tk
from tkinter import messagebox

class Board:
    def __init__(self, board_size=4):
        self.size = board_size
        self.board = [[0] * self.size for _ in range(self.size)]

    def set_board(self, board): self.board = board
    def print_board(self):
        for x in self.board: print(" ".join(map(str, x)))
        print()

    def gen_2(self):
        r, c = random.randint(0, self.size-1), random.randint(0, self.size-1)
        while self.board[r][c] != 0:
            r, c = random.randint(0, self.size-1), random.randint(0, self.size-1)
        self.board[r][c] = 2

    def rotate_90(self):
        for x in range(0, int(self.size / 2)):
            for y in range(x, self.size - x - 1):
                temp = self.board[x][y]
                self.board[x][y] = self.board[y][self.size - 1 - x]
                self.board[y][self.size - 1 - x] = self.board[self.size - 1 - x][self.size - 1 - y]
                self.board[self.size - 1 - x][self.size - 1 - y] = self.board[self.size - 1 - y][x]
                self.board[self.size - 1 - y][x] = temp

    def rotate_board(self, num_rotations):
        for i in range(num_rotations): self.rotate_90()

    def compress(self):
        for i in range(self.size):
            pos = 0
            new_row = [0] * self.size
            for j in range(self.size):
                if self.board[i][j] != 0:
                    new_row[pos] = self.board[i][j]
                    pos += 1
            self.board[i] = new_row

    def merge_left(self):
        for i in range(self.size):
            for j in range(self.size - 1):
                if self.board[i][j] == self.board[i][j + 1] and self.board[i][j] != 0:
                    self.board[i][j] *= 2
                    self.board[i][j + 1] = 0

    def move_left(self):
        self.compress(); self.merge_left(); self.compress()

    def move_up(self): self.rotate_board(1); self.move_left(); self.rotate_board(3)
    def move_right(self): self.rotate_board(2); self.move_left(); self.rotate_board(2)
    def move_down(self): self.rotate_board(3); self.move_left(); self.rotate_board(1)

    def full(self):
        return all(all(cell != 0 for cell in row) for row in self.board)

    def win(self):
        return any(2048 in row for row in self.board)

class GameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("2048 - Mattbatwings Edition")
        self.colors = {
            0: "#cdc1b4", 2: "#eee4da", 4: "#ede0c8", 8: "#f2b179",
            16: "#f59563", 32: "#f67c5f", 64: "#f65e3b", 128: "#edcf72",
            256: "#edcc61", 512: "#edc850", 1024: "#edc53f", 2048: "#edc22e"
        }
        self.setup_ui()
        self.restart_game()
        for key in ['<Up>', '<Left>', '<Down>', '<Right>', '<w>', '<a>', '<s>', '<d>']:
            self.root.bind(key, self.handle_input)

    def setup_ui(self):
        header_frame = tk.Frame(self.root, padx=10, pady=10)
        header_frame.pack()
        tk.Label(header_frame, text="2048", font=("Helvetica", 24, "bold")).pack(side=tk.LEFT, padx=10)
        tk.Button(header_frame, text="Reset", font=("Helvetica", 12, "bold"), bg="#8f7a66", fg="#f9f6f2", command=self.restart_game).pack(side=tk.RIGHT, padx=10)
        self.grid_frame = tk.Frame(self.root, bg="#bbada0", bd=5)
        self.grid_frame.pack(padx=10, pady=10)
        self.cells = []
        for r in range(4):
            row_cells = []
            for c in range(4):
                cell_label = tk.Label(self.grid_frame, text="", font=("Helvetica", 22, "bold"), width=4, height=2, bg="#cdc1b4", fg="#776e65")
                cell_label.grid(row=r, column=c, padx=5, pady=5)
                row_cells.append(cell_label)
            self.cells.append(row_cells)

    def restart_game(self):
        self.board = Board()
        self.board.gen_2(); self.board.gen_2()
        self.update_ui()

    def handle_input(self, event):
        key = event.keysym.lower()
        prev = [row[:] for row in self.board.board]
        if key in ['w', 'up']: self.board.move_up()
        elif key in ['a', 'left']: self.board.move_left()
        elif key in ['s', 'down']: self.board.move_down()
        elif key in ['d', 'right']: self.board.move_right()
        else: return
        self.update_ui()
        if self.board.win():
            messagebox.showinfo("Victory!", "You win!"); self.restart_game()
            return
        if prev != self.board.board:
            if not self.board.full(): self.board.gen_2(); self.update_ui()
        if self.board.full() and not self.has_valid_moves():
            messagebox.showwarning("Game Over", "No moves left!"); self.restart_game()

    def has_valid_moves(self):
        b = self.board.board
        for r in range(4):
            for c in range(4):
                if (r < 3 and b[r][c] == b[r+1][c]) or (c < 3 and b[r][c] == b[r][c+1]): return True
        return False

    def update_ui(self):
        for r in range(4):
            for c in range(4):
                val = self.board.board[r][c]
                self.cells[r][c].config(text=str(val) if val > 0 else "", bg=self.colors.get(val, "#3c3a32"), fg="#776e65" if val <= 4 else "#f9f6f2")

if __name__ == '__main__':
    root = tk.Tk(); app = GameGUI(root); root.mainloop()
