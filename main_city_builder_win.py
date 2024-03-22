from PySide2.QtWidgets import QApplication, QLabel
from PySide2.QtGui import QColor

class ClickableLabel(QLabel):
    def __init__(self, text):
        super().__init__(text)
        self.setStyleSheet("border: 2px solid black; padding: 5px;")
        self.setMouseTracking(True)
        self.clicked = False

    def enterEvent(self, event):
        if not self.clicked:
            self.setStyleSheet("border: 2px solid blue; padding: 5px;")

    def leaveEvent(self, event):
        if not self.clicked:
            self.setStyleSheet("border: 2px solid black; padding: 5px;")

    def mousePressEvent(self, event):
        self.setStyleSheet("border: 2px solid red; padding: 5px;")
        self.clicked = True

    def mouseReleaseEvent(self, event):
        self.setStyleSheet("border: 2px solid black; padding: 5px;")
        self.clicked = False

if __name__ == "__main__":
    app = QApplication([])
    label = ClickableLabel("Click me")
    label.show()
    app.exec_()
