import time
import digitalio
import board
import busio
import adafruit_rfm9x

spi = busio.SPI(clock=board.GP2, MOSI=board.GP3, MISO=board.GP4)

cs = digitalio.DigitalInOut(board.GP6)
reset = digitalio.DigitalInOut(board.GP7)

rfm9x = adafruit_rfm9x.RFM9x(spi, cs, reset, 433.0)

print("Receiver ready")

while True:
    packet = rfm9x.receive(timeout=1.0)

    if packet is not None:
        message = packet.decode("utf-8")
        print(message)

    time.sleep(0.1)