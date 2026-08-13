import logging

from robot import InsufficientBatteryError


def fleet_report(robots):
    for robot in robots:
        print(str(robot))


def run_task_safely(robot, **kwargs):
    try:
        result = robot.perform_task(**kwargs)
    except InsufficientBatteryError as error:
        logging.error(str(error))
    else:
        print(f"Task result: {result}")
    finally:
        print(f"{robot.name} battery level: {robot.battery}%")