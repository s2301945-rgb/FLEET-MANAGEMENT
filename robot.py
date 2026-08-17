import abc
import functools
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

class InsufficientBatteryError(Exception):
    def __init__(self, name, required, available):
        self.name = name
        self.required = required
        self.available = available
        message = f"{name} needs {required}% battery for this task but only has {available}%."
        super().__init__(message)


def log_action(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        logging.info(f"{self.name}: starting {func.__name__}")
        result = func(self, *args, **kwargs)
        logging.info(f"{self.name}: finished {func.__name__}")
        return result
    return wrapper

class Robot(abc.ABC):
    manufacturer = "RoboCorp"
    population = 0

    def __init__(self, name, battery=100):
        self.name = name
        self._battery = 0
        self.battery = battery
        Robot.population += 1

    @property
    def battery(self):
        return self._battery

    @battery.setter
    def battery(self, value):
        self._battery = max(0, value)

    def __str__(self):
        return f"{self.name} ({self.battery}% battery)"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, battery={self.battery})"

    @abc.abstractmethod
    def perform_task(self, **kwargs):
        """Subclasses must implement their own task behavior."""
        raise NotImplementedError    
    def use_battery(self, amount):
        if amount > self.battery:
            raise InsufficientBatteryError(self.name, amount, self.battery)
        self.battery -= amount

    @classmethod
    def from_config(cls, config):
        return cls(**config)