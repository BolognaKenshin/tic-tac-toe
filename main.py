from game_manager import GameManager
import art

gm = GameManager()
gm.greet_player(art.logo[0])

keep_playing = True

while keep_playing:
      game_ongoing = True
      gm.row_1 = ["-", "-", "-"]
      gm.row_2 = ["-", "-", "-"]
      gm.row_3 = ["-", "-", "-"]
      gm.game_setup()
      while game_ongoing:
            gm.turn_ongoing = True
            while gm.turn_ongoing:
                  row, col, mark = gm.player_turn()
                  gm.update_board(row, col, mark)

            game_board = [f'''   
               a     b     c
                  |     |
            1  {gm.row_1[0]}  |  {gm.row_1[1]}  |  {gm.row_1[2]}
             _____|_____|_____
                  |     |
            2  {gm.row_2[0]}  |  {gm.row_2[1]}  |  {gm.row_2[2]}
             _____|_____|_____
                  |     |
            3  {gm.row_3[0]}  |  {gm.row_3[1]}  |  {gm.row_3[2]}
                  |     |    
            ''', ]

            print(game_board[0])
            is_winner = gm.check_for_winner(mark)
            if is_winner:
                  gm.keep_score(gm.current_turn, art.winner[0])
                  game_ongoing = False

            if gm.current_turn == 1:
                  gm.current_turn = 2
            else:
                  gm.current_turn = 1

      play_again = input('Would you like to play again? (Yes/No): ').lower()

      if play_again == "no":
            keep_playing = False
            print("Come play again soon!")



