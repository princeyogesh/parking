import const, Slot, ParkingLot


class Car:
    def __init__(self, license_number) -> None:
        self.licence_number = license_number
        pass

    def park(self):
        if ParkingLot.isFull():
            return const.PARKING_IS_FULL_SORRY
        else:
            pass
        pass

    def __str__(self) -> str:
        return str(self.licence_number)
    pass