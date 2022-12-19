class TicTacToe:
  def __init__(self, n):
    self.rows = [0]*n
    self.cols = [0]*n
    self.d = 0
    self.a_d = 0
    self.n = n
    
    

  def move(self, row, col, player):
    # check for winner
    # row_placed has n in a row 
    # col_placed has n in a row
    # diag, anti_diag 
      # a diag, 0,2  1,1, 2,0
    # player 1, = +n, player2 = -n
    # return 0 if no winner
    val_add = 1
    if player == 2:
      val_add = -1
    
    self.rows[row] += val_add
    self.cols[col] +=val_add
    if row == col:
      self.d += val_add
    if row + col == len(self.rows) -1:
      self.a_d += val_add

    if self.rows[row] == self.n or self.cols[col] == self.n or self.d == self.n or self.a_d == self.n:
      return 1
    if self.rows[row] == -self.n or self.cols[col] == -self.n or self.d == -self.n or self.a_d == -self.n:
      return 2
    print(self.rows, self.cols, self.d, self.a_d)
    return 0

g = TicTacToe(3)
print(g.rows, g.cols)
print(g.move(0,0,1))
print(g.move(0,2,2))
print(g.move(2,2,1))
print(g.move(1,1,2))
print(g.move(2,0,1))
print(g.move(1,0,2))
print(g.move(2,1,1))