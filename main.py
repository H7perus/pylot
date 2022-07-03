import math

from SimConnect import  *
import time
import CoordManage
import keyboard
import pylot

def current_micro_time():
    return round(time.time() * 1000000)

sm = SimConnect()

aq = AircraftRequests(sm, _time=0)

frequency = 50
altitude = 0.0
pitch = 0.0
roll = 0.0

pitch_pid = pylot.pid_system
roll_pid = pylot.pid_system

pitch_pid.setup(frequency, 1.5)
roll_pid.setup(frequency, 1.5)


target_coordinates = [(51.5072 / 180) * math.pi, (0.1337 / 180) * math.pi]
#target_coordinates2 = [(51.5072 / 180) * math.pi, (4 / 180) * math.pi]

next_loop = current_micro_time()
while True:
    while current_micro_time() >= next_loop:
        next_loop += 1000000 / frequency
        self_coordinates = [aq.get("PLANE_LATITUDE") / 180 * math.pi, aq.get("PLANE_LONGITUDE") / 180 * math.pi]
        altitude = aq.get("PLANE_ALTITUDE")
        pitch = aq.get("PLANE_PITCH_DEGREES")
        roll = aq.get("PLANE_BANK_DEGREES")
        control_pitch = pitch_pid.advance(0, pitch)
        control_roll =  roll_pid.advance(0, roll)
        aq.set("ELEVATOR_POSITION", control_pitch)
        aq.set("AILERON_POSITION", control_roll)
        print(CoordManage.coordinates_to_heading(self_coordinates, target_coordinates) * 180 / math.pi)
        print(self_coordinates)
        print(target_coordinates)


sm.exit()
quit()
