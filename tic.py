from guizero import App, Box, PushButton, Text



# Bàn cờ dưới dạng danh sách 1D
board = [" " for _ in range(9)]

# Hàm kiểm tra người chiến thắng
def check_winner():
    win_patterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Hàng ngang
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Cột dọc
        [0, 4, 8], [2, 4, 6]              # Đường chéo
    ]

    for pattern in win_patterns:
        if board[pattern[0]] == board[pattern[1]] == board[pattern[2]] != " ":
            return board[pattern[0]]  # Trả về người thắng ("X" hoặc "O")

    if " " not in board:  # Kiểm tra hòa
        return "draw"

    return None  # Chưa ai thắng


# Biến toàn cục
current_player = "X"

# Cập nhật hàm `make_move` để kiểm tra chiến thắng
def make_move(button, index):
    global current_player

    if button.text == " ":
        button.text = current_player
        board[index] = current_player  # Cập nhật bàn cờ
        print(board[index])
        winner = check_winner()  # Kiểm tra kết quả

        if winner:
            if winner == "draw":
                status.value = "Hòa!"
            else:
                status.value = f"Người chơi {winner} thắng!"
        else:
            current_player = "O" if current_player == "X" else "X"
            status.value = f"Đến lượt người chơi {current_player}"

# Tạo ứng dụng chính
app = App("Tic Tac Toe", width=300, height=350)

# Thêm ô trạng thái để hiển thị lượt chơi
status = Text(app, text="Đến lượt người chơi X", size=14)

# Tạo hộp chứa các nút bấm
board_box = Box(app, layout="grid")

# Lưu danh sách các nút
buttons = []
for i in range(9):
    button = PushButton(board_box, text=" ", grid=[i % 3, i // 3], width=6, height=3)
    button.update_command(make_move, args=[button, i])
    buttons.append(button)  # Thêm nút vào danh sách



# Hàm khởi động lại
def restart():
    global board, current_player
    board = [" " for _ in range(9)]  # Làm trống bàn cờ
    current_player = "X"
    status.value = "Đến lượt người chơi X"
    for button in buttons:
        button.text = " "

# Thêm nút khởi động lại vào giao diện
restart_button = PushButton(app, text="Khởi động lại", command=restart)



# Chạy ứng dụng
app.display()
