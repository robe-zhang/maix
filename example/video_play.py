
import video,time
from Maix import GPIO
from board import board_info
from fpioa_manager import fm
import lcd

lcd.init()
fm.register(34,  fm.fpioa.I2S0_OUT_D1)
fm.register(35,  fm.fpioa.I2S0_SCLK)
fm.register(33,  fm.fpioa.I2S0_WS)

v = video.open("/sd/zombie.avi")
print(v)
v.volume(50)
while True:
    if v.play() == 0:
        print("play end")
        break
v.__del__()
lcd.clear()
lcd.draw_string(100, 100, "end", lcd.RED, lcd.BLACK)
