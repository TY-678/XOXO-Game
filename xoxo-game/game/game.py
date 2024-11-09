import sys
from PyQt6 import QtWidgets
from ui.ui import Ui_Dialog
from logic.game_logic import GameLogic


class GameApp(QtWidgets.QDialog, Ui_Dialog, GameLogic):

    def __init__(self):
        super().__init__()
        GameLogic.__init__(self)
        self.setupUi(self)
        self.setup_connections()
        self.update_score_dispaly()

    def setup_connections(self):
        for button in self.gameAeraButtonList:
            button.clicked.connect(lambda _, b=button: self.click_game_button(b))

        self.playButton.clicked.connect(self.game_start)
        self.cancelButton.clicked.connect(self.cancel_setp)
        self.resetButton.clicked.connect(self.reset_all_data)

    def update_score_dispaly(self):
        self.player1Score_display.display(self.player_1_score)
        self.player2Score_display.display(self.player_2_score)

    def click_game_button(self, button):
        game_status = self.on_button_click(button)
        self.update_message_display(self.gameMessageBrowser, game_status)
        self.update_score_dispaly()

    def reset_all_button(self):
        [self.reset_button(button) for button in self.gameAeraButtonList]

    def game_start(self):
        self.reset_game()
        self.reset_all_button()
        self.update_message_display(self.gameMessageBrowser, None)

    def reset_all_data(self):
        self.reset_data()
        self.reset_all_button()
        self.update_score_dispaly()
