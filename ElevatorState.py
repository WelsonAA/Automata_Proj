from enum import Enum


class ElevatorState(Enum):
    """Enumerated states for the elevator."""
    IDLE = "IDLE"
    MOVING_UP_TO_REQUESTED = "MOVING_UP_TO_REQUESTED"
    MOVING_DOWN_TO_REQUESTED = "MOVING_DOWN_TO_REQUESTED"
    MOVING_UP_TO_TARGET = "MOVING_UP_TO_TARGET"
    MOVING_DOWN_TO_TARGET = "MOVING_DOWN_TO_TARGET"
    OPEN_DOORS_AT_REQUESTED = "OPEN_DOORS_AT_REQUESTED"
    CLOSE_DOORS_AT_REQUESTED = "CLOSE_DOORS_AT_REQUESTED"
    ABOVE_REQUESTED_FLOOR = "ABOVE_REQUESTED_FLOOR"
    BELOW_REQUESTED_FLOOR = "BELOW_REQUESTED_FLOOR"
    AT_REQUESTED_FLOOR = "AT_REQUESTED_FLOOR"
    ABOVE_TARGET_FLOOR = "ABOVE_TARGET_FLOOR"
    BELOW_TARGET_FLOOR = "BELOW_TARGET_FLOOR"
    AT_TARGET_FLOOR = "AT_TARGET_FLOOR"
    OPEN_DOORS_AT_TARGET = "OPEN_DOORS_AT_TARGET"
    CLOSE_DOORS_AT_TARGET = "CLOSE_DOORS_AT_TARGET"
