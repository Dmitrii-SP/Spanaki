import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
pwm_pin = 21  

GPIO.setup(pwm_pin, GPIO.OUT)

pwm = GPIO.PWM(pwm_pin, 1000)
pwm.start(0)  

try:
    while True:
        try:
            duty_cycle = float(input("Введите коэффициент заполнения (0-100): "))
            
            if duty_cycle < 0 or duty_cycle > 100:
                print("Ошибка: значение должно быть в диапазоне 0-100")
                continue
            
            pwm.ChangeDutyCycle(duty_cycle)
            
            voltage = 3.26 * duty_cycle / 100  
            print(f"Предполагаемое напряжение на RC-цепи: {voltage:.2f} В")
            
        except ValueError:
            print("Ошибка: введите числовое значение!")

finally:
    pwm.stop()
    GPIO.cleanup()