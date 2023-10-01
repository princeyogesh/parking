import const, Slot
class ParkingLot:
    def __init__(self, squareFootage = 0) -> None:
        self.area   = squareFootage
        self.length_slot = 12 #in feet
        self.width_slot  = 8 #in feet
        self.area_slot = self.findArea()
        self.number_of_slots = self.calculateNoofSlots()
        self.Slots = self.generateSlots()
        pass
    def findArea(self):
        return self.length * self.width
        pass

    def calculateNoofSlots(self):
        return self.area / self.area_slot
    
    def generateSlots(self):
        slotArray = []
        for i in range(self.number_of_slots):
            slotArray.append(Slot(const.UNOCCUPIED))

        return slotArray    
        pass