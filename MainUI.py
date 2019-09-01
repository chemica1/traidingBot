import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
import numpy as np

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.A=np.array([[1,2],[3,4]])
        self.B=np.array([[1,4],[7,8]])
        self.initUI()

    def initUI(self):

        label1 = QLabel(f"{np.dot(self.A,self.B)}", self)
        label1.setAlignment(Qt.AlignCenter)

        label2 = QLabel('고래를 들어 관악을 보게하라', self)
        label2.setAlignment(Qt.AlignVCenter)

        font1 = label1.font()
        font1.setPointSize(20)

        font2 = label2.font()
        font2.setFamily('Times New Roman')
        font2.setBold(True)

        label1.setFont(font1)
        label2.setFont(font2)

        layout = QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(label2)

        self.setLayout(layout)

        self.setWindowTitle('QLabel')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())


