from robot import Robot, log_action


class CleaningRobot(Robot):
    def __init__(self, name, battery=100, dust_capacity=500):
        super().__init__(name, battery)
        self.dust_capacity = dust_capacity

    @log_action
    def perform_task(self, **kwargs):
        self.use_battery(10)
        return f"{self.name} vacuumed the living room."


class DroneRobot(Robot):
    def __init__(self, name, battery=100, max_altitude=120):
        super().__init__(name, battery)
        self.max_altitude = max_altitude

    def perform_task(self, **kwargs):
        self.use_battery(25)
        return f"{self.name} completed an aerial survey up to {self.max_altitude}m."