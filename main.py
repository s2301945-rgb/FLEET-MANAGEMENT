from robot import Robot
from robots import CleaningRobot, DroneRobot
from fleet import fleet_report, run_task_safely


def main():
    roomba = CleaningRobot("Roomba", battery=100, dust_capacity=500)
    aqua_drone = DroneRobot.from_config({"name": "Aqua-Drone", "battery": 15})

    print("--- Fleet report ---")
    fleet_report([roomba, aqua_drone])
    print()

    print("--- repr() check ---")
    print(repr(roomba))
    print(repr(aqua_drone))
    print()

    print(f"manufacturer: {Robot.manufacturer}")
    print(f"population so far: {Robot.population}")
    print()

    print("--- Running tasks safely ---")
    run_task_safely(roomba)
    run_task_safely(aqua_drone)  # only 15% battery, task needs 25% — triggers except
    print()

    print("--- Decorator identity check ---")
    print(CleaningRobot.perform_task.__name__)  # should print "perform_task", not "wrapper"


if __name__ == "__main__":
    main()