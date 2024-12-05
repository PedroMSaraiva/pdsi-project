from djitellopy import Tello
from time import sleep

tello = Tello()
tello.connect()
sleep(2)
print(f"Tello battery: {tello.get_battery}%")

tello.takeoff()

for i in range(10):
    tello.move_forward(100)
    sleep(2)
    tello.move_left(100)
    sleep(2)
    tello.move_back(100)
    sleep(2)
    tello.move_right(100)