


from Elevator import Elevator
# MAIN
if __name__ == "__main__":
    elevator = Elevator()
    #floors_to_request = [3, 1, 4, 2, 5, 7, 2, 8, 1]
    print(f"Requesting floor {6}")
    elevator.request(6)
    elevator.request(1)
    elevator.target(3)