import math

class pid_system:
    Kp = 1
    Ki = 0
    Kd = 0
    frequency = 0
    integral_length = 0
    integral_list = []

    last_sensor_input = 0
    current_sensor_input = 0

    def setup(self, frequency_set: int, integral_length_set: float):
        frequency = frequency_set
        integral_length = int(frequency * integral_length_set)

    def advance(self, control_input: float, sensor_input: float):
        proportional_output = sensor_input

        self.integral_list.append(sensor_input)
        self.integral_list.pop(0)
        integral_output = 0
        for integral_value in self.integral_list:
            integral_output += integral_value

        integral_value /= self.integral_length

        self.last_sensor_output = self.current_sensor_input
        self.current_sensor_input = sensor_input

        derivative_output = (self.current_sensor_input - self.last_sensor_output) * self.frequency

        pid_output = proportional_output * self.Kp + integral_output * self.Ki + derivative_output * self.Kd

        return proportional_output

