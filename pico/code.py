import digitalio
import board
import time
# import bmp280
import radio_v2
# led = digitalio.DigitalInOut(board.LED)
# led.direction = digitalio.Direction. OUTPUT
# led.value = True
# count = 2
# switch = int(input("sending (1) or Receiving (2): "))
# if switch ==1:
#     is_cansat = True
# elif switch == 2:
#     is_cansat = False
# else:
#     print("Error!")# switch = int(input("sending (1) or Receiving (2): "))
# if switch ==1:
#     is_cansat = True
# elif switch == 2:
#     is_cansat = False
# else:
#     print("Error!")

# while is_cansat == True:
#     cansat_temperature = bmp280.read_temperature()
#     cansat_pressure = bmp280.read_pressure()
#     radio.send(f"[Salesian Cansat]: Temperature: {cansat_temperature}, Pressure: {cansat_pressure}")
#     is_cansat = False
# while is_cansat == False:
#     radio_message = radio.try_read()
#     if radio_message is not None:
#         print(f"Radio RX {packet_count} {radio_message}, RSSI: {radio.rssi()}")
#         packet_count + 1

# while count > 0:  # flashes for 2 seconds then stops
    # led.value = False
    # time.sleep(0.5)
    # led.value = True
    # time.sleep(0.5)
    # count = count - 1
'''
cansat_temperature = bmp280.read_temperature()
print(cansat_temperature)
cansat_pressure = bmp280.read_pressure()
print(cansat_pressure)
print("Temperature: {: .5f} Pressure: {: .5f}". format(cansat_temperature, cansat_pressure))
print("Radio message sent")


while True:
    temp = bmp280.read_temperature()
    pres = bmp280.read_pressure()
    # rad = read_radiation()   # optional
    message = "{:.5f},{:.5f}".format(temp, pres)
    print(message)  # sends over USB serial automatically
    time.sleep(1)
'''

