from tkinter import *
import random


def next_turn(p, q):
    global player
    if buttons[p][q]['text'] == "" and check_winner() is False:
        if player == players[0]:
            buttons[p][q]['text'] = player
            if check_winner() is False:
                player = players[1]
                turn_label.config(text=(players[1]) + " turn")

            elif check_winner() is True:
                turn_label.config(text=(players[0]) + " wins")

            elif check_winner() == 'Tie':
                turn_label.config(text='Tie!')

        else:
            buttons[p][q]['text'] = player
            if check_winner() is False:
                player = players[0]
                turn_label.config(text=(players[0]) + " turn")

            elif check_winner() is True:
                turn_label.config(text=(players[1]) + " wins")

            elif check_winner() == 'Tie':
                turn_label.config(text='Tie!')


def check_winner():
    for r in range(3):
        if buttons[r][0]['text'] == buttons[r][1]['text'] == buttons[r][2]['text'] != "":
            buttons[r][0].config(bg="green")
            buttons[r][1].config(bg="green")
            buttons[r][2].config(bg="green")
            return True

    for c in range(3):
        if buttons[0][c]['text'] == buttons[1][c]['text'] == buttons[2][c]['text'] != "":
            buttons[0][c].config(bg="green")
            buttons[1][c].config(bg="green")
            buttons[2][c].config(bg="green")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True

    elif empty_spaces() is False:
        for r in range(3):
            for c in range(3):
                buttons[r][c].config(bg="yellow")
        return "Tie"

    else:
        return False


def new_game():
    global player
    player = random.choice(players)
    turn_label.config(text=player + " turn")
    for r in range(3):
        for c in range(3):
            buttons[r][c].config(text="", bg="#f0f0f0")


def empty_spaces():
    spaces = 9
    for r in range(3):
        for c in range(3):
            if buttons[r][c]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False

    else:
        return True


window = Tk()
window.title("Tic-Tac-Toe")

players = ["X", "O"]
player = random.choice(players)

buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

turn_label = Label(window, text=player + " turn", font=('consolas', 30))
turn_label.pack(side=TOP)

restart_button = Button(window, text="Restart", font=('consolas', 20), command=new_game)
restart_button.pack(side=TOP)

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('consolas', 20), width=5, height=2,
                                      command=lambda x=row, y=column: next_turn(x, y))

        buttons[row][column].grid(row=row, column=column)


window.mainloop()
