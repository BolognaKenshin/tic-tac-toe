import time
import random

class GameManager:
    def __init__(self):
        self.row_1 = ["-", "-", "-"]
        self.row_2 = ["-", "-", "-"]
        self.row_3 = ["-", "-", "-"]
        self.current_turn = ""
        self.turn_ongoing = ""
        self.player_1_score = 0
        self.player_2_score = 0

    # Greets the player, explains the game
    def greet_player(self, art):
        print(art)
        print(
            "Welcome to Tic-Tac-Toe! You and and a friend will be playing against each other. First player to get three-in-a-row "
            "wins!")
        time.sleep(3)
        print('Player 1 will mark the board with "X" while Player 2 will use "O" for their own turns.')
        time.sleep(3)
        print("You'll make your moves by specifying your selected space with a letter from A-C and a number from 1-3.")
        time.sleep(3)
        print("For example: A3, B2 or C1.")
        time.sleep(3)
        input('Once you are ready to continue, please press "Enter":')

    # Determines who will go first
    def game_setup(self):
        print(f"Deciding who makes the first move...")
        time.sleep(3)
        self.current_turn = random.randint(1, 2)
        print(f"Player {self.current_turn} will go first!")
        time.sleep(3)
        print("Ready? Begin!")
        time.sleep(2)

    # The player's actual turn takes place within this function
    def player_turn(self):
        selecting_letter = True
        selecting_number = True

        while selecting_letter:
            letter = input(f"Player {self.current_turn}, choose a letter from A-C: ").lower()
            if letter != "a" and letter != "b" and letter != "c":
                print("That's not a valid selection. Try again.")
            else:
                selecting_letter = False
        while selecting_number:
            number = input(f"Now, please select a number from 1-3: ")
            if number != "1" and number != "2" and number != "3":
                print("That's not a valid selection. Try again.")
            else:
                selecting_number = False
        print(f"Player {self.current_turn} has selected {letter + number}.")
        if self.current_turn == 1:
            mark = "X"
        else:
            mark = "O"
        return number, letter, mark

    # Checks if the player's selected space is available, updates the rows filling the game board
    def update_board(self, row, col, mark):
        self.turn_ongoing = True
        if col == "a":
            col = 0
        elif col == "b":
            col = 1
        elif col == "c":
            col = 2
        if int(row) == 1:
            if self.row_1[col] == "-":
                self.row_1[col] = mark
                self.turn_ongoing = False
            else:
                print("That space is taken, try again!")
                time.sleep(2)
        elif int(row) == 2:
            if self.row_2[col] == "-":
                self.row_2[col] = mark
                self.turn_ongoing = False
            else:
                print("That space is taken, try again!")
                time.sleep(2)
        else:
            if self.row_3[col] == "-":
                self.row_3[col] = mark
                self.turn_ongoing = False
            else:
                print("That space is taken, try again!")
                time.sleep(2)


    # Checks for a winner
    def check_for_winner(self, mark):
        is_winner = True
        if self.row_1[0] == mark and self.row_1[1] == mark and self.row_1[2] == mark:
            print(f"Player {self.current_turn} is the winner!")
        elif self.row_2[0] == mark and self.row_2[1] == mark and self.row_2[2] == mark:
            print(f"Player {self.current_turn} is the winner!")
        elif self.row_3[0] == mark and self.row_3[1] == mark and self.row_3[2] == mark:
            print(f"Player {self.current_turn} is the winner!")
        elif self.row_1[0] == mark and self.row_2[0] == mark and self.row_3[0] == mark:
            print(f"Player {self.current_turn} is the winner!")
        elif self.row_1[1] == mark and self.row_2[1] == mark and self.row_3[1] == mark:
            print(f"Player {self.current_turn} is the winner!")
        elif self.row_1[2] == mark and self.row_2[2] == mark and self.row_3[2] == mark:
            print(f"Player {self.current_turn} is the winner!")
        elif self.row_1[0] == mark and self.row_2[1] == mark and self.row_3[2] == mark:
            print(f"Player {self.current_turn} is the winner!")
        elif self.row_1[2] == mark and self.row_2[1] == mark and self.row_3[0] == mark:
            print(f"Player {self.current_turn} is the winner!")
        else:
            is_winner = False
        return is_winner

    # Updates and provided score
    def keep_score(self, player_number, art):
        print(art)
        if player_number == 1:
            self.player_1_score += 1
        else:
            self.player_2_score += 1
        print(f"Player 1 Score: {self.player_1_score}")
        print(f"Player 2 Score: {self.player_2_score}")