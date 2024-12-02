import sys

from random import randint
from PyQt6.QtCore import Qt, QRectF, QPointF
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QMainWindow, QLabel, QSlider
from PyQt6.QtGui import QImage, QColor, QTransform, QPainter
from classui import Ui_MainWindow


class Supermatism(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.generate.clicked.connect(self.drawf)
        self.f = False

    def drawf(self):
        self.f = True
        self.update()

    def paintEvent(self, event):
        if self.f:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw()
            self.qp.end()

    def draw(self):
        radius = randint(20, 100)

        self.qp.setBrush(QColor(*[randint(0, 255) for i in range(3)]))
        self.qp.drawEllipse(QPointF(randint(0, 355), randint(0, 355)), radius, radius)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Supermatism()
    ex.show()
    sys.exit(app.exec())
