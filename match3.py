board = [
    ["A", "A", "A", "D"],
    ["C", "D", "B", "C"],
    ["B", "C", "D", "A"],
    ["D", "A", "B", "C"]
]

for row in board:
    for piece in row:
        print(piece, end=" ")
    print()
row = board[0]
print(row)
if row[0] == row[1] == row[2]:
    print("Match found!")
for i in range(len(row) - 2):
    if row[i] == row[i + 1] == row[i + 2]:
        print("Match found!")
