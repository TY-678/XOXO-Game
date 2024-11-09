from typing import Optional


class GameLogic:

    def __init__(self):
        self._reset_score()
        self._reset_step_count()
        self._reset_winner()
        self._reset_cache()
        self._reset_player_to_waiting()
        self._reset_board()

    def reset_game(self):
        self._reset_board()
        self._reset_step_count()
        self._reset_player_to_start()
        self._reset_winner()
        self._reset_cache()

    def on_button_click(self, button):
        if self.current_player not in ("player_1", "player_2"):
            return self.current_player
        elif button.text() == "":
            mark = self._mapping_player_mark(self.current_player)
            button.setText(mark)
            row = button.property("row")
            col = button.property("col")
            self.step_count += 1
            self._mark_place(mark, row, col)
            self._record_to_cache(button, row, col)
            self._listent_game()
            if (self.step_count == 9) or (self.winner is not None):
                return self._game_over()
            self._switch_player()

    def cancel_setp(self):
        if (self.current_player in ("player_1", "player_2")) and (self.cache != {}):
            self._mark_place("", self.cache["row"], self.cache["col"])
            self.reset_button(self.cache["button"])
            self._reset_cache()
            self._switch_player()

    def update_message_display(self, message_browser, message):
        if message is None:
            turn = self.current_player.lower().replace("_", " ")
            mark = self._mapping_player_mark(player=self.current_player).lower()
            message = f"It's {turn} to play {mark}"
        message_browser.setText(message)

    def reset_button(self, button):
        button.setText("")

    def reset_data(self):
        self._reset_score()
        self._reset_player_to_waiting()

    def _game_over(self):
        self.current_player = "game over"
        if self.winner is None:
            display_message = "Game tie!"
        else:
            self._add_score(self.winner)
            display_message = f"Winner is {self.winner.lower().replace("_", " ")}!"
        return display_message

    def _listent_game(self):
        for row in self.game_board:
            if row[0] == row[1] == row[2]:
                self.winner = self._mapping_player_mark(mark=row[0])
                break

        for col in range(3):
            if (
                self.game_board[0][col]
                == self.game_board[1][col]
                == self.game_board[2][col]
            ):
                self.winner = self._mapping_player_mark(mark=self.game_board[0][col])
                break

        if self.game_board[0][0] == self.game_board[1][1] == self.game_board[2][2]:
            self.winner = self._mapping_player_mark(mark=self.game_board[0][0])

        if self.game_board[0][2] == self.game_board[1][1] == self.game_board[2][0]:
            self.winner = self._mapping_player_mark(mark=self.game_board[0][2])

    def _add_score(self, player):
        if player == "player_1":
            self.player_1_score += 1
        elif player == "player_2":
            self.player_2_score += 1

    def _switch_player(self):
        match self.current_player.lower():
            case "player_1":
                self.current_player = "player_2"
            case "player_2":
                self.current_player = "player_1"

    def _record_to_cache(self, button, row, col):
        self.cache["button"] = button
        self.cache["row"] = row
        self.cache["col"] = col

    def _mapping_player_mark(
        self,
        player: Optional[str] = None,
        mark: Optional[str] = None,
    ):
        if player:
            match player:
                case "player_1":
                    return "O"
                case "player_2":
                    return "X"
        if mark:
            match mark:
                case "O":
                    return "player_1"
                case "X":
                    return "player_2"
        return None

    def _mark_place(self, mark, row, col):
        self.game_board[row][col] = mark

    def _reset_winner(self):
        self.winner = None

    def _reset_step_count(self):
        self.step_count = 0

    def _reset_board(self):
        self.game_board = [["" for _ in range(3)] for _ in range(3)]

    def _reset_player_to_start(self):
        self.current_player = "player_1"

    def _reset_player_to_waiting(self):
        self.current_player = "Click play to start game"

    def _reset_cache(self):
        self.cache = {}

    def _reset_score(self):
        self.player_1_score = 0
        self.player_2_score = 0
