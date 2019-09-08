import numpy as np
from bitmex_websocket import BitMEXWebsocket
import logging
from time import sleep

#행렬의 덧셈과 뺄셈
class cal:

    # Basic use of websocket.
    def run(self):
        logger = self.setup_logger()

        # Instantiating the WS will make it connect. Be sure to add your api_key/api_secret.
        ws = BitMEXWebsocket(endpoint="https://testnet.bitmex.com/api/v1", symbol="XBTUSD",
                             api_key=None, api_secret=None)

        logger.info("Instrument data: %s" % ws.get_instrument())

        # Run forever
        while(ws.ws.sock.connected):
            logger.info("Ticker: %s" % ws.get_ticker())
            if ws.api_key:
                logger.info("Funds: %s" % ws.funds())
            logger.info("Recent Trades: %s\n\n" % ws.recent_trades())
            sleep(10)


    def setup_logger(self):
        # Prints logger info to terminal
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)  # Change this to DEBUG if you want a lot more info
        ch = logging.StreamHandler()
        # create formatter
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        # add formatter to ch
        ch.setFormatter(formatter)
        logger.addHandler(ch)
        return logger


if __name__ == '__main__':
    a = cal()
    a.run()