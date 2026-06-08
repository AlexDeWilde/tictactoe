cell1 = "1"
cell2 = "2"
cell3 = "3"
# ...
cell1 = 2
#  2  => "X"
# lookup(0,1,2;" ","O","X")
# Cell1 = "X"
# cell3 = "X"
# if cell1,4,7 = same then cell1 == cell4 and (cell4 == cell7) true - pl2 wins
# if 
# X | 2 | X
# ------------
# 4 | O | 6 
# ------------
# X | 8 | O 
# Player 2 "X" position input > 3
# 
# def vars 1 to 9 as spaces  DONE
# set vars to zero  DONE
# player 1 chooses X or O  DONE
# start loop 
#   print board  DONE
#   input request player1  DONE
#   print board  DONE
#   check for tie/win, break end loop  TESTING
#   input request player2   DONE
#   print board  DONE
#   check for tie/win,        TESTING
# end loop
# loop back mandatory (will only end if tie or win triggers loop interruption)
