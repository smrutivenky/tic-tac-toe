class TicTacToe:
    class STATES():
        CROSS_TURN = 0
        NAUGHT_TURN = 0
        DRAW = 0
        CROSS_WON = 0
        NAUGHT_WON = 0

    def __init__(self):
        self.board = [['_' for _ in range(3)]for _ in range(3)]
        self.PLAY = True

    def display(self):
        for row in self.board:
            print(row)
    def start(self):
        move_x = True
        while(self.PLAY):
            if move_x:
                symbol = 'x'
            else:
                symbol = 'o'
            print("Its your turn "+symbol)
            self.display()
            print("Please enter a value between 0 and 2")
            row = input()
            print("Please enter a value between 0 and 2")
            column = input()
            if self.place_marker(symbol, row, column) is False:
                print("Invalid move please enter the values again.")
                continue
            move_x = not move_x
            winner = self.winner_checker(symbol)
            if winner:
                self.display()
                print(winner)
                self.reset()
                print("press R to play again and another key to Quit")
                ip = input().lower()
                if ip == 'r':
                    self.PLAY = True
                else:
                    self.PLAY = False

    def winner_checker(self, symbol):
        if self.STATES.CROSS_TURN >=3 or self.STATES.NAUGHT_TURN  >=3:
            if(self.game_checker(symbol)):
                if symbol == 'x':
                    self.STATES.CROSS_WON +=1
                else:
                    self.STATES.NAUGHT_WON +=1
                return("Game won by " + symbol)
            elif(self.STATES.CROSS_TURN+self.STATES.NAUGHT_TURN == 9):
                self.STATES.DRAW +=1
                return("Game is a draw")
        return None

    def reset(self):
        self.board = [["_" for _ in range(3)]for _ in range(3)]
        self.STATES.CROSS_TURN = 0
        self.STATES.NAUGHT_TURN = 0

    def place_marker(self, symbol, row, column):
        try:
            row = int(row)
            column = int(column)
        except:
            return False
        if self.valid_move(symbol, row, column) == False:
            return False
        self.board[row][column] = symbol
        if symbol == 'x':
            self.STATES.CROSS_TURN+=1
        else:
            self.STATES.NAUGHT_TURN+=1
        return True

    def game_checker(self, symbol):
        # row CHECK
        for row in range(3):
            win = True
            for col in range(3):
                if self.board[row][col]!=symbol:
                    win = False
                    continue
            if win:
                return win
        # col check
        for col in range(3):
            win = True
            for row in range(3):
                if self.board[row][col]!=symbol:
                    win = False
                    continue
            if win:
                return win
        # diagonal check
        win = True
        for x in range(3):
            if self.board[x][x]!=symbol:
                win = False
                continue
        if win:
            return win

        # diagonal check
        win = True
        for x in range(3):
            if self.board[x][len(self.board)-x-1]!=symbol:
                win = False
                continue
        if win:
            return win

        return win

    def valid_move(self, symbol, row, col):
        if(row < 0 or row > 2) or (col < 0 or col > 2):
            return False
        if self.board[row][col] != '_':
            return False
        return True

if __name__ == "__main__":
    t = TicTacToe()
    t.start()
