EMPTY_CELL = '.'
board_size = input("Enter board size: ")
game_board = [[EMPTY_CELL for i in range(int(board_size))] for j in range(int(board_size))]
print(game_board)
print()

game_board = [[[j, i] for i in range(int(board_size))] for j in range(int(board_size))]
print(game_board)
print()

game_board = [[str(j)+str(i) for i in range(int(board_size))] for j in range(int(board_size))]
print(game_board)
print()
single_row = ["*" for i in range(int(board_size))]
all_rows = [single_row for i in range(int(board_size))]
print(all_rows)