import busio
import board
import adafruit_bmp280
i2c = busio.I2C(scl=board.GP27, sda=board.GP26)  #look at diagram and read the light green label for the hole it is plugged in
bmp280_sensor = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)
bmp280_sensor.temperature
def read_temperature():
    return bmp280_sensor.temperature
def read_pressure():
    return bmp280_sensor.pressure
