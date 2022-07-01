import math

class pid_system:
    Kp = 0
    Ki = 0
    Kd = 0
    frequency = 0
    integral_length = 0
    integral_list = []

    def setup(self, frequency_set: int, integral_length_set: float):
        frequency = frequency_set
        integral_length = int(frequency * integral_length_set)

    def advance(self, control_input: float, sensor_input: float):

