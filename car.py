# ========================= #
#         Car Class         #
# ========================= #
# imports
from machine import Pin, PWM, time_pulse_us
import time

class States:
    IDLE = 'IDL'
    ARMED = 'ARM'
    RUNNING = 'RUN'
    TRIGGER = 'TRG'


class Car:
    def __init__(self, arm_button_pin = 21, echo_sensor_pin = 23, trig_sensor_pin = 22, motor_pins = [18, 19, 20]):
        self.car_state = States.IDLE

        # set up pin for arm button
        self.arm_button = Pin(arm_button_pin, Pin.IN, Pin.PULL_UP)

        # set up pin for distance sensor
        self.echo = Pin(echo_sensor_pin, Pin.IN)
        self.trig = Pin(trig_sensor_pin, Pin.OUT, value=0)

        # set up pin for motor control
        self.motor_in1 = Pin(motor_pins[0], Pin.OUT, value = 0)
        self.motor_in2 = Pin(motor_pins[1], Pin.OUT, value = 0)
        self.motor_en = PWM(Pin(motor_pins[2]), freq=1000)
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
        # set the threshold distance for triggering sensor
        THRESHOLD = 15

        d = self.distance_cm()
        print(d)
        if d is not None and d > THRESHOLD:
            return True
        else:
            return False

    def is_finished(self):
        # return true when car has finished its task
        d = self.distance_cm()
        Threshold = 5
        if d is not None and d < Threshold:
            return True
        # This is a placeholder - replace with actual logic
        return False
    
    def drive(self):
        print('Car is driving.')
        self.motor_in1.value(1)
        self.motor_in2.value(0)

        # set the motor to full speed
        self.motor_en.duty_u16(65535)

    def stop_motors(self):
        self.motor_in1.value(0)
        self.motor_in2.value(0)
        self.motor_en.duty_u16(0)

    def distance_cm(self):
        self.trig.value(0); time.sleep_us(2)
        self.trig.value(1); time.sleep_us(10)
        self.trig.value(0)
        dur = time_pulse_us(self.echo, 1, 30000)
        if dur < 0:
            return None
        return (dur* 0.0343)/2


class EV(Car):
    def __init__(self):
        super().__init__()

    def drive(self):
        self.motor_in1.value(1)
        self.motor_in2.value(0)
        self.motor_en.duty_u16(65535)

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