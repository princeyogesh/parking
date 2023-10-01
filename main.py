import classes.const as const
from classes.Car import Car
if __name__ == "__main__":
    number_plates = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n"]
    carsArr = []
    for i in number_plates:
        carsArr.append(Car(i))

    ###try to park each car from carArr#####
    for i in carsArr:
        print(str(i))
        i.park()
        pass

    print("MAIN")
    pass