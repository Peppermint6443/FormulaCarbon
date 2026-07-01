# ========================= #
#         Car Class         #
# ========================= #
# imports

class States:
    IDLE = 'IDL'
    ARMED = 'ARM'
    RUNNING = 'RUN'
    TRIGGER = 'TRG'


class Car:
    def __init__(self):
        self.car_state = States.IDLE
        return

    def update(self):
        # idle
        if self.car_state == States.IDLE:
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
        # return true when user types b and pushes enter
        user_input = input('Press b to press the button: ')
        return user_input == 'b'

    def is_sensor_triggered(self):
        # return true when sensor is triggered
        user_input = input('Press s to trigger the sensor: ')
        return user_input == 's'

    def is_finished(self):
        # return true when car has finished its task
        user_input = input('Press f to indicate finished: ')
        return user_input == 'f'
    
    def drive(self):
        print('Car is driving.')


class EV(Car):
    def __init__(self):
        super().__init__()

    def drive(self):
        print('EV is driving.')

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