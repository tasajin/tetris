import tkinter as tk
import tkinter.messagebox
import random

tate = 20
yoko = 10
masu_size = 40


# 2次元リスト　盤面は0　壁は9
masu_data = [[0 for i in range(yoko + 2)] for j in range(tate + 2)]
for i in range(tate + 1):
    masu_data[i][0] = 9
    masu_data[i][yoko + 1] = 9
    masu_data[tate + 1] = [9 for i in range(yoko + 2)]


class Tetris():
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(self.root, width=yoko * masu_size, height=tate * masu_size, bg="gray")
        self.canvas.pack()
        self.board()

        self.createMino()


    #盤面を描画　20×10
    def board(self):
        for row in range(tate):
            for col in range(yoko):
                x1 = col * masu_size
                y1 = row * masu_size
                x2 = x1 + masu_size
                y2 = y1 + masu_size
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="white")


    #落ちてくるミノの種類を決定
    def choiseMino(self):
        mino_data = [
            # I
            [
                [0, 0, 0, 0],
                [1, 1, 1, 1],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ],
            # O
            [
                [2, 2],
                [2, 2]
            ],
            # S
            [
                [0, 3, 3],
                [3, 3, 0],
                [0, 0, 0]
            ],
            # Z
            [
                [4, 4, 0],
                [0, 4, 4],
                [0, 0, 0]
            ],
            # J
            [
                [5, 0, 0],
                [5, 5, 5],
                [0, 0, 0]
            ],
            # L
            [
                [0, 0, 6],
                [6, 6, 6],
                [0, 0, 0]
            ],
            # T
            [
                [0, 7, 0],
                [7, 7, 7],
                [0, 0, 0]
            ]
        ]
        mino = random.choice(mino_data)
        self.current_block = mino
        
    #二次元配列にそれぞれの数値を打ち込む
    def createMino():
        for row in range(len(mino)):
        for col in range(len(mino[0])):
            if mino[row][col] != 0:
                masu_data[row+1][col+(yoko//2)-1] = mino[row][col]

    

    #盤面の数値ごとに、ブロックの色を表示していく。または更新していく




        
            
    #落ちる間隔を0.5秒で設定、⇩で同様に 


    #左右に移動できるようにする


    #回転させる 


    #下で止まったら、停止


    #横がそろったら一列削除



    #強制落下










root = tk.Tk()
root.title('Tetris')
tetris = Tetris(root)
root.mainloop()
