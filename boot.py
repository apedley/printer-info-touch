# import espidf as esp
import gc
import ConnectWiFi

# import webrepl
# webrepl.start()

# import machine
# led_pin = machine.Pin(4, machine.Pin.OUT)
# 
# print('Restart cause: {}'.format(machine.reset_cause()))

ConnectWiFi.connect()

# run garbage collector at the end to clean up
gc.collect()