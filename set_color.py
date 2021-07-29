import pigpio
import sys

def clear():
    print('clear')
    pi.set_PWM_dutycycle(24, 0)
    pi.set_PWM_dutycycle(17, 0)
    pi.set_PWM_dutycycle(22, 0)

def setRed():
    clear()
    print('red')
    pi.set_PWM_dutycycle(24, 0)
    pi.set_PWM_dutycycle(17, 255)

def setGreen():
    clear()
    print('green')
    pi.set_PWM_dutycycle(17, 0)
    pi.set_PWM_dutycycle(22, 255)

def setBlue():
    clear()
    print('blue')
    pi.set_PWM_dutycycle(22, 0)
    pi.set_PWM_dutycycle(24, 255)

mode = 'clear'

if len(sys.argv) > 1:
    mode = sys.argv[1]

pi = pigpio.pi()

if mode.startswith("r"):
    setRed()
elif mode.startswith("g"):
    setGreen()
elif mode.startswith("b"):
    setBlue()
else:
    clear()