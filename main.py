import sys
from random import randrange, randint

from PyQt6.QtCore import QPointF
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(500, 500)
        self.setWindowTitle('Координаты')
        # self.setMouseTracking(True)
        self.button = QPushButton('❤', self)
        self.button.move(100, 100)
        self.button.resize(40, 50)
        self.button.clicked.connect(self.run)

        self.cx = 100
        self.cy = 100

    def paintEvent(self, event):
        qt = QPainter(self)
        r = randint(20, 100)
        x, y = randrange(100, 500), randrange(100, 500)
        qt.setBrush(QColor(255, 255, 0))
        qt.drawEllipse(QPointF(x, y), r, r)

    #
    def run(self):
        self.update()

    # def mouseMoveEvent(self, event):
    #     if (self.cx - 20 <= event.pos().x() <= self.cx + 60 and
    #             self.cy - 20 <= event.pos().y() <= self.cy + 60):
    #         self.cx = randrange(1, 460)
    #         self.cy = randrange(1, 460)
    #         self.button.move(self.cx, self.cy)
    #         print(self.button.x(), self.button.y())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    # sys.excepthook = except_hook
    sys.exit(app.exec())
