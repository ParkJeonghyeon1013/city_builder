

import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PySide2 import QtGui

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Drag and Drop Example")
        self.setGeometry(300, 300, 400, 200)

        # 파일 경로를 보여줄 라벨
        self.file_path_label = QLabel("Drag and drop file here", self)
        self.file_path_label.setAlignment(QtGui.Qt.AlignCenter)

        # 메인 윈도우의 레이아웃 설정
        layout = QVBoxLayout()
        layout.addWidget(self.file_path_label)

        # 위젯에 레이아웃 설정
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        # 그래그 앤 드롭 이벤트 핸들링
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        urls = event.mimeData().urls()
        if urls:
            file_path = urls[0].toLocalFile()
            self.file_path_label.setText(file_path)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
