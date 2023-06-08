import tkinter as tk
import tkinter.messagebox
import random

tate = 20
yoko = 10
masu_size = 40

block_color = {
            0:"gray",
            1:"cyan",
            2: "yellow",
            3: "green",
            4: "red",
            5: "blue",
            6: "orange",
            7: "purple" 
            }


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
        self.block = None
        self.choiseMino()
        self.drawMino()


        self.root.bind('<Down>', lambda event: self.moveDown())
        self.root.bind('<Left>', lambda event: self.moveLeft())
        self.root.bind('<Right>', lambda event: self.moveRight())

        self.root.after(500, self.dropMino)


    #盤面を描画　20×10
    def board(self):
        for row in range(tate):
            for col in range(yoko):
                x1 = col * masu_size
                y1 = row * masu_size
                x2 = x1 + masu_size
                y2 = y1 + masu_size
                color = block_color[masu_data[row + 1][col + 1]]
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="white")

    #落ちてくるミノの種類を決定
    def choiseMino(self):
        mino_data = [
            [
                [0, 0, 0, 0],
                [1, 1, 1, 1],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ],
            [
                [2, 2],
                [2, 2]
            ],
            [
                [0, 3, 3],
                [3, 3, 0],
                [0, 0, 0]
            ],
            [
                [4, 4, 0],
                [0, 4, 4],
                [0, 0, 0]
            ],
            [
                [5, 0, 0],
                [5, 5, 5],
                [0, 0, 0]
            ],
            [
                [0, 0, 6],
                [6, 6, 6],
                [0, 0, 0]
            ],
            [
                [0, 7, 0],
                [7, 7, 7],
                [0, 0, 0]
            ]
        ]
        mino = random.choice(mino_data)
        self.block = mino
        
    #二次元配列にmoniの数値を代入
        for row in range(len(mino)):
            for col in range(len(mino[0])):
                if mino[row][col] != 0:
                    masu_data[row+1][col+(yoko//2)-1] = mino[row][col]

    

    #盤面の数値ごとに、ブロックの色を表示していく。または更新していく
    def drawMino(self):
        self.canvas.delete("all")
        self.board()

        for row in range(tate):
            for col in range(yoko):
                x1 = col * masu_size
                y1 = row * masu_size
                x2 = x1 + masu_size
                y2 = y1 + masu_size
                color = block_color[masu_data[row + 1][col + 1]]
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="white")

       
    #落ちる間隔を0.5秒で設定、⇩で同様に 
    def dropMino(self):
        if not self.move(0, 1):
            self.choiseMino()
        self.drawMino()
        
        self.root.after(500, self.dropMino)

    def move(self, dx, dy):
        new_block = [[0 for _ in range(yoko + 2)] for _ in range(tate + 2)]
        for row in range(tate, 0, -1):
            for col in range(1, yoko + 1):
                if masu_data[row][col] != 0:
                    if (
                        new_block[row + dy][col + dx] != 0
                        or new_block[row + dy][col + dx] == 9
                        or col + dx < 1 
                        or col + dx > yoko
                        or masu_data[row + 1][col] == 9
                    ):
                        if dy == 1:
                            self.choiseMino()
                        return False
                    new_block[row + dy][col + dx] = masu_data[row][col]

        for row in range(tate, 0, -1):
            for col in range(1, yoko + 1):
                new_block[row + dy][col + dx] = masu_data[row][col]

        for row in range(1, tate + 2):
            for col in range(1, yoko + 1):
                masu_data[row][col] = new_block[row][col]

        return True

    #下で停止


    #左右に移動できるようにする
    def moveDown(self):
        self.move(0, 1)
        self.drawMino()

    def moveLeft(self):
        self.move(-1, 0)
        self.drawMino()

    def moveRight(self):
        self.move(1, 0)
        self.drawMino()

    #回転させる 

    


    #横がそろったら一列削除













root = tk.Tk()
root.title('Tetris')
tetris = Tetris(root)
root.mainloop()
