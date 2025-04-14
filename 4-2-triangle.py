import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setup(dac, GPIO.OUT)

def dec2bin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def get_period():
    while True:
        try:
            period = float(input("Введите период треугольного сигнала (секунды): "))
            if period <= 0:
                print("Период должен быть положительным числом!")
                continue
            return period
        except ValueError:
            print("Ошибка: введите числовое значение!")

try:
    period = get_period()
    half_period = period / 2
    step_time = half_period / 255
    
    while True:
        for value in range(256):
            GPIO.output(dac, dec2bin(value))
            time.sleep(step_time)
        
        for value in range(255, -1, -1):
            GPIO.output(dac, dec2bin(value))
            time.sleep(step_time)

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()