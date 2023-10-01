from classes.Slot import Slot

import classes.const as const

class ParkingLot:
    def __init__(self, squareFootage = 0) -> None:
        self.area   = squareFootage
        self.length_slot = 12 #in feet
        self.width_slot  = 8 #in feet
        self.area_slot = self.findArea()
        self.number_of_slots = self.calculateNoofSlots()
        self.Slots = self.generateSlots()
        self.FreeSlots = self.number_of_slots
        self.OccupiedSlots = 0
        pass
    def findArea(self):
        return self.length_slot * self.width_slot
        pass

    def calculateNoofSlots(self):
        return self.area / self.area_slot
    
    def generateSlots(self):
        slotArray = []
        for i in range(int(self.number_of_slots)):
            slotArray.append(Slot(const.UNOCCUPIED))

        return slotArray    
        pass
    
    def isFull(self):
        for i in self.Slots:
            if(i.status == const.UNOCCUPIED):
                return False

        return True
        pass

    def CheckForSlot(self):
        for i in self.Slots:
            if(i.status == const.UNOCCUPIED):
                return True
        
        
        return False
        pass

    def AccomodateNewCar(self):
        for i in self.Slots:
            if(i.status == const.UNOCCUPIED):
                i.status = const.OCCUPIED
                return
p = ParkingLot(1000)