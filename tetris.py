import tkinter as tk
import tkinter.messagebox
import random

tate = 20
yoko = 10
masu_size = 40

mino = 0

#2二元リスト　盤面は０　壁は９
masu_data = [[0 for i in range(yoko +9)] for j in range(tate +9)]
for i in range(tate+1):
    masu_data[i][0],masu_data[i][yoko +1] = 9,9
    masu_data[tate +1] = [9 for i in range(yoko + 9)]

#美濃の種類ごとに、色と形を定義

class Tetris():
    def __into__(self, x=0, y=0 , color="gray"):
        self.x = x
        self.y = y
        self.color = color

#盤面を描画　20×10


#落ちてくるミノの種類を決定


#落ちる間隔を設定、⇩で同様に 


#回転させる 


#下で止まったら、停止


#横がそろったら一列削除



#下にずらす










root = tkinter.Tk()
root.title('Tetris')
Tetris(root)
root.mainloop()
