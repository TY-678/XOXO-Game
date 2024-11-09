import sys
from PyQt6 import QtWidgets
from game.game import GameApp


def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = GameApp()
    ui.show()
    ui.reset_all_data()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
