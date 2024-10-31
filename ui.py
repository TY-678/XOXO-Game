from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(240, 320)
        self.gameAeraButton_0_0 = QtWidgets.QPushButton(parent=Dialog)
        self.gameAeraButton_0_0.setGeometry(QtCore.QRect(70, 160, 50, 55))
        self.gameAeraButton_0_0.setText("")
        self.gameAeraButton_0_0.setObjectName("gameAeraButton_0_0")
        self.gameAeraButton_0_1 = QtWidgets.QPushButton(parent=Dialog)
        self.gameAeraButton_0_1.setGeometry(QtCore.QRect(125, 160, 50, 55))
        self.gameAeraButton_0_1.setText("")
        self.gameAeraButton_0_1.setObjectName("gameAeraButton_0_1")
        self.gameAeraButton_0_2 = QtWidgets.QPushButton(parent=Dialog)
        self.gameAeraButton_0_2.setGeometry(QtCore.QRect(180, 160, 50, 55))
        self.gameAeraButton_0_2.setText("")
        self.gameAeraButton_0_2.setObjectName("gameAeraButton_0_2")
        self.gameAeraButton_1_0 = QtWidgets.QPushButton(parent=Dialog)
        self.gameAeraButton_1_0.setGeometry(QtCore.QRect(70, 210, 50, 55))
        self.gameAeraButton_1_0.setText("")
        self.gameAeraButton_1_0.setObjectName("gameAeraButton_1_0")
        self.gameAeraButton_1_1 = QtWidgets.QPushButton(parent=Dialog)
        self.gameAeraButton_1_1.setGeometry(QtCore.QRect(125, 210, 50, 55))
        self.gameAeraButton_1_1.setText("")
        self.gameAeraButton_1_1.setObjectName("gameAeraButton_1_1")
        self.gameAeraButton_1_2 = QtWidgets.QPushButton(parent=Dialog)
        self.gameAeraButton_1_2.setGeometry(QtCore.QRect(180, 210, 50, 55))
        self.gameAeraButton_1_2.setText("")
        self.gameAeraButton_1_2.setObjectName("gameAeraButton_1_2")
        self.gameAeraButton_2_1 = QtWidgets.QPushButton(parent=Dialog)
        self.gameAeraButton_2_1.setGeometry(QtCore.QRect(125, 260, 50, 55))
        self.gameAeraButton_2_1.setText("")
        self.gameAeraButton_2_1.setObjectName("gameAeraButton_2_1")
        self.gameAeraButton_2_0 = QtWidgets.QPushButton(parent=Dialog)
        self.gameAeraButton_2_0.setGeometry(QtCore.QRect(70, 260, 50, 55))
        self.gameAeraButton_2_0.setText("")
        self.gameAeraButton_2_0.setObjectName("gameAeraButton_2_0")
        self.gameAeraButton_2_2 = QtWidgets.QPushButton(parent=Dialog)
        self.gameAeraButton_2_2.setGeometry(QtCore.QRect(180, 260, 50, 55))
        self.gameAeraButton_2_2.setText("")
        self.gameAeraButton_2_2.setObjectName("gameAeraButton_2_2")
        self.playButton = QtWidgets.QPushButton(parent=Dialog)
        self.playButton.setGeometry(QtCore.QRect(160, 20, 65, 31))
        self.playButton.setObjectName("playButton")
        self.cancelButton = QtWidgets.QPushButton(parent=Dialog)
        self.cancelButton.setGeometry(QtCore.QRect(160, 50, 65, 31))
        self.cancelButton.setObjectName("cancelButton")
        self.resetButton = QtWidgets.QPushButton(parent=Dialog)
        self.resetButton.setGeometry(QtCore.QRect(160, 80, 65, 31))
        self.resetButton.setObjectName("resetButton")
        self.textBrowser = QtWidgets.QTextBrowser(parent=Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(10, 20, 141, 91))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.gameMessageBrowser = QtWidgets.QTextBrowser(parent=Dialog)
        self.gameMessageBrowser.setGeometry(QtCore.QRect(10, 120, 221, 31))
        self.gameMessageBrowser.setObjectName("gameMessageBrowser")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(10, 170, 51, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 260, 51, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 200, 51, 21))
        self.label_3.setObjectName("label_3")
        self.player1Score = QtWidgets.QLCDNumber(parent=Dialog)
        self.player1Score.setGeometry(QtCore.QRect(10, 220, 51, 21))
        self.player1Score.setObjectName("player1Score")
        self.player2Score = QtWidgets.QLCDNumber(parent=Dialog)
        self.player2Score.setGeometry(QtCore.QRect(10, 280, 51, 21))
        self.player2Score.setObjectName("player2Score")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.playButton.setText(_translate("Dialog", "Paly"))
        self.cancelButton.setText(_translate("Dialog", "Cancel"))
        self.resetButton.setText(_translate("Dialog", "Reset"))
        self.textBrowser.setHtml(
            _translate(
                "Dialog",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                '<p align="center" dir=\'rtl\' style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:32pt; font-weight:600;">XOXO Game</span></p></body></html>',
            )
        )
        self.label.setText(_translate("Dialog", "Score"))
        self.label_2.setText(_translate("Dialog", "Player 2"))
        self.label_3.setText(_translate("Dialog", "Player 1"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
