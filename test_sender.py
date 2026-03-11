import time
import board
import busio
import digitalio
import adafruit_bmp280
import adafruit_rfm9x

spi = busio.SPI(clock=board.GP2, MOSI=board.GP3, MISO=board.GP4)
cs = digitalio.DigitalInOut(board.GP6)
reset = digitalio.DigitalInOut(board.GP7)

rfm9x = adafruit_rfm9x.RFM9x(spi, cs, reset, 433.0)
rfm9x.tx_power = 23

i2c = busio.I2C(board.GP1, board.GP0)
bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)

print("Transmitter ready")

while True:
    temp = bmp280.temperature
    pres = bmp280.pressure
    message = "{:.5f},{:.5f}".format(temp, pres)
    rfm9x.send(bytes(message, "utf-8"))
    print("Sent:", message)
    time.sleep(1)