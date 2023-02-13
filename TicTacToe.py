import random
import time
class human:
    def __init__(self):
        pass
    def get_move(self, choices):
        print("YOUR CHOICES ARE ", choices)
        i = -1
        while True:
             i = int(input("Enter Position: "))
             if(i in choices):
                 return i
             else:
                 print("Incorrect Value Enter Again")
class random_opt:
    def __init__(self) -> None:
        pass
    def get_move(self,choices):
        return random.choice(choices)
class TicTacToe:
    def __init__(self):
        self. mat = [' ' for i in range(9)]
        self . curr_win = None
    def show_mat(self):
        for i in range(0, 9,3):
            print('| ', end = '')
            for j in range(3):
                print(self.mat[j+i], end = ' | ')
            print()
    def available(self):
        ans = [i for i in range(9) if self.mat[i] == ' ']
        return ans
    def make_move(self, i, letter):
        self.mat[i] = letter
        print(f"Value Entered By {letter} at {i}")
    def chk_winner(self, letter):
        ans = False
        if(self.mat[0:3] == [letter,letter,letter] or self.mat[3:6] == [letter,letter,letter]):
            ans = True
        elif (self.mat[6:9] == [letter,letter,letter]):
            ans = True
        elif(self.mat[0]== self.mat[3] == self.mat[6] == letter):
            ans = True
        elif(self.mat[1]== self.mat[4] == self.mat[7] == letter):
            ans = True
        elif(self.mat[2]== self.mat[5] == self.mat[8] == letter):
            ans = True
        elif(self.mat[0]== self.mat[4] == self.mat[8] == letter):
            ans = True
        elif(self.mat[2]== self.mat[4] == self.mat[6] == letter):
            ans = True
        if(ans):
            print(f"{letter} WON !!!!!!!!")
        return ans
            
    
    def play(self, x_player, y_player, letter):
        while not self.curr_win:
            choices = self.available()
            if(not choices):
                print("MATCH DRAWN !!!!")
                break
            i = -1
            if(letter == 'X'):
                i = x_player.get_move(choices)
                self.make_move(i, letter)
            else:
                i = y_player.get_move(choices)
                self.make_move(i,letter)
            self.show_mat()
            if(self.chk_winner(letter)):
                break
            time.sleep(0.8)
            letter = "X" if letter == "O" else "O"
if(__name__ == "__main__"):
    t = TicTacToe()
    x = human()
    y =random_opt()
    t.show_mat()
    t.play(x, y, "X")

            
        
        
    
    
    