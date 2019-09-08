from bitmex_websocket import BitMEXWebsocket
from time import sleep

#행렬의 덧셈과 뺄셈
class cal:

    # Basic use of websocket.
    def run(self):
        # Instantiating the WS will make it connect. Be sure to add your api_key/api_secret.
        ws = BitMEXWebsocket(endpoint="https://testnet.bitmex.com/api/v1", symbol="XBTUSD",
                             api_key=None, api_secret=None)

        print(f"Instrument data: {ws.get_instrument()}")

        # Run forever
        while(ws.ws.sock.connected):
            print(f"Ticker: {ws.get_ticker()}")
            if ws.api_key:
                print(f"Funds: {ws.funds()}")
            print(f"Recent Trades: {ws.recent_trades()}\n\n")
            sleep(10)


if __name__ == '__main__':
    a = cal()
    a.run()