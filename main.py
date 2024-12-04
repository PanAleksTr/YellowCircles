import sys
from random import randrange

from PyQt6.QtWidgets import QWidget, QApplication, QPushButton


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(500, 500)
        self.setWindowTitle('Координаты')
        self.setMouseTracking(True)
        self.button = QPushButton('❤', self)
        self.button.move(100, 100)
        self.button.resize(40, 40)

        self.cx = 100
        self.cy = 100

    def mouseMoveEvent(self, event):
        if (self.cx - 20 <= event.pos().x() <= self.cx + 60 and
                self.cy - 20 <= event.pos().y() <= self.cy + 60):
            self.cx = randrange(1, 460)
            self.cy = randrange(1, 460)
            self.button.move(self.cx, self.cy)
            print(self.button.x(), self.button.y())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    # sys.excepthook = except_hook
    sys.exit(app.exec())
