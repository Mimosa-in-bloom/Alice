from guizero import App, Box, PushButton, Text

# Biến toàn cục
current_player = "X"
app = App("Tic Tac Toe", width=300, height=350)
status = Text(app, text="Đến lượt người chơi X", size=14)
board_box = Box(app, layout="grid")
for i in range(9):
    button = PushButton(board_box, text=" ", grid=[i % 3, i // 3], width=6, height=3)
    button.update_command(make_move, args=[button, i]) 
def make_move(button, index):
    global current_player

    if button.text == " ":
        button.text = current_player
        board[index] = current_player  # Cập nhật bàn cờ
        winner = check_winner()  # Kiểm tra kết quả

        if winner:
            if winner == "draw":
                status.value = "Hòa!"
            else:
                status.value = f"Người chơi {winner} thắng!"
        else:
            current_player = "O" if current_player == "X" else "X"
            status.value = f"Đến lượt người chơi {current_player}"

 # Truyền chỉ số i



buttons = []
for i in range(9):
    button = PushButton(board_box, text=" ", grid=[i % 3, i // 3], width=6, height=3)
    button.update_command(make_move, args=[button, i])
    buttons.append(button)  # Thêm nút vào danh sách

for i in range(9):
    PushButton(board_box, text=" ", grid=[i % 3, i // 3], width=6, height=3)



app.display()
































