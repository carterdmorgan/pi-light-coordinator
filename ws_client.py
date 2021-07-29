import asyncio
import websockets
import json
import pigpio

class LedStrip:
    RED_PIN = 17
    GREEN_PIN = 22
    BLUE_PIN = 24
    pi = None

    def __init__(self, pi, rp, gp, bp):
        self.pi = pi
        self.RED_PIN = rp
        self.GREEN_PIN = gp
        self.BLUE_PIN = bp
    
    def setColor(self, r, g, b):
        pi.set_PWM_dutycycle(self.RED_PIN, r)
        pi.set_PWM_dutycycle(self.GREEN_PIN, g)
        pi.set_PWM_dutycycle(self.BLUE_PIN, b)

    def clear(self):
        print('clear')
        pi.set_PWM_dutycycle(24, 0)
        pi.set_PWM_dutycycle(17, 0)
        pi.set_PWM_dutycycle(22, 0)
    

RED_PIN = 17
GREEN_PIN = 22
BLUE_PIN = 24

pi = pigpio.pi()
ledStrip = LedStrip(pi, RED_PIN, GREEN_PIN, BLUE_PIN)

async def watch_socket(ledStrip):
    uri = "ws://192.168.0.14:8999"
    async with websockets.connect(uri) as websocket:
        while True:
            greeting = await websocket.recv()
            response = json.loads(greeting)
            print(response)
            r = response['r']
            g = response['g']
            b = response['b']
            ledStrip.setColor(r,g,b)

asyncio.get_event_loop().run_until_complete(watch_socket(ledStrip))