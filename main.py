from machine import Pin
from time import sleep

led_board = Pin("LED", Pin.OUT)
sleep(1)    #le damos tiempo a vREPL
print("\nLED esta destellando...")
while True:
    try:
        led_board.toggle() 
        # led_board.value(not led_board.value()) #para esp32, lee el estado, lo niega y pasa como argumento 
        sleep(.25) # sleep 0.5sec
    except KeyboardInterrupt:
        break
led_board.off()
print("Listo")
