import classes.const as const
from classes.ParkingLot import p as currLot
class Car:
    def __init__(self, license_number:str) -> None:
        self.licence_number = license_number
        pass

    def park(self):
        print("parking "+ self.licence_number)
        if currLot.isFull():
            print(const.PARKING_IS_FULL_SORRY + "for car number " + self.licence_number)
            return const.PARKING_IS_FULL_SORRY
        else:
            if currLot.CheckForSlot():
                currLot.AccomodateNewCar()
                print(const.PARKED_SUCCESSFULLY + "for car number " + self.licence_number)

                return const.PARKED_SUCCESSFULLY
            else:
                print("SOMETHING WRONG")    
            
            

    def __str__(self) -> str:
        return str(self.licence_number)
    pass