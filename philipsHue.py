from phue import Bridge
from playsound import playsound
bridge_ip_address = '192.168.1.103'
b = Bridge(bridge_ip_address)


import time

def access_lights(bridge_ip_address):
    b = Bridge(bridge_ip_address)
    light_names_list = b.get_light_objects('name')
    return light_names_list

def fbi():
    lights = access_lights(bridge_ip_address)
    for light in lights:
        lights[light].on = False
    time.sleep(10)
    for light in lights:
        lights[light].on = True

def bomb():
    lights = access_lights(bridge_ip_address)
    running = 0
    while running < 3:
        time.sleep(0.5)
        for light in lights:
            lights[light].on = True
        time.sleep(0.5)
        for light in lights:
            lights[light].on = False
        running = running + 1
def lightsOn():
    lights = access_lights(bridge_ip_address)
    for light in lights:
        lights[light].on = True


