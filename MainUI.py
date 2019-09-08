import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
import numpy as np
import threading
from bitmex_websocket import BitMEXWebsocket
from time import sleep


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initBitmex()
        self.A=np.array([[1,2],[3,4]])
        self.B=np.array([[1,4],[7,8]])
        self.initUI()
        t = threading.Thread(target=self.initPrice)
        t.start()

    def initUI(self):

        self.label1 = QLabel(f"{np.dot(self.A,self.B)}", self)
        self.label1.setAlignment(Qt.AlignCenter)

        self.label2 = QLabel('고래를 들어 관악을 보게하라', self)
        self.label2.setAlignment(Qt.AlignVCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.label2)

        self.setLayout(layout)
        self.setWindowTitle('QLabel')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def initPrice(self):

        print(f"Instrument data: {self.ws.get_instrument()}")

        # Run forever
        while (self.ws.ws.sock.connected):
            self.label1.setText(f"{self.ws.get_ticker()}")
            if self.ws.api_key:
                print(f"Funds: {self.ws.funds()}")
            print(f"Recent Trades: {self.ws.recent_trades()}\n\n")
            sleep(5)

        self.label1.setText("hi")

    def initBitmex(self):
        self.ws = BitMEXWebsocket(endpoint="https://testnet.bitmex.com/api/v1", symbol="XBTUSD",
                             api_key=None, api_secret=None)



if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())


