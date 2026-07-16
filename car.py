# ========================= #
#         Car Class         #
# ========================= #
# imports
from machine import Pin

class States:
    IDLE = 'IDL'
    ARMED = 'ARM'
    RUNNING = 'RUN'
    TRIGGER = 'TRG'


class Car:
    def __init__(self, arm_button_pin = 21, distance_sensor_pin = 22, motor_pin = 20):
        self.car_state = States.IDLE

        # set up pin for arm button
        self.arm_button = Pin(arm_button_pin, Pin.IN, Pin.PULL_UP)

        # set up pin for distance sensor
        self.distance_sensor = Pin(distance_sensor_pin, Pin.IN, Pin.PULL_UP)

        # set up pin for motor control
        self.motor = Pin(motor_pin, Pin.OUT)
        return

    def update(self):
        # idle
        if self.car_state == States.IDLE:
            self.stop_motors()
            if self.is_button_pressed():
                self.update_state(States.ARMED)

        # armed
        if self.car_state == States.ARMED:
            if self.is_sensor_triggered():
                self.update_state(States.RUNNING)

        # running
        if self.car_state == States.RUNNING:
            # can eventally include logging of cool metrics
            self.drive()
            if self.is_finished():
                self.update_state(States.IDLE)

    def update_state(self, new_state):
        temp = self.car_state
        self.car_state = new_state
        print(f'Car state updated from {temp} to {self.car_state}')

    def is_button_pressed(self):
        # check if button is pressed
        button_value = self.arm_button.value()
        
        # check to see if voltage is low (button pressed)
        if button_value == 0:
            print('Button pressed.')
            return True
        return False

    def is_sensor_triggered(self):
        # return true when sensor is triggered
        sensor_value = self.distance_sensor.value()
        if sensor_value == 0:
            print('Sensor triggered.')
            return True
        return False

    def is_finished(self):
        # return true when car has finished its task
        # This is a placeholder - replace with actual logic
        return False
    
    def drive(self):
        print('Car is driving.')
        self.motor.value(1)

    def stop_motors(self):
        self.motor.value(0)


class EV(Car):
    def __init__(self):
        super().__init__()

    def drive(self):
        self.motor.value(1)

class CO2(Car):
    def __init__(self):
        super().__init__()

    def update(self):
        # idle
        if self.car_state == States.IDLE:
            if self.is_button_pressed():
                self.update_state(States.ARMED)

        # armed
        if self.car_state == States.ARMED:
            if self.is_sensor_triggered():
                self.update_state(States.TRIGGER)

        if self.car_state == States.TRIGGER:
            self.trigger_cartridge()
            self.update_state(States.RUNNING)

        # running
        if self.car_state == States.RUNNING:
            # can also include logging and other cool features here
            self.drive()
            if self.is_finished():
                self.update_state(States.IDLE)

    def drive(self):
        print('CO2 car is driving.')

    def trigger_cartridge(self):
        print('### HAMMER ACTIVATED ###')