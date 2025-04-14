import RPi.GPIO as GPIO

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)

def decimal_to_binary(number):
    return [int(bit) for bit in bin(number)[2:].zfill(8)]

try:
    while True:
        user_input = input("Введите число от 0 до 255 (или 'q' для выхода): ")
        
        if user_input.lower() == 'q':
            break  
            
        try:
            number = int(user_input)
            
            if number < 0:
                print("Ошибка: введено отрицательное число")
                continue
            if number > 255:
                print("Ошибка: число превышает возможности 8-разрядного ЦАП (макс. 255)")
                continue
                
            GPIO.output(dac, decimal_to_binary(number))
            
            voltage = number * 3.24 / 255
            print(f"Предполагаемое напряжение на ЦАП: {voltage:.2f} В")
            
        except ValueError:
            if not user_input.isdigit():
                print("Ошибка: введено не числовое значение")
            else:
                print("Ошибка: введено не целое число")

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()